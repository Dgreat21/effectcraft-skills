# Рендер и экспорт

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды file.* (3)](#команды-file-3)
- [Команды render.* (4)](#команды-render-4)
- [Команды renderQueue.* (20)](#команды-renderqueue-20)
<!-- toc:end -->

## Как работать

- **OUT-01.** Превью — `render-frame --time S --max-side N` (`--transparent` для альфы). Финал — `render`.
- **OUT-02.** Альфа: `render --format png|prores|exr|tiff --channels rgba`. H.264 и HEVC альфы не несут. Проверка — `ec.py verify --alpha`.
- **OUT-03.** PNG-секвенция пишется как `имя_00000.png`. `--start 0 --end 1` при 25 fps дают 25 кадров. Проверка — `ec.py verify --sequence 'dir/имя_*.png' --frames N`.
- **OUT-04.** Сначала короткий кусок в четверть размера (`--resolution quarter`), потом полный рендер.
- **OUT-05.** Видео скрипт не декодирует: посмотри его глазами или проверь кадры из проекта.
- **OUT-06.** Проверка вывода: размер, fps, длительность, звук и альфа сверяются с заданием, тестовые слои выключены. Рендер упал — сохрани проект и текст ошибки, вслепую не перезапускай.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды file.* (3)

| id | что делает | параметры |
| --- | --- | --- |
| `file.checkOutput` | Check Output File | {path} → {path, blocked, source?: footage\|proxy\|project, reason?}: whether an export may be written to path (it may not replace a file the project reads) |
| `file.exportLottie` | Lottie JSON... (File › Export) | {comp?, path (.json or .lottie), includeExpressions?: bool, textAsShapes?: bool} |
| `file.exportTimeline` | Adobe Premiere Pro Project... (File › Export) | {comp?, path (Final Cut Pro XML .xml for Premiere Pro or .fcpxml .otio .edl .aaf .omf), format?: xml\|fcpxml\|otio\|edl\|aaf\|omf, prerender?: none\|unsupported\|all, precomps?: nest\|prerender, background?: bool (pre-render and write as a job, jobs.list / jobs.wait; returns {job})} |

## Команды render.* (4)

| id | что делает | параметры |
| --- | --- | --- |
| `render.addOutputModule` | Add Output Module (Composition) | {item?\|index? (default: the last item), format?, output?, channels?, quality?, bitrate?, proresProfile?, exrCompression?, exrBitDepth?, audio?} |
| `render.backend` | Video Rendering and Effects | {backend?: gpu\|cpu} |
| `render.preRender` | Pre-render... (Composition) | {comp?, output?: path\|template, format?} |
| `render.saveCurrentPreview` | Save Current Preview... (Composition) | {comp?, path} |

## Команды renderQueue.* (20)

| id | что делает | параметры |
| --- | --- | --- |
| `renderQueue.add` | Add to Render Queue (Composition) | {comp?: id\|name, template?: Render Settings template, format?: h264\|hevc\|av1\|prores\|uncompressed\|webm\|png\|jpeg\|tiff\|exr\|tga\|gif\|wav\|aiff, output?: path\|template, log?: errorsOnly\|plusSettings\|plusPerFrameInfo, quality?: best\|draft\|1-100 (jpeg, webm), resolution?: full\|half\|third\|quarter\|scale, proxyUse?, effects?, solo?, guideLayers?, colorDepth?, frameBlending?, fieldRender?, pulldown?, motionBlur?, timeSpan?: workArea\|comp\|custom, start?: s, end?: s, duration?: s, frameRate?: fps\|null, skipExisting?: bool, storageOverflow?: bool, channels?: rgb\|rgba\|alpha, color?, bitrate?: kbps, webmBitrate?, keyframeInterval?, proresProfile?, exrCompression?, exrBitDepth?, profile?, level?, rateControl?, webmCodec?, audioBitrate?, opusApplication?, crop?, resize?, includeProjectLink?, audio?: auto\|on\|off, sampleRate?, audioChannels?, audioFormat?, loop?: bool (values as in setRenderSettings / setOutputModule)} |
| `renderQueue.applyTemplate` | Apply Template | {item?\|index?, renderSettings?: template name, outputModule?: template name, module?: n} |
| `renderQueue.deleteTemplate` | Delete Template | {kind: renderSettings\|outputModule, name} |
| `renderQueue.duplicate` | Duplicate Render Item | {item?\|index?} |
| `renderQueue.formats` | Output Formats | {} |
| `renderQueue.list` | Render Queue Items | {} |
| `renderQueue.move` | Move in Render Queue | {item?\|index?, to: n (1-based)} |
| `renderQueue.remove` | Remove from Render Queue | {item?: id, index?: n} |
| `renderQueue.render` | Render | {wait?: bool (default true; the UI renders in the background)} |
| `renderQueue.saveTemplate` | Save Template... | {kind: renderSettings\|outputModule, name, item?\|index? (save from this item), from?: template to copy, module?, params?: {setRenderSettings / setOutputModule keys}} |
| `renderQueue.setLog` | Render Queue: Log | {item?\|index?, log: errorsOnly\|plusSettings\|plusPerFrameInfo} |
| `renderQueue.setNotify` | Notify When Done | {notify?: bool (toggles)} |
| `renderQueue.setOutput` | Output To... | {item?\|index?, module?: n, path: file path or template like [compName].[fileExtension]} |
| `renderQueue.setOutputModule` | Output Module Settings... | {item?\|index?, module?: n (1 = first), template?: name, format?: h264\|hevc\|av1\|prores\|uncompressed\|webm\|png\|jpeg\|tiff\|exr\|tga\|gif\|wav\|aiff, channels?: rgb\|rgba\|alpha, color?: straight\|premultiplied, quality?: 1-100, bitrate?: kbps, webmBitrate?: bool, keyframeInterval?: frames (0 = auto), proresProfile?: proxy\|lt\|standard\|hq\|4444\|4444xq, exrCompression?: none\|rle\|zips\|zip\|piz\|pxr24\|b44\|b44a\|dwaa\|dwab (OpenEXR, scan lines; default zip; lossy: pxr24 on float, b44/b44a on half, dwaa/dwab), exrBitDepth?: half\|float (OpenEXR; default float), profile?: main\|main10 (HEVC/AV1), level?: auto\|4.1, rateControl?: bitrate\|quality, webmCodec?: vp9\|av1, audioBitrate?: Opus kbps, opusApplication?: audio\|voice, crop?: bool\|{useRoi?, roi?, top?, left?, bottom?, right?}, cropTop?, cropLeft?, cropBottom?, cropRight?, resize?: bool\|{preset?, width?, height?, lockAspect?, quality?: low\|high}, resizeWidth?, resizeHeight?, postRenderAction?: none\|import\|importAndReplace\|setProxy, includeProjectLink?: bool, audio?: auto\|on\|off, sampleRate?, audioChannels?: mono\|stereo, audioFormat?: 16\|24\|32, loop?: bool, output?} |
| `renderQueue.setOverflowFolders` | Storage Overflow Folders | {folders: [path, …] (used in order when the output volume is full)} |
| `renderQueue.setRender` | Render Queue: Render Checkbox | {item?\|index?, render?: bool (toggles)} |
| `renderQueue.setRenderSettings` | Render Settings... | {item?\|index?, template?: name, quality?: best\|draft, resolution?: full\|half\|third\|quarter\|scale, proxyUse?: current\|all\|comp\|none, effects?: current\|allOn\|allOff, solo?: current\|allOff, guideLayers?: current\|allOff, colorDepth?: current\|8\|16\|32, frameBlending?: current\|onForChecked\|offForAll, fieldRender?: off\|upper\|lower, pulldown?: off\|WSSWW\|SSWWW\|SWWWS\|WWWSS\|WWSSW, motionBlur?: bool\|current\|onForChecked\|offForAll, timeSpan?: workArea\|comp\|custom, start?: s, end?: s, duration?: s, frameRate?: fps\|null, skipExisting?: bool, storageOverflow?: bool} |
| `renderQueue.setTemplateDefault` | Set Template Default | {kind: renderSettings\|outputModule, slot: movie\|still\|preRender\|movieProxy\|stillProxy, name} |
| `renderQueue.stop` | Stop Rendering | {} |
| `renderQueue.templates` | Render Templates | {} |

<!-- generated:end -->
