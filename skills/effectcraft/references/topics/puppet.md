# Куклы (Puppet)

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды puppet.* (10)](#команды-puppet-10)
<!-- toc:end -->

## Как работать

- **PUP-01.** Кукла работает на видимом слое (материал, сплошной, текст, шейп, прекомп), не на null.
- **PUP-02.** Координаты булавок — в пространстве эффекта (слоя), не композиции.
- **PUP-03.** Первая `puppet.addPin` создаёт эффект Puppet и сетку. Следующие булавки ставь в ту же сетку (`mesh`), лишние `newMesh` не плоди.
- **PUP-04.** ID сетки и булавок бери из ответов и `puppet.info`. Индекс в массиве — не идентификатор.
- **PUP-05.** Запись: `puppet.recordOptions` (настройка сессии, в проект не сохраняется — задавай каждый раз) → `puppet.recordPin` с `samples` вида `[t, x, y]`, где t — секунды от начала записи.
- **PUP-06.** `puppet.follow`: `leader`, `pins`, `delay` (сек), `amount` (%), `cascade`. Меняет только перечисленные булавки.
- **PUP-07.** Проверка: `puppet.info`, ключи и кадры. Показанная сетка — ещё не результат.
- В DgreatStudio куклы собирает кит `ikigai-motion` (скелет кита + Puppet). Этот файл — про команды движка.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды puppet.* (10)

| id | что делает | параметры |
| --- | --- | --- |
| `puppet.addPin` | Add Puppet Pin | {layer?, kind?: position\|advanced\|bend\|starch\|overlap, position: [x,y] (effect space), time? (s) \| frame?, mesh?: uid, newMesh?, density?, expansion?, triangles?} |
| `puppet.follow` | Follow-Through... | {layer?, leader?: uid \| name (default: the first selected pin), pins?: [uid \| name…] (default: the other selected pins), delay? (s, 0.1), amount? (%, 100), cascade? (true: the k-th nearest pin trails k × delay)} |
| `puppet.info` | Puppet Mesh Info | {layer?, time? \| frame?} |
| `puppet.mesh` | Puppet Mesh Options | {layer?, mesh?: uid, density?, expansion?, triangles?, showMesh?, time?, merge?} |
| `puppet.movePin` | Move Puppet Pin | {layer?, pin: uid \| name, position: [x,y], time? \| frame?, merge?} |
| `puppet.recordOptions` | Record Options... | {speed? (%, 100), smoothing? (0-100), useDraftDeformation?, showMesh?} |
| `puppet.recordPin` | Record Puppet Pin | {layer?, pin: uid \| name, samples: [[t, x, y]…] (t = seconds since the drag began, effect space), pins?: [uid \| name…] (more pins that move by the same displacement), start? (s, default current time), speed? (%, Record Options), smoothing? (Record Options)} |
| `puppet.removePin` | Delete Puppet Pin | {layer?, pin?: uid \| name, pins?: [uid \| name…]} (default: the selected pins) |
| `puppet.selectPins` | Select Puppet Pins | {layer?, pins: [uid \| name…] ([] deselects), add?, toggle?} |
| `puppet.setPin` | Edit Puppet Pin | {layer?, pin: uid \| name, position?, scale? (%), rotation? (°), amount? (%), extent? (px), inFront?, time? \| frame?, merge?} |

<!-- generated:end -->
