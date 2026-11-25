# EffectCraft skills

Один скилл для работы агента в EffectCraft через уже установленный CLI и MCP, рецепты типовых сцен и субагент-проверяющий. Форк `full-aigc-skills/effectcraft-skills`, переложенный по схеме «один рабочий скилл + справочники по темам + проверка кодом + хук на сдачу + независимый проверяющий».

Справочники собраны с **EffectCraft CLI 0.25.1** (766 команд).

## Состав

| Что | Где | Зачем |
| --- | --- | --- |
| Скилл `effectcraft` | `skills/effectcraft/` | Чек-лист работы, 12 общих правил (EC-01…EC-12), темы и рецепты. Вызов только командой `/effectcraft`. |
| Темы | `skills/effectcraft/references/topics/*.md` | 13 тем: ручной раздел «Как работать» с правилами по ID и сгенерированная таблица всех команд темы. |
| Рецепты | `skills/effectcraft/references/recipes/` | Титр главы, отсчёт, финальные титры, плашка, кинетический текст, логотип, луп, замена экрана. |
| Скрипты | `skills/effectcraft/scripts/` | `ec.py` — поиск CLI, каталог, проверка плана, запуск, `verify`; `build_refs.py` — сборка справочников; `gate.py` — хуки. |
| Хуки | frontmatter `SKILL.md` | PostToolUse запоминает сохранённые `.ecproj`, Stop не даёт закончить без `ec.py verify` последней версии. |
| Субагент | `agents/effectcraft-verifier.md` | Независимая проверка проекта против задания. Хук запрещает ему сохранять. |
| `effectcraft-editor` | `skills/effectcraft-editor/` | Встроенный редактор из исходного пакета; работает только с плагином `effectcraft-plugin`. |

Установки нет: скилл не скачивает и не обновляет EffectCraft, Python или пакеты. Нет CLI — `ec.py which` говорит, как его поставить.

## Подключение в Claude Code

```bash
ln -s "$PWD/skills/effectcraft" ~/.claude/skills/effectcraft
ln -s "$PWD/agents/effectcraft-verifier.md" ~/.claude/agents/effectcraft-verifier.md
```

Codex и другие агенты читают `SKILL.md` по стандарту Agent Skills. Хуки во frontmatter и `${CLAUDE_SKILL_DIR}` — расширения Claude Code; в остальных агентах `scripts/` лежит рядом с `SKILL.md`, проверку `ec.py verify` запускай сам.

## Новая версия EffectCraft

```bash
python3 skills/effectcraft/scripts/build_refs.py
python3 skills/effectcraft/scripts/build_refs.py --check
python3 -m unittest discover -s tests -v
```

`build_refs.py` переписывает только таблицы команд и `VERSION`. Живые тесты сверяют справочники с CLI, проверяют, что команды из ручных правил существуют, прогоняют рецепты через `check`, собирают плашку и проверяют её `verify --alpha`. Без CLI идут только статические тесты (так в CI).

## Что изменилось относительно исходного пакета

Было 26 скиллов: 14 почти одинаковых `effectcraft-cli*`, зонтик `effectcraft-use`, исполнитель `effectcraft-harness` с установкой закреплённого CLI 0.4.0 и Python, 9 сценовых скиллов на 0.10.0. Стало: один скилл, справочники по темам с CLI 0.25.1, рецепты внутри скилла, проверка кодом, хук и субагент. История исходного пакета — в `RELEASE-HISTORY.md`.
