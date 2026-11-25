# Материалы и импорт

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды file.* (1)](#команды-file-1)
- [Команды footage.* (12)](#команды-footage-12)
- [Команды layer.* (1)](#команды-layer-1)
- [Команды mediaBrowser.* (7)](#команды-mediabrowser-7)
<!-- toc:end -->

## Как работать

- **FTG-01.** Импорт возвращает id элемента проекта. В композицию его ставит `layer.addItem` с этим id — не ищи элемент по имени файла.
- **FTG-02.** Импорт метаданных ещё не значит, что видео декодируется. Отрендери два кадра в разные моменты и убедись, что виден сам материал, а не слои под ним.
- **FTG-03.** PSD и SVG переносятся не полностью: структура слоёв, шрифты, эффекты. Сверь с оригиналом.
- **FTG-04.** Замена материала с сохранением анимации — `layer.replaceSource` и команды replace. Исходники не трогай; прокси — отдельный файл, и его тоже проверь кадром.
- **FTG-05.** Не перекодируй исходники без просьбы.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды file.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `file.relinkFootage` | Relink Missing Footage... (File › Dependencies) | {folder: string (recursive desktop search, no symlinks; max 100000 entries), dryRun?: bool (report only), wait?: bool (return results inline; otherwise jobs.list/jobs.wait)} — relinks only unique exact filenames with compatible metadata; preserves interpretation and sequence ranges. Reports high/low confidence and ambiguous, incompatible, unsupported or notFound items. |

## Команды footage.* (12)

| id | что делает | параметры |
| --- | --- | --- |
| `footage.check` | Check Footage | {items?: [id], wait?} — look for every footage file (in the background unless `wait`) and flag missing items |
| `footage.clearInOut` | Clear In and Out | {} |
| `footage.info` | Footage Panel State | {} |
| `footage.missing` | Missing Footage | {} → {missing: [{item, name, path}]} |
| `footage.open` | Open in Footage Panel | {item: id\|name} |
| `footage.overlayEdit` | Overlay Edit | {item?, comp?, in? (s), out? (s), at? (comp s; default the current time)} |
| `footage.relink` | Relink Footage | {item, path} — point a footage item at its file's new location (keeps the interpretation) and relink the other missing files found in the same place |
| `footage.reloadChanged` | Reload Changed Footage | {} — reload the footage whose file changed on disk since it was last seen (size or modification time; Settings ▸ Import ▸ Automatically Reload Footage runs this in the background; image sequences only with All Footage); files seen for the first time are only remembered. Returns {files, reloaded} |
| `footage.rippleInsertEdit` | Ripple Insert Edit | {item?, comp?, in? (s), out? (s), at? (comp s; default the current time)} |
| `footage.setIn` | Set In Point | {time? \| frame? (default: the panel's time)} |
| `footage.setOut` | Set Out Point | {time? \| frame? (default: the panel's time)} |
| `footage.setTime` | Footage Panel Time | {time? (s, source) \| frame?} |

## Команды layer.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `layer.replaceSource` | Replace Layer Source | {comp?, layers?, layer?, item?: id\|name (default the Project panel selection), fixExpressions?: bool (accepted for After Effects compatibility)} → {layers, item} |

## Команды mediaBrowser.* (7)

| id | что делает | параметры |
| --- | --- | --- |
| `mediaBrowser.action` | Media Browser Action | {action}: an action from mediaBrowser.list's `actions` (web: openFolder, addFiles, uploadFolder) |
| `mediaBrowser.addFavorite` | Add to Favorites | {path?} |
| `mediaBrowser.fileInfo` | File Info | {path} |
| `mediaBrowser.go` | Go to Folder | {path?: folder \| "..", importableOnly?} |
| `mediaBrowser.import` | Import | {paths, sequence? (default true: a numbered still brings its image sequence), addToComp?, time?, index?, position? (where the layers go, as in layer.addItem)} |
| `mediaBrowser.list` | List Folder | {path?, importableOnly?} |
| `mediaBrowser.removeFavorite` | Remove from Favorites | {path?} |

<!-- generated:end -->
