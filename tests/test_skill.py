"""Проверки скилла effectcraft.

Статические — без EffectCraft (идут в CI). Живые — только если найден effectcraft-cli:
справочники совпадают с CLI, рецепты проходят check, рецепт исполняется и проверяется.

  python3 -m unittest discover -s tests -v
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "effectcraft"
SCRIPTS = SKILL / "scripts"
sys.path.insert(0, str(SCRIPTS))
import _common as C  # noqa: E402
import gate  # noqa: E402

LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path
    return text[4:text.index("\n---\n", 4)]


class Static(unittest.TestCase):
    def test_skills_in_repo(self):
        names = sorted(p.name for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").exists())
        self.assertEqual(names, ["effectcraft", "effectcraft-editor"])

    def test_frontmatter(self):
        for skill in (ROOT / "skills").iterdir():
            fm = frontmatter(skill / "SKILL.md")
            self.assertIn(f"name: {skill.name}\n", fm + "\n")
            self.assertIn("disable-model-invocation: true", fm)
            desc = re.search(r"^description: (.+)$", fm, re.M).group(1)
            self.assertLessEqual(len(desc), 1024, skill.name)

    def test_skill_md_size_and_links(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(text.splitlines()), 500)
        for link in LINK.findall(text):
            if not link.startswith("http"):
                self.assertTrue((SKILL / link).exists(), link)

    def test_no_installation(self):
        banned = re.compile(r"bootstrap|runtime\.lock|craft-runtimes|npx skills add|urlretrieve|curl |wget ")
        for f in SKILL.rglob("*"):
            if f.is_file() and f.suffix in (".md", ".py", ".json"):
                self.assertIsNone(banned.search(f.read_text(encoding="utf-8")), f)

    def test_topics_have_rules_toc_and_tables(self):
        for f in (SKILL / "references" / "topics").glob("*.md"):
            text = f.read_text(encoding="utf-8")
            self.assertIn("## Как работать", text, f.name)
            self.assertIn("Содержание:", text.split("## Как работать")[0], f.name)
            self.assertRegex(text, r"\| `[a-zA-Z]+\.[^`]+` \|", f.name)

    def test_rule_ids_unique(self):
        ids = []
        for f in [SKILL / "SKILL.md", *(SKILL / "references" / "topics").glob("*.md")]:
            ids += re.findall(r"\*\*([A-Z]{3}-\d\d)\.\*\*", f.read_text(encoding="utf-8"))
        self.assertEqual(len(ids), len(set(ids)))

    def test_recipes_shape(self):
        for f in (SKILL / "references" / "recipes").glob("*.json"):
            data = json.loads(f.read_text(encoding="utf-8"))
            self.assertEqual(data["id"], f.stem)
            self.assertTrue(data["steps"])
            for s in data["steps"]:
                self.assertEqual(set(s), {"command", "params"}, f.name)
            texts = [s["params"].get("text") for s in data["steps"] if s["params"].get("text")]
            for ph in data["placeholders"]:
                self.assertIn(ph, texts, f"{f.name}: заглушка {ph} не встречается в шагах")

    def test_gate_parses_saves(self):
        cwd = Path("/work")
        got = gate.saved_paths_from_bash("cd out && python3 ec.py run p.json --save-as a.ecproj", cwd)
        self.assertEqual(got, [Path("/work/out/a.ecproj")])
        got = gate.saved_paths_from_bash("effectcraft-cli exec x --project /p/b.ecproj --save", cwd)
        self.assertEqual(got, [Path("/p/b.ecproj")])
        self.assertEqual(gate.saved_paths_from_bash("ls --save-as x.ecproj", cwd), [])


@unittest.skipUnless(os.environ.get("EFFECTCRAFT_CLI") or Path.home().joinpath(".local/share/artcraft-cli").exists(),
                     "effectcraft-cli не найден")
class Live(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cli = C.find_cli()
        cls.version = C.cli_version(cls.cli)

    def ec(self, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / "ec.py"), *args], capture_output=True, text=True, timeout=600)

    def test_references_match_cli(self):
        r = subprocess.run([sys.executable, str(SCRIPTS / "build_refs.py"), "--check"], capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_manual_rules_name_live_commands(self):
        live = {c["id"] for c in C.catalog(self.cli)}
        for f in [SKILL / "SKILL.md", SKILL / "references" / "recipes.md", *(SKILL / "references" / "topics").glob("*.md")]:
            manual = f.read_text(encoding="utf-8").split("<!-- generated:start -->")[0]
            for cid in re.findall(r"`([a-z][A-Za-z]+\.[A-Za-z0-9.]+[A-Za-z0-9])`", manual):
                if cid.startswith(("app.", "ec.", "verify.")) or cid.endswith((".py", ".json", ".md", ".ecproj", ".png")):
                    continue
                self.assertTrue(cid in live or any(c.startswith(cid + ".") for c in live), f"{f.name}: {cid}")

    def test_recipes_check(self):
        for f in (SKILL / "references" / "recipes").glob("*.json"):
            r = self.ec("check", str(f))
            problems = [p for p in json.loads(r.stdout)["problems"] if "заглушка" not in p]
            self.assertEqual(problems, [], f.name)

    def test_recipe_runs_and_verifies(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.environ["XDG_STATE_HOME"] = tmp
            out = Path(tmp) / "lt.ecproj"
            r = self.ec("run", str(SKILL / "references/recipes/lower-third.json"), "--save-as", str(out), "--allow-placeholders")
            self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
            r = self.ec("verify", str(out), "--alpha", "--times", "0.2,3")
            report = json.loads(r.stdout)
            self.assertTrue(report["ok"], report)
            self.assertTrue(C.receipt_path(C.sha256(out)).exists())


if __name__ == "__main__":
    unittest.main()
