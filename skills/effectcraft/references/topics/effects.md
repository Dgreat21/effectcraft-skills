# Эффекты

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды effect.* (25)](#команды-effect-25)
- [Команды effects.* (1)](#команды-effects-1)
<!-- toc:end -->

## Как работать

- **EFX-01.** Список эффектов — `list_effects` (MCP) или `ec.py search effect.`. Есть в списке — ещё не значит, что рендерится как надо: проверь кадром.
- **EFX-02.** Порядок эффектов влияет на результат. Пути параметров — `effects/#N/<параметр>` из `props --flat`.
- **EFX-03.** Эффект отключён или у него нет описания параметров — остановись и назови пробел, не подменяй похожим.
- **EFX-04.** Тяжёлые эффекты сначала смотри `render-frame` в четверть размера.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды effect.* (25)

| id | что делает | параметры |
| --- | --- | --- |
| `effect.apply` | Apply Effect | {effect: id\|name (e.g. Gaussian Blur), layers?} |
| `effect.applyLast` | Last Effect (Effect) | {layers?} |
| `effect.copy` | Copy Effects | {layer?, effect? \| effects?: [uid\|name\|index]} (default: the selected effects) |
| `effect.cryptomatteAt` | Cryptomatte At | {layer?, effect?: index\|uid\|name, x, y (effect space), scale?, time?, probeOnly?: bool (don't build the probe)} → {name, hash, layer, selected} \| {pending} \| null — the Cryptomatte ID under the point |
| `effect.duplicate` | Duplicate Effect | {layer?, effect} |
| `effect.editDropdown` | Edit Dropdown Menu | {layer, path?\|prop?, items: [string]} |
| `effect.helpers.list` | List Effect Helpers | {} → {helpers: [{program, name, version, loads, running, effects, restarts, error}], blocked: [effect ids]} |
| `effect.helpers.load` | Load Plug-ins Through Helper... | {path (a file or folder an installed helper accepts, e.g. a folder of .ofx plug-ins for an OpenFX helper; the menu asks for a folder)} → {loaded: [{id, name, category, helper}], errors} |
| `effect.helpers.scan` | Scan for Effect Helpers | {retry?} → {paths, helpers, loaded, errors}: starts the effect helpers installed in helpers/ next to the app, helpers/ in the settings folder and EFFECTCRAFT_HELPER_PATH, and adds their effects; retry turns effects that kept stopping their helper back on |
| `effect.list` | List Effects | {filter?} → [{params: [{id, name, type, default, options?, min?, max?, sliderMin?, sliderMax?, decimals?}]}]; popup indices are zero-based (JSX uses one-based values) |
| `effect.manage` | Manage Effects... (Effect) | {} |
| `effect.paste` | Paste Effects | {layers?} — adds the copied effects to the layers |
| `effect.pickColor` | Pick Effect Colour | {layer?, effect?: index\|uid\|name, param: id (e.g. screenColour) \| prop: uid, x, y (effect space), average?: bool (5×5), time?} — the colour of the effect's input there |
| `effect.pickCryptomatte` | Pick Cryptomatte | {layer?, effect?: index\|uid\|name, x, y (effect space), mode?: replace\|add\|remove (default replace), scale? (preview resolution, default 1), time?, probeOnly?} → {name, hash, layer, selection, changed, selected} \| {pending} — edits the Cryptomatte effect's Selection with the ID under the point |
| `effect.plugins.install` | Install Effect Plug-in... | {path (.wasm plug-in: copied into the Plug-ins folder and loaded on every start) \| folder (a plug-in bundle: every .wasm goes into the Plug-ins folder and every .jsx becomes a ScriptUI panel), bundle? (the menu: ask for a folder)} |
| `effect.plugins.list` | List Effect Plug-ins | {} → {api, wasm, helpers, plugins: [{id, name, category, version, author, source, params, error}]} |
| `effect.plugins.load` | Load Effect Plug-in... | {path (.wasm / .wat plug-in, WebAssembly ABI 1 or 2) \| folder (loads every .wasm in it)} |
| `effect.remove` | Remove Effect | {layer?, effect: index\|uid\|name} |
| `effect.removeAll` | Remove All (Effect) | {layers?} |
| `effect.reorder` | Reorder Effect | {layer?, effect, index} |
| `effect.reset` | Reset Effect | {layer?, effect} |
| `effect.setLabel` | Effect Label | {layer?, effect, label: name\|index 0-16 (None clears)} |
| `effect.swapTintColors` | Swap Tint Colors | {comp?, layer?, effect?: index\|uid\|name} — swaps Tint's Map Black To and Map White To at the current layer time in one undo step |
| `effect.toggle` | Toggle Effect | {layer?, effect, value?} |
| `effect.warning` | Effect Warning | {layer?, effect?: index\|uid\|name (default: the selected effect), time?} → {effect, warning: string\|null} — what Effect Controls warns about (an OCIO config it can't read, transforms it passes through) |

## Команды effects.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `effects.copyPresetsFolderPath` | Copy Presets Folder Path | {} |

<!-- generated:end -->
