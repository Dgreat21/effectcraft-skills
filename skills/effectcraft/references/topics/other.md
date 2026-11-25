# Правка, интерфейс, шаблоны и прочее

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды app.* (12)](#команды-app-12)
- [Команды cache.* (1)](#команды-cache-1)
- [Команды command.* (2)](#команды-command-2)
- [Команды contentFill.* (2)](#команды-contentfill-2)
- [Команды edit.* (27)](#команды-edit-27)
- [Команды editor.* (1)](#команды-editor-1)
- [Команды engine.* (1)](#команды-engine-1)
- [Команды essential.* (22)](#команды-essential-22)
- [Команды face.* (5)](#команды-face-5)
- [Команды help.* (14)](#команды-help-14)
- [Команды jobs.* (3)](#команды-jobs-3)
- [Команды journal.* (1)](#команды-journal-1)
- [Команды learn.* (5)](#команды-learn-5)
- [Команды library.* (8)](#команды-library-8)
- [Команды liquify.* (2)](#команды-liquify-2)
- [Команды markers.* (5)](#команды-markers-5)
- [Команды motion.* (1)](#команды-motion-1)
- [Команды paint.* (6)](#команды-paint-6)
- [Команды paths.* (3)](#команды-paths-3)
- [Команды playback.* (6)](#команды-playback-6)
- [Команды prefs.* (5)](#команды-prefs-5)
- [Команды scopes.* (1)](#команды-scopes-1)
- [Команды script.* (4)](#команды-script-4)
- [Команды scriptui.* (9)](#команды-scriptui-9)
- [Команды shortcuts.* (7)](#команды-shortcuts-7)
- [Команды storage.* (3)](#команды-storage-3)
- [Команды templates.* (5)](#команды-templates-5)
- [Команды view.* (62)](#команды-view-62)
- [Команды warp.* (3)](#команды-warp-3)
- [Команды window.* (9)](#команды-window-9)
<!-- toc:end -->

## Как работать

- Шаблоны: `ec.py -- render --template T.ectemplate --values V.json --out F` рендерит один экземпляр. Essential Graphics — команды `essential.*`.
- Журнал и сбои: `journal.export` пишет сценарий, `ec.py -- replay SCRIPT.jsonl` воспроизводит его без окна.
- `view.*`, `window.*`, `help.*`, `prefs.*`, `shortcuts.*` — интерфейс. Без окна они обычно не нужны.
- `library.*` ставит внешние библиотеки — только по прямой просьбе (EC-10).

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды app.* (12)

| id | что делает | параметры |
| --- | --- | --- |
| `app.about` | About EffectCraft... | {} |
| `app.capabilities` | App Capabilities | {} → version, command/effect counts, export formats, parity summary |
| `app.commandPalette` | Quick Apply... (Edit) | {query?} |
| `app.find` | Find (File) | {query?: string, status?: all\|available\|missing} |
| `app.gpuInfo` | GPU Information... | {} |
| `app.hide` | Hide EffectCraft | {} |
| `app.hideOthers` | Hide Others | {} |
| `app.keyboardShortcuts` | Keyboard Shortcuts (Edit) | {} |
| `app.quit` | Quit EffectCraft | {} |
| `app.settings` | Settings... | {page?: general\|startup\|project\|composition\|previews\|appearance\|grids\|labels\|type\|import\|export\|audio\|disk\|memory\|video\|3d\|scripting} |
| `app.showAll` | Show All | {} |
| `app.templates` | Templates | {kind: renderSettings\|outputModule} |

## Команды cache.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `cache.diskStats` | Disk Cache Statistics | {} |

## Команды command.* (2)

| id | что делает | параметры |
| --- | --- | --- |
| `command.describe` | Describe Command | {command} → id, label, menu, shortcut, params doc, JSON `schema`, enabled |
| `command.list` | List Commands | {filter?, enabledOnly?, schemas? (add each command's params JSON Schema)} |

## Команды contentFill.* (2)

| id | что делает | параметры |
| --- | --- | --- |
| `contentFill.generate` | Generate Fill Layer | {layer?, method?: object\|surface\|edgeBlend, range?: workArea\|entire, alphaExpansion? (px), lightingCorrection?: none\|subtle\|moderate\|strong, referenceLayer?, referenceTime? (s), outputDir?, wait?: bool} |
| `contentFill.set` | Content-Aware Fill Settings | {method?: object\|surface\|edgeBlend, range?: workArea\|entire, alphaExpansion? (px), lightingCorrection?: none\|subtle\|moderate\|strong, referenceLayer?: layer\|null, referenceTime? (s)} |

## Команды edit.* (27)

| id | что делает | параметры |
| --- | --- | --- |
| `edit.clear` | Clear (Edit) | {layers?} |
| `edit.copy` | Copy (Edit) | {layers?} (keyframes, effects or shape items when they are selected) |
| `edit.copyExpressionOnly` | Copy Expression Only (Edit) | {} |
| `edit.copyWithPropertyLinks` | Copy with Property Links (Edit) | {layers?} (selected properties, or layers, as expressions linking to the originals) |
| `edit.copyWithRelativePropertyLinks` | Copy with Relative Property Links (Edit) | {layers?} (like Copy with Property Links, using thisComp) |
| `edit.cut` | Cut (Edit) | {layers?} (keyframes, effects or shape items when they are selected) |
| `edit.deselectAll` | Deselect All (Edit) | {} |
| `edit.duplicate` | Duplicate (Edit) | {layers?, merge?} (without layers: during a text edit the edited layer, else the selected effects, shape items or text animators, else the selected layers) |
| `edit.editOriginal` | Edit Original... (Edit) | {} |
| `edit.extractWorkArea` | Extract Work Area (Edit) | {layers?} |
| `edit.history` | History | {steps?: n (undo n steps), redo?: n} |
| `edit.history.goto` | Go to History State | {index? (from edit.history.list) \| id? \| steps? (negative = back along the line)} |
| `edit.history.list` | History | {} → {states: [{index, id, label, parent, depth, current, line, future}], current, branches} |
| `edit.label` | Label (Edit › Label) | {label: Red\|Yellow\|Aqua\|…, layers?, keys?, target?: layers} |
| `edit.liftWorkArea` | Lift Work Area (Edit) | {layers?} |
| `edit.paste` | Paste (Edit) | {} (layers, keyframes at the CTI, effects, shape items into the selected shape layers, or property links / expressions) |
| `edit.pasteReversedKeyframes` | Paste Reversed Keyframes (Edit) | {layers?, prop?\|path?, time?} |
| `edit.pasteSvg` | Paste SVG as Shapes | {svg: SVG markup, name?, comp?} → {layer, skipped} (Edit ▸ Paste runs it for SVG on the system clipboard) |
| `edit.pasteTextFormattingOnly` | Paste Text Formatting Only (Edit) | {layer?} (the copied text's formatting on the selected text or text layers) |
| `edit.pasteTextMatchFormatting` | Paste Text and Match Formatting (Edit) | {text?} (the clipboard's text in the style at the caret) |
| `edit.purge` | Purge | {what?: all\|memoryAndDisk\|memory\|disk\|3d\|image\|snapshot} |
| `edit.purgeUndo` | Undo (Edit › Purge) | {} |
| `edit.redo` | Redo (Edit) | {} |
| `edit.selectAll` | Select All (Edit) | {} |
| `edit.selectLabelGroup` | Select Label Group (Edit › Label) | {} |
| `edit.splitLayer` | Split Layer (Edit) | {layers?} |
| `edit.undo` | Undo (Edit) | {} |

## Команды editor.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `editor.state` | Editor State | {} |

## Команды engine.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `engine.batch` | Run Commands (Batch) | {steps: [{command, params?}], label? (undo step name, default Batch), atomic?: bool (default true: a failing step rolls the whole batch back)} → {steps, results: [each step's result]}; a string param "$N" or "$N.key.0" is step N's result (1-based), e.g. {"layer": "$1.layer"} |

## Команды essential.* (22)

| id | что делает | параметры |
| --- | --- | --- |
| `essential.addComment` | Add Comment | {comp?, text?, group?} |
| `essential.addGroup` | Add Group | {comp?, name?, index?} |
| `essential.addMedia` | Add Media Replacement | {layer, name?, group?} |
| `essential.addMirror` | Add Mirror | {comp?, control, name?, group?, index?} |
| `essential.addProperty` | Add Property to Essential Graphics (Animation) | {comp?, layer?, path?\|prop?: uid (default: the selected properties), name?, group?: control id, index?, as?: font (Source Text font family/style/size) \| scale (uniform Scale), mirror?: bool (a property already present is added as a mirror; default true)} |
| `essential.canAdd` | Can Add Property to Essential Graphics | {layer, path\|prop, as?} → {ok, type?, reason?} |
| `essential.exportTemplate` | Essential Graphics Template... (File › Export) | {comp?, path (.ectemplate), name?} |
| `essential.importTemplate` | Essential Graphics Template... (File › Import) | {path (.ectemplate), comp?, addToComp?: bool} |
| `essential.instance` | Essential Properties of a precomp layer | {layer} |
| `essential.linkProperty` | Link Property to Control | {comp?, control, layer?, path?\|prop? (default: the selected property)} |
| `essential.list` | Essential Graphics controls | {comp?, supported?: bool} |
| `essential.move` | Move Control | {comp?, control, group?: id (null = top level), index?} |
| `essential.pushToComp` | Push Override Values to Source | {layer, control? (default: all overridden)} |
| `essential.remove` | Remove Control | {comp?, control} |
| `essential.rename` | Rename Control | {comp?, control, name} |
| `essential.revert` | Revert | {layer, control? (default: all overridden)} |
| `essential.set` | Set Essential Property | {layer, control: id\|name, value \| item (media)} |
| `essential.setName` | Essential Graphics Name | {comp?, name} |
| `essential.setPrimary` | Primary Composition | {comp} |
| `essential.soloSupported` | Solo Supported Properties | {on?} |
| `essential.templateInfo` | Read a template's manifest | {path} |
| `essential.unlinkProperty` | Unlink Property | {comp?, control, layer?, path?\|prop? (default: the selected property)} |

## Команды face.* (5)

| id | что делает | параметры |
| --- | --- | --- |
| `face.model.download` | Download Face Tracking Model | {id, wait?} — the official model, verified (desktop; uses the system curl) |
| `face.model.install` | Install Face Tracking Model | {path: model file, id?, wait?} — verified against the registry's SHA-256 |
| `face.model.remove` | Remove Face Tracking Model | {id} |
| `face.model.select` | Use Face Tracking Model | {id: classical\|mediapipe-face, wait?} (face tracking uses it; wait: loaded before returning) |
| `face.models` | Face Tracking Models | {} |

## Команды help.* (14)

| id | что делает | параметры |
| --- | --- | --- |
| `help.appPage` | EffectCraft Home Page (Help) | {} |
| `help.discord` | Join the ArtCraft Discord... (Help) | {} |
| `help.docs` | EffectCraft Help... | {page?: help\|scripting\|expressions\|effects\|agents} |
| `help.enableLogging` | Enable Logging (Help) | {on?} |
| `help.exportRepro` | Save Bug Repro... | {path? (default: Repros in the settings folder)} → {path, steps}: the steps since the project was opened, for a bug report (commands and parameters only) |
| `help.github` | EffectCraft on GitHub (Help) | {} |
| `help.inAppTutorials` | In-App Tutorials... (Help) | {} → the Home screen's Learn tab |
| `help.onlineTutorials` | Online Tutorials... (Help) | {} |
| `help.reportIssue` | Provide Feedback... (Help) | {} |
| `help.revealLogFile` | Reveal Logging File (Help) | {} |
| `help.sibling` | Other ArtCraft Apps | {app: photocraft\|vectorcraft\|filmcraft\|lightcraft\|pdfcraft\|designcraft, kind?: page\|github} |
| `help.systemInfo` | System Information | {} |
| `help.systemReport` | System Compatibility Report... (Help) | {quiet?} |
| `help.website` | ArtCraft Website (Help) | {} |

## Команды jobs.* (3)

| id | что делает | параметры |
| --- | --- | --- |
| `jobs.cancel` | Cancel Job | {job?: render\|track\|maskTrack\|warp\|camera\|roto\|task:<n>\|all} |
| `jobs.list` | Background Jobs | {} |
| `jobs.wait` | Wait for Background Jobs | {} |

## Команды journal.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `journal.export` | Export Command Journal | {path? (write the script there)} → {script, steps} or {path, steps}: the commands run since the project was last opened, as a replay script (docs/agents.md, Repro scripts) |

## Команды learn.* (5)

| id | что делает | параметры |
| --- | --- | --- |
| `learn.list` | Learn Tutorials | {} → [{id, title, summary, minutes, steps}] |
| `learn.start` | Start Tutorial | {id} |
| `learn.state` | Tutorial State | {} → {tutorial, step, steps, done, current: {title, text, target, accepts}} \| null |
| `learn.step` | Tutorial Step | {action?: next\|back\|showMe\|goto, index?} |
| `learn.stop` | Close Tutorial | {} |

## Команды library.* (8)

| id | что делает | параметры |
| --- | --- | --- |
| `library.install` | Install Plug-in | {id, version?, wait?} — downloads the release (a GitHub release asset, in the package's repo when it names one), checks its SHA-256 against the catalog, loads it |
| `library.list` | Plug-in Library | {query?, tag?, installed?: bool} → {catalog, fetched, packages: [{id, name, author, description, license, repo, tags, latest, effects, installed, updateAvailable, needsNewerApp, loaded, restartNeeded, video, previewed, unlisted?}], tags, busy, error, folder, available} |
| `library.loadInstalled` | Load Installed Plug-ins | {} → {loaded, errors} (the app runs it at start-up) |
| `library.missing` | Missing Effects in the Plug-in Library | {} → {effects: [{effect, packages: [package id]}]} — effects the project uses that aren't installed, and the catalog packages that provide them |
| `library.preview` | Preview Plug-in | {id, version?, wait?} → {id, version, width, height, fps, frames, changes, animated, effect: manifest} — downloads the release (checked like an install) and renders its effect on a sample frame at default settings, without installing it |
| `library.refresh` | Refresh Plug-in Catalog | {catalog?: https:// or file:// URL of an index.json (default: the community catalog; file:// takes a local path, not a network path such as //server/share), wait?} |
| `library.uninstall` | Remove Plug-in | {id} — its effects stay registered until the next start |
| `library.update` | Update Plug-ins | {id? (default: every package with an update), wait?} |

## Команды liquify.* (2)

| id | что делает | параметры |
| --- | --- | --- |
| `liquify.clear` | Clear Liquify Mesh | {layer?, effect?: uid} |
| `liquify.stroke` | Liquify Stroke | {layer?, effect?: uid, tool?: warp\|turbulence\|twirlClockwise\|twirlCounterclockwise\|pucker\|bloat\|shiftPixels\|reflection\|clone\|reconstruction\|freeze\|thaw, points: [[x,y],…] (effect space), size?, pressure? (1-100), jitter? (1-100), cloneOffset?: [dx,dy], time? (s) \| frame?} |

## Команды markers.* (5)

| id | что делает | параметры |
| --- | --- | --- |
| `markers.convert` | Convert Marker | {layer? (layer marker → comp marker), index? \| at?, toLayer? (comp marker → layer marker)} |
| `markers.delete` | Delete Marker | {layer?, index? \| at? (comp s)} |
| `markers.list` | List Markers | {layer? (omit for composition markers)} |
| `markers.nested` | Nested Comp Markers | {layer: a precomp layer, comp?} — its comp's markers at their times in this comp (as on the layer bar) |
| `markers.set` | Marker Settings | {layer? (omit: comp marker), index? (0-based) \| at? (comp s) \| new?: true, time? (comp s), duration? (s), comment?, chapter?, url?, frameTarget?, cuePoint?: {name, navigation?, params?: [[name, value]…]} \| null, protected?, label?} |

## Команды motion.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `motion.sketch` | Motion Sketch | {layer?, points: [[t, x, y]…] (t = capture seconds) \| [[x, y]…] (one per frame), start? (s, default current time), captureSpeed? (%, 100), smoothing? (px, 1)} |

## Команды paint.* (6)

| id | что делает | параметры |
| --- | --- | --- |
| `paint.brushPreset` | Brush Preset | {preset?: index \| name} |
| `paint.options` | Paint Options | {color?, background?, opacity?, flow?, mode?, channels?, durationMode?, customFrames?, eraseMode?, diameter?, angle?, roundness?, hardness?, spacing?, preset?, sizePressure?, minSize?, opacityPressure?, flowPressure?, clonePreset?, cloneSource?, clonePoint?, cloneOffset?, aligned?, lockSourceTime?, cloneTimeShift?, cloneTime?, showOverlay?, overlayOpacity?, overlayDifference?, reset?} |
| `paint.presets` | Brush Presets | {} |
| `paint.removeStroke` | Delete Paint Stroke | {layer?, stroke: uid \| name} |
| `paint.setCloneSource` | Set Clone Source | {layer?, point: [x,y]} |
| `paint.stroke` | Paint Stroke | {layer?, kind?: brush\|clone\|eraser, points: [[x,y,pressure?],…] (effect space), time? (s) \| frame?, duration? (s, drawing time for Write On), color?: [r,g,b,a], diameter?, angle?, hardness?, roundness?, spacing?, opacity?, flow?, mode?, channels?: RGBA\|RGB\|Alpha, durationMode?: constant\|writeOn\|singleFrame\|custom, customFrames?, eraseMode?: layerSourceAndPaint\|paintOnly\|lastStrokeOnly, cloneSource?: layer id, clonePosition?: [x,y], cloneTimeShift? (s), lockSourceTime?, cloneTime? (s), sizePressure?, minSize?, opacityPressure?, flowPressure?} |

## Команды paths.* (3)

| id | что делает | параметры |
| --- | --- | --- |
| `paths.nullsFollowPoints` | Nulls Follow Points | {layer?, path?\|prop?, pins?: [uid \| name…]} → a null per vertex (or puppet pin) following it (Position expressions) |
| `paths.pointsFollowNulls` | Points Follow Nulls | {layer?, path?\|prop?, pins?: [uid \| name…]} → a null per vertex (or Position / Advanced puppet pin); the path (pins) follow them (expressions) |
| `paths.tracePath` | Trace Path | {layer?, path?\|prop?, loop?: bool} → a null moving along the path (Progress slider) |

## Команды playback.* (6)

| id | что делает | параметры |
| --- | --- | --- |
| `playback.audio` | Audio (Composition › Preview) | {value?: include audio in previews} |
| `playback.cacheWhenIdle` | Cache Frames When Idle (Composition › Preview) | {value?} |
| `playback.scrubAudio` | Scrub Audio | {time? (s, default the current time)} — plays one frame of the comp's audio there (Ctrl/Cmd-drag the current time) |
| `playback.settings.get` | Preview Settings | {shortcut?: spacebar\|shiftSpacebar\|numpad0\|shiftNumpad0\|altNumpad0 (default: the one shown in the Preview panel)} → options + plan {start, end, first, step, fps} |
| `playback.settings.set` | Change Preview Settings | {shortcut?, current?: shortcut shown in the panel, reset?: bool, values?: {…}, includeVideo?, includeAudio?, includeOverlays?, includeLayerControls?, loop?, cacheBeforePlayback?, range?: workArea\|workAreaExtended\|entireDuration\|aroundCurrentTime, preRoll?, postRoll?: seconds, playFrom?: rangeStart\|currentTime, frameRate?: fps\|"auto", skip?, resolution?: auto\|full\|half\|third\|quarter\|custom, customResolution?, fullScreen?, playCachedFrames?, moveTimeToPreviewTime?} |
| `playback.toggle` | Play Current Preview (Composition › Preview) | {shortcut?: spacebar\|shiftSpacebar\|numpad0\|shiftNumpad0\|altNumpad0 (whose Preview panel options to use; default spacebar)} |

## Команды prefs.* (5)

| id | что делает | параметры |
| --- | --- | --- |
| `prefs.get` | Get Setting | {key?: e.g. general.undoLevels (omit for all settings)} |
| `prefs.open` | Open Settings | {page?: general\|startup\|project\|composition\|previews\|appearance\|grids\|labels\|type\|import\|export\|audio\|disk\|memory\|video\|3d\|scripting} |
| `prefs.pages` | Settings Pages | {} |
| `prefs.reset` | Reset Settings | {page?: general\|labels\|project\|…} |
| `prefs.set` | Change Setting | {key, value, values?: {key: value}} |

## Команды scopes.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `scopes.analyze` | Video Scopes | {comp?, time?\|frame?, scope?: waveformRgb\|waveformLuma\|waveformYc\|vectorscopeYuv\|vectorscopeHls\|histogram\|paradeRgb\|paradeYuv, standard?: rec601\|rec709\|rec2020, float?, clamp?, size?} |

## Команды script.* (4)

| id | что делает | параметры |
| --- | --- | --- |
| `script.run` | Run Script | {code (JavaScript: app, app.project, CompItem, Layer, Property… like After Effects scripting), name?, console? (Script Console context)} → {ok, result, output, error: {message, line, column} \| null} |
| `script.runTasks` | Run Scheduled Script Tasks | {} → runs the app.scheduleTask tasks that are due (frontends do it every frame) → {ran, output, errors, next (ms until the next task, or null)} |
| `script.settings.get` | Get Script Setting | {section, key} → {have, value} (app.settings.haveSetting / getSetting) |
| `script.settings.save` | Save Script Setting | {section, key, value (text)} → kept in the settings store (app.settings.saveSetting) |

## Команды scriptui.* (9)

| id | что делает | параметры |
| --- | --- | --- |
| `scriptui.click` | Click Script Window Control | {window?: id \| title, widget: id \| "#id" \| properties.name \| text} (buttons, checkboxes, radio buttons, tabs) |
| `scriptui.close` | Close Script Window | {window?, result? (a dialog's show() returns it; default 2 = Cancel)} |
| `scriptui.fileDialog` | Answer Script File Dialog | {id? (from scriptui.fileDialogs; default the only one), host?, paths: [path…] \| null (cancelled)} → the waiting script goes on with the picked files |
| `scriptui.fileDialogs` | Script File Dialogs | {} → [{id, host, kind: open\|save\|folder, prompt, exts, label, any, many, start, shown}]: the file dialogs scripts wait on (File.openDialog, File.saveDialog, Folder.selectDialog…) |
| `scriptui.get` | Script Window Controls | {window?: id \| title} → {id, title, kind, root: {id, type, name, text, value, checked, items, selection, bounds, enabled, draw (onDraw paint list), children…}} |
| `scriptui.list` | List Script Windows | {} → [{window, title, kind: dialog\|palette\|window\|panel, script, modal, size}] |
| `scriptui.mouse` | Mouse Event on Script Window Control | {window?, widget, type: mousedown \| mouseup \| mousemove \| mouseover \| mouseout \| click (default), x?, y? (relative to the control; default its centre), button? (0 left, 1 middle, 2 right), buttons? (held: 1 left, 2 right, 4 middle), detail? (click count), screenX?, screenY?, altKey?, ctrlKey?, metaKey?, shiftKey?} → the script's addEventListener listeners on the control and its containers receive a MouseEvent |
| `scriptui.resize` | Resize Script Window | {window?, size: [width, height] (pixels)} → the window takes the size, lays itself out again and its onResizing / onResize run (a docked ScriptUI panel gets its dock's size) |
| `scriptui.set` | Set Script Window Control | {window?, widget, value: text \| number \| bool \| item index \| item text, changing?: bool (a live update: each keystroke / slider step; fires onChanging only)} (edit text, sliders, checkboxes, lists) → fires onChanging / onChange |

## Команды shortcuts.* (7)

| id | что делает | параметры |
| --- | --- | --- |
| `shortcuts.conflicts` | Keyboard Shortcut Conflicts | {} |
| `shortcuts.export` | Export Keyboard Shortcuts | {preset?, path?} |
| `shortcuts.import` | Import Keyboard Shortcuts | {path? \| preset?: exported document, name?} |
| `shortcuts.list` | List Keyboard Shortcuts | {query?, keys?, assigned?: bool} |
| `shortcuts.preset` | Keyboard Shortcut Preset | {op: select\|new\|duplicate\|delete\|rename, name?, from?, newName?} |
| `shortcuts.reset` | Reset Keyboard Shortcuts | {command?, params?} |
| `shortcuts.set` | Set Keyboard Shortcut | {command, params?, keys: "Cmd+Shift+K" \| [keys] \| null} |

## Команды storage.* (3)

| id | что делает | параметры |
| --- | --- | --- |
| `storage.clear` | Clear Browser Storage | {what: diskCache\|media\|projects\|autoSaves\|all} → {cleared, entries, bytes} |
| `storage.info` | Browser Storage | {} → {available, backend, usage, quota, persisted, files: {count, bytes, media, projects, autoSaves}, diskCache: {enabled, entries, bytes, maxBytes, hits, misses, writes, evictions}} |
| `storage.persist` | Request Persistent Storage | {} → {requested, persisted} |

## Команды templates.* (5)

| id | что делает | параметры |
| --- | --- | --- |
| `templates.create` | New Project from Template | {id (templates.list) \| path (.ectemplate), projectPath? (save the new project there; embedded footage goes to `<stem> Footage/` next to it), footageDir?} → an untitled copy (embedded footage extracted: `footage` lists the files) |
| `templates.delete` | Delete Template | {id: user/<file>} |
| `templates.list` | Project Templates | {thumbnails?: bool} → [{id, name, description, category, builtin, width, height, frameRate, duration, controls, thumbnail? (hex RGB 256×144)}] |
| `templates.saveAs` | Save as Template... (File) | {name, description?, category?, overwrite?: bool (default true), embedFootage?: bool (default true: the footage files go into the template), embedLimitMB? (default 256: footage beyond it stays linked, with a warning)} → {id, path, embedded, embeddedBytes, linked: [{item, name, reason}], warning?} |
| `templates.thumbnail` | Template Thumbnail | {id} → {id, width, height, rgb (hex)} |

## Команды view.* (62)

| id | что делает | параметры |
| --- | --- | --- |
| `view.addGuide` | Add Guide... (View) | {orientation?: vertical\|horizontal, position? (comp px, or percent with percent: true), percent?: bool} |
| `view.addPercentGuide` | Add Percentage Guide... (View) | {orientation?: vertical\|horizontal, position? (percent of the comp)} |
| `view.assign3dShortcut` | Assign Shortcut to 3D View | {slot: F10\|F11\|F12, comp?} |
| `view.channel` | Show Channel | {channel: rgb\|red\|green\|blue\|alpha\|rgbStraight, colorized?, toggle?} |
| `view.channel.alpha` | Show Channel: Alpha | {} |
| `view.channel.blue` | Show Channel: Blue | {} |
| `view.channel.blueColorized` | Show Channel: Blue, Colorized | {} |
| `view.channel.green` | Show Channel: Green | {} |
| `view.channel.greenColorized` | Show Channel: Green, Colorized | {} |
| `view.channel.red` | Show Channel: Red | {} |
| `view.channel.redColorized` | Show Channel: Red, Colorized | {} |
| `view.channel.rgbStraight` | Show Channel: RGB Straight | {} |
| `view.clearGuides` | Clear Guides (View) | {comp?} |
| `view.closeLockedViewer` | Close Locked Viewer | {} |
| `view.convertGuides` | Convert Guides to Percentage (View) | {comp?, to?: percent\|pixels, index?} |
| `view.customRgb` | My Custom RGB... | {name?, red?/green?/blue?/white?: [x, y] (CIE xy), gamma?, srgbCurve?: bool, icc?: path (RGB ICC profile, matrix/TRC or LUT-based A2B0: read when it changes, "" clears; a LUT profile simulates through its tables, `lutProfile` in the reply; typed-in numbers replace it), reload?, from?: a Simulate Output profile to start from, reset?, preserveRgb?, apply?: bool (default true: simulate it)} → the definition (kept in Settings) |
| `view.displayColor` | Viewer Color State | {} → display colour management, output simulation, display profile, locked viewer |
| `view.displayColorManagement` | Use Display Color Management (View) | {value?} |
| `view.exportGuides` | Export Guides... (View) | {path} |
| `view.exposure` | Adjust Exposure | {stops? \| delta?} |
| `view.extendedViewer` | Extended Viewer | {value?} |
| `view.fastPreviewMode` | Fast Previews | {mode: off\|adaptive\|draft\|fastDraft\|wireframe} |
| `view.fastPreviews.adaptive` | Fast Previews: Adaptive Resolution | {} |
| `view.fastPreviews.draft` | Fast Previews: Draft | {} |
| `view.fastPreviews.fastDraft` | Fast Previews: Fast Draft | {} |
| `view.fastPreviews.off` | Fast Previews: Off (Final Quality) | {} |
| `view.fastPreviews.wireframe` | Fast Previews: Wireframe | {} |
| `view.fullScreen` | Enter Full Screen (View) | {} |
| `view.grid` | Show Grid (View) | {value?} |
| `view.guides` | Show Guides (View) | {value?} |
| `view.importGuides` | Import Guides... (View) | {path} |
| `view.layerControls` | Show Layer Controls (View) | {value?} |
| `view.layout` | Switch View Layout | {views: 1\|2\|4} |
| `view.lockGuides` | Lock Guides (View) | {value?} |
| `view.lookAtAll` | Look at All Layers (View) | {comp?} |
| `view.lookAtSelected` | Look at Selected Layers (View) | {comp?, layers?} |
| `view.moveGuide` | Move Guide | {comp?, index, position (comp px), merge?} |
| `view.newViewer` | New Viewer (View) | {} — another Composition viewer of the active comp; the one in use is locked |
| `view.options` | View Options... (View) | {} |
| `view.panelBackground` | Panel Background Color | {color?: black\|darkGray\|mediumGray\|lightGray\|white\|custom\|#hex, pick?: true} |
| `view.removeGuide` | Remove Guide | {comp?, index} |
| `view.res.auto` | Resolution: Auto | {comp?} |
| `view.res.custom` | Custom... (View › Resolution) | {factor?: 1..40 (render every n-th pixel), comp?} |
| `view.res.full` | Full (View › Resolution) | {comp?} |
| `view.res.half` | Half (View › Resolution) | {comp?} |
| `view.res.quarter` | Quarter (View › Resolution) | {comp?} |
| `view.res.third` | Third (View › Resolution) | {comp?} |
| `view.resetExposure` | Reset Exposure | {} |
| `view.rulers` | Show Rulers (View) | {value?} |
| `view.setPaneView` | Set View of Pane | {pane: 0 (main) \| 1 \| 2 \| 3, view: activeCamera\|default\|front\|left\|top\|back\|right\|bottom\|custom1\|custom2\|custom3, comp?} |
| `view.setRegionOfInterest` | Region of Interest | {rect?: [x, y, w, h] \| null} |
| `view.shareViewOptions` | Share View Options (View › Switch View Layout) | {value?} |
| `view.showSnapshot` | Show Snapshot | {value?} |
| `view.simulateOutput` | Simulate Output | {profile: none\|rec709\|ntsc\|pal\|mac18\|srgb\|rec2020\|p3\|linear\|myCustom\|custom, preserveRgb?, space? (custom)} |
| `view.snapToGrid` | Snap to Grid (View) | {value?} |
| `view.snapToGuides` | Snap to Guides (View) | {value?} |
| `view.snapping` | Snapping (View) | {value?} |
| `view.snappingOptions` | Snapping Options | {edgesExtended? (Snap Edges Extended), collapsedFeatures? (Snap to Features in Collapsed Compositions and Text Layers): bool, toggle?: one of those keys} → the options |
| `view.splitLockedViewer` | Split with New Locked Viewer (View) | {comp?, view?: 3D view id} |
| `view.takeSnapshot` | Take Snapshot | {comp?, scale?: 0.05..1} |
| `view.zoomIn` | Zoom In (View) | {} |
| `view.zoomOut` | Zoom Out (View) | {} |

## Команды warp.* (3)

| id | что делает | параметры |
| --- | --- | --- |
| `warp.analyze` | Analyze | {layer?, effect?: uid\|name\|index, wait?: block until done} |
| `warp.cancel` | Cancel | {} |
| `warp.status` | Warp Stabilizer Status | {layer?, effect?} |

## Команды window.* (9)

| id | что делает | параметры |
| --- | --- | --- |
| `window.assignWorkspaceShortcut` | Assign Shortcut to Workspace | {slot: Shift+F10\|Shift+F11\|Shift+F12, workspace?} |
| `window.editWorkspaces` | Edit Workspaces... (Window › Workspace) | {name, rename?: new name, delete?: bool} |
| `window.panel` | Show Panel | {panel: project\|effectControls\|composition\|layer\|timeline\|info\|audio\|preview\|effectsPresets\|properties\|character\|paragraph\|align\|tracker\|wiggler\|smoother\|motionSketch\|paint\|brushes\|renderQueue\|flowchart\|history\|markers\|tools\|lumetriScopes\|footage\|mediaBrowser\|metadata\|progress\|contentAwareFill\|createNullsFromPaths\|vrCompEditor} |
| `window.resetWorkspace` | Reset to Saved Layout (Window › Workspace) | {} |
| `window.restoreScriptPanels` | Restore ScriptUI Panels | {} → reopens the ScriptUI panels open when EffectCraft last quit (frontends call it at launch) → {opened: [name], failed: [{name, error}]} |
| `window.saveWorkspace` | Save Changes to this Workspace (Window › Workspace) | {} |
| `window.saveWorkspaceAs` | Save as New Workspace... (Window › Workspace) | {name} |
| `window.scriptPanel` | ScriptUI Panel | {name (a script in the ScriptUI Panels folder, e.g. `Layer Tools.jsx`, or `Folder/Panel.jsx` in a subfolder)} → opens it as a dockable panel |
| `window.workspace` | Workspace | {name: Default\|Standard\|Small Screen\|Animation\|Effects\|Motion Tracking\|Paint\|Text\|Minimal\|All Panels} |

<!-- generated:end -->
