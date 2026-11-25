# Проект и файлы

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды file.* (62)](#команды-file-62)
- [Команды item.* (1)](#команды-item-1)
- [Команды project.* (13)](#команды-project-13)
<!-- toc:end -->

## Как работать

- **PRJ-01.** Открывай `--project F.ecproj`, сохраняй в новый файл `--save-as NEW.ecproj`. `--save` перезаписывает открытый файл — только для своего промежуточного.
- **PRJ-02.** Каждый вызов CLI — отдельный процесс с чистым состоянием: ID, выделение и активная композиция между вызовами не живут. Шаги, которым нужны возвращённые ID, держи в одном `run`.
- **PRJ-03.** После сохранения открой проект новым процессом: `ec.py -- info --project F --json`. У всех `project.items[]` должно быть `missing: false`.
- **PRJ-04.** Перенос проекта с материалами — команда сбора файлов (`ec.py search collect`), потом `ec.py verify` уже в новом месте.
- **PRJ-05.** Обмен с After Effects (`file.importAep`, `file.exportAep`) не бывает без потерь: результат сверяй кадрами с оригиналом.
- **PRJ-06.** Скрипты в духе After Effects: `ec.py -- script FILE.jsx [F.ecproj]` или `--eval КОД` (объекты `app.project`, композиции, слои). Запускай только свои или утверждённые скрипты (EC-09).

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды file.* (62)

| id | что делает | параметры |
| --- | --- | --- |
| `file.applyInterpretation` | Apply Interpretation (File › Interpret Footage) | {items?\|item?} |
| `file.autoSave` | Auto-Save Now | {} |
| `file.clearRecent` | Clear Recent Projects (File › Open Recent) | {} |
| `file.clearRecentFootage` | Clear Recent Footage (File › Import Recent Footage) | {} |
| `file.close` | Close (File) | {comp?} |
| `file.closeProject` | Close Project (File) | {} |
| `file.collectFiles` | Collect Files... (File › Dependencies) | {folder} |
| `file.consolidateFootage` | Consolidate All Footage (File › Dependencies) | {} |
| `file.createProxy` | Create Proxy | {kind: still\|movie, comp?\|item?, path?\|output? (template), resolution? (default 0.5)} |
| `file.cycleBitDepth` | Cycle Project Bit Depth | {} |
| `file.executeFile` | Execute File | {path, confirmed?} |
| `file.exportAep` | Adobe After Effects Project... (File › Export) | {path (.aep), allowLosses?: bool (export although parts cannot be exported), dryRun?: bool (only return the report)} |
| `file.findMissing` | Find Missing | {what: footage\|effects\|fonts} |
| `file.import` | File... (File › Import) | {paths: [string] (files or folders), sequence?: bool (the Sequence checkbox: true imports numbered stills of one run as one image sequence, one picked file bringing its whole run and several picked files that range; default false: picked or dropped files import as stills, as in After Effects; folders' runs import as sequences; false imports stills and a folder's files individually), alphabetical?: bool (Force Alphabetical Order: every image of that type in the folder, by name), frameRate?: fps (image sequences; default Settings ▸ Import ▸ Sequence Footage), importAs?: footage\|composition\|compositionLayerSizes (Photoshop, PDF, Illustrator and EPS files), layer?: name\|index (footage of one Photoshop layer), page?: number from 1 (PDF / Illustrator page), drag?: bool (dropped files: Settings ▸ Import ▸ Default Drag Import As; files import as stills unless sequence), addToComp?: bool (also add them to the active comp, at time?, index?, position? as in layer.addItem), newComp?: bool (make one new composition of the footage and solids imported, as file.newCompFromSelection with single; a layered file imported as a composition is that composition and gets no other; takes precedence over addToComp), background?: bool (probe the files in a background job, jobs.list / jobs.wait; returns {job})} |
| `file.importAep` | Adobe After Effects Project... (File › Import) | {path (.aep or .aepx), allowLosses?: bool (import although parts cannot be imported), dryRun?: bool (only return the report), applySettings?: bool (take over the file's project settings; default: when the project has no compositions)} |
| `file.importLottie` | Lottie... (File › Import) | {path (.json or .lottie)} |
| `file.importMultiple` | Multiple Files... (File › Import) | {paths: [string]} |
| `file.importPlaceholder` | Placeholder... (File › Import) | {name?, width?, height?, frameRate?, duration? (s)} |
| `file.importProject` | EffectCraft Project... (File › Import) | {path (.ecproj or .ecprojx)} — merges the project into a folder named after the file; returns {folder, items, comps, rootComps, primaryComp (the only root comp, else null), missingMedia, warnings} |
| `file.importRecent` | Import Recent Footage | {index? \| path?} |
| `file.importSolid` | Solid... (File › Import) | {name?, color?, width?, height?} |
| `file.importTimeline` | Adobe Premiere Pro Project... (File › Import) | {path (.xml Final Cut Pro XML from Premiere Pro or .fcpxml .otio .edl .aaf .omf), format?: auto\|xml\|fcpxml\|otio\|edl\|aaf\|omf, edlFrameRate?: number} |
| `file.importVanishingPoint` | Vanishing Point (.vpe)... (File › Import) | {} (always disabled: undocumented format) |
| `file.incrementAndSave` | Increment and Save (File) | {} |
| `file.installScript` | Install Script File... (File › Scripts) | {path (.jsx / .js)} → copies it to the Scripts folder; it appears in File ▸ Scripts |
| `file.installScriptUIPanel` | Install ScriptUI Panel... (File › Scripts) | {path (.jsx / .js)} → copies it to the ScriptUI Panels folder; it appears in the Window menu |
| `file.interpretFootage` | Main... (File › Interpret Footage) | {items?\|item?, frameRate?: fps\|"file", alpha?: straight\|premultiplied\|ignore\|guess, guessAlpha?, matteColor?\|premulColor?, invertAlpha?, loop?, pixelAspect?, fields?: off\|upper\|lower, colorProfile?: srgb\|rec709\|rec2020\|p3\|auto, linearLight?, preserveRgb? (the file's values unconverted), overrideStart?: bool (false: Use Source File Timecode), startTimecode?: timecode\|frame (Override Start), logConversion? (Cineon Settings of DPX and Cineon files), cineonUnits?: 10bit\|8bit\|float, convertedBlack?, convertedWhite?, pointUnits?: 10bit\|8bit\|float (the units of convertedBlack and convertedWhite; default cineonUnits, else the footage's Units), tenBitBlack?, tenBitWhite? (0..1023), currentGamma? (0.1..10), highlightRolloff? (0..100)} |
| `file.interpretProxy` | Proxy... (File › Interpret Footage) | {items?\|item?, alpha?, guessAlpha?, matteColor?\|premulColor?, invertAlpha?, frameRate?, loop?, pixelAspect?, fields?, colorProfile?, linearLight?, preserveRgb?, overrideStart?, startTimecode? (as file.interpretFootage), logConversion?, cineonUnits?, convertedBlack?, convertedWhite?, pointUnits?, tenBitBlack?, tenBitWhite?, currentGamma?, highlightRolloff? (Cineon Settings of DPX and Cineon proxies)} |
| `file.newCompFromSelection` | New Comp from Selection... (File) | {duration? (s, for stills), single?: bool (one comp for all), dimensionsFrom?: index, sequence?: bool, overlap?: bool, overlapDuration? (s), transition?: off\|dissolveFront\|crossDissolve, addToRenderQueue?: bool} → {comps} |
| `file.newFromTemplate` | New Project from Template... (File › New) | {} → the Home screen's Templates tab |
| `file.newProject` | New Project (File › New) | {} |
| `file.open` | Open Project... (File) | {path} |
| `file.openDemoProject` | Open Demo Project (Help) | {} |
| `file.openRecent` | Open Recent | {index? \| path?} |
| `file.projectSettings` | Project Settings... (File) | {bitDepth?: 8\|16\|32, colorEngine?: adobe\|ocio, workingSpace?: none\|srgb\|rec709\|rec2020\|p3\|acescg\|aces2065, workingGamma?: 2.2\|2.4 (with no working space), linearize?, blendLinear?, hdr?: clip\|compand\|toneMap, outputSpace?: srgb\|rec709\|rec2020\|p3\|rec2100pq\|rec2100hlg, renderer?: gpu\|software, timeDisplay?: timecode\|frames\|feet35\|feet16, frameStart?: 0\|1 (Frame Count: Start at 0 / Start at 1)} |
| `file.recoveryInfo` | Auto-Save Status | {} |
| `file.reduceProject` | Reduce Project (File › Dependencies) | {} (keeps the selected comps and what they use) |
| `file.reloadFootage` | Reload Footage (File) | {items?\|item?} |
| `file.rememberInterpretation` | Remember Interpretation (File › Interpret Footage) | {item?} |
| `file.removeUnusedFootage` | Remove Unused Footage (File › Dependencies) | {} |
| `file.replaceFootage` | File... (File › Replace Footage) | {path, item?, sequence?: bool (a numbered still brings its image sequence; default: the item keeps its kind, so a still stays a still and a sequence stays a sequence), alphabetical?: bool} |
| `file.replaceWithLayeredComp` | With Layered Comp (File › Replace Footage) | {item?} |
| `file.replaceWithPlaceholder` | Placeholder... (File › Replace Footage) | {item?, width?, height?, frameRate?, duration?} |
| `file.replaceWithPrecomp` | Replace with Precomposition | {item?} |
| `file.replaceWithSolid` | Solid... (File › Replace Footage) | {item?, color?, width?, height?} |
| `file.revealInFinder` | Reveal in Finder (File) | {item?} |
| `file.revert` | Revert (File) | {} |
| `file.runScript` | Run Script File... (File › Scripts) | {path (.jsx/.js JavaScript, or a .jsonl/.json command script) \| name (an installed or sample script, see file.scripts.list) \| recent: index (File ▸ Scripts ▸ Recent Script Files, 0 = the most recent) \| steps: [{command, params}]} |
| `file.runShutdownScripts` | Run Shutdown Scripts | {} → closes the project, then runs the scripts in Scripts/Shutdown in alphabetical order (frontends call it as the app quits; their modal dialogs close as if canceled) → {ran: [name], waiting: [name], failed: [{name, error}]} |
| `file.runStartupScripts` | Run Startup Scripts | {} → runs the scripts in Scripts/Startup in alphabetical order (frontends call it at launch) → {ran: [name], waiting: [name] (in a modal dialog), failed: [{name, error}]} |
| `file.save` | Save (File) | {path?} |
| `file.saveAs` | Save As... (File › Save As) | {path} |
| `file.saveCopy` | Save a Copy... (File › Save As) | {path} |
| `file.saveCopyAsXml` | Save a Copy As XML... (File › Save As) | {path: .ecprojx} |
| `file.scripts.list` | List Scripts | {} → [{name (`Folder/File.jsx` in a subfolder), panel, source: installed\|sample\|extension}] |
| `file.setProxy` | File... (File › Set Proxy) | {path, items?\|item?} |
| `file.setProxyNone` | None (File › Set Proxy) | {items?\|item?} |
| `file.timelineFormats` | Timeline Interchange Formats | {} |
| `file.uninstallScript` | Uninstall Script | {name (a script at the top of a Scripts folder, not `Folder/File.jsx`)} |
| `file.useProxy` | Use Proxy | {items?\|item?, on?} |
| `file.watchFolder` | Watch Folder... (File) | {folder, stop?: bool} → watches the folder for .ecproj files with queued renders, renders them and writes `<project>.status.json` |
| `file.watchFolder.poll` | Poll Watch Folder | {folder? (default: the watched one)} → renders new projects now: {watching, rendered: [{project, state: done\|failed, items: [{comp, status, output}]}]} |

## Команды item.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `item.metadata` | Metadata | {item?: id\|name} |

## Команды project.* (13)

| id | что делает | параметры |
| --- | --- | --- |
| `project.delete` | Delete Project Items | {items?: [id\|name] (default: selected)} (folders with their contents; layers using the items go too) |
| `project.deleteWithoutConfirmation` | Delete Project Items Without Confirmation | {} — the Project panel's selection, with the layers that use it; one undo step |
| `project.duplicate` | Duplicate Project Items | {items?: [id\|name] (default: selected)} → {items} |
| `project.move` | Move to Folder | {items?: [id\|name] (default: selected), folder: id\|name\|null (root)} |
| `project.newFolder` | New Folder (File › New) | {name?, parent?, items?: [id\|name] (moved into it)} |
| `project.rename` | Rename Item | {item?: id\|name (default: selected), name} |
| `project.select` | Select Project Items | {items: [id\|name], add?} |
| `project.setComment` | Item Comment | {items?, comment} |
| `project.setLabel` | Item Label | {items?, label: name\|index} |
| `project.setProjectComment` | Project Comment | {comment} |
| `project.summary` | Project Summary | {} |
| `project.usage` | Project Item Usage | {items?: [id\|name] (default: selected)} → {items, layers, comps} that deleting them removes |
| `project.usedIn` | Project Item Used In | {item?: id\|name (default: selected)} → {item, count, comps: [{id, name, layers}]} |

<!-- generated:end -->
