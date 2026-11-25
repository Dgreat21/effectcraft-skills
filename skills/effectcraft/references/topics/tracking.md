# Трекинг и стабилизация

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды track.* (22)](#команды-track-22)
<!-- toc:end -->

## Как работать

- **TRK-01.** Сначала убедись, что видео декодируется (footage.md, FTG-02).
- **TRK-02.** Перед `track.new` явно выдели слой-источник (`layer.select`).
- **TRK-03.** Порядок: `track.new {layer, kind, target}` → `track.setPoint` (точки с 1) → `track.options` → `track.analyze {start, end, wait: true}` → `track.status` → `track.apply` → сохранить → открыть заново.
- **TRK-04.** `frames` в ответе `track.analyze` — план, а не результат. Считай ключи в `track.status` (`tracker.points[].keys`); 0 ключей — провал.
- **TRK-05.** После `track.apply` проверь `get` позиции цели в нескольких моментах.
- **TRK-06.** Стабилизация кадра и привязка графики — разные задачи. Обе сразу делай только по просьбе.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды track.* (22)

| id | что делает | параметры |
| --- | --- | --- |
| `track.analyze` | Analyze | {layer?, tracker?, direction?: forward\|backward\|frameForward\|frameBackward, start? (s), end? (s), wait?: block until done} |
| `track.apply` | Apply | {layer?, tracker?, dimensions?: xy\|x\|y} |
| `track.camera` | Track Camera (Animation) | {layer?, shotType?: fixed\|variable\|specify, aov?: degrees, solveMethod?: auto\|typical\|flat\|tripod, detailed?, lensDistortion?: solve k1/k2, undistort?: render undistorted, wait?} |
| `track.delete` | Delete Tracker | {layer?, tracker?} |
| `track.editTargetDialog` | Edit Target... | {} |
| `track.extractFaceMeasurements` | Extract & Copy Face Measurements | {layer?} → keys a Face Measurements effect from the layer's Face Track Points (one key per tracked frame) and copies those keys |
| `track.mask` | Track Mask (Animation) | {layer?, mask?: uid\|index\|name, method?: position\|positionScale\|positionScaleRotation\|positionScaleRotationSkew\|perspective\|faceOutline\|faceDetailed, direction?: forward\|backward\|frameForward\|frameBackward, start? (s), end? (s), wait?: block until done} |
| `track.maskMethod` | Mask Tracking Method | {method: position\|positionScale\|positionScaleRotation\|positionScaleRotationSkew\|perspective\|faceOutline\|faceDetailed} |
| `track.motion` | Track Motion (Animation) | {layer?} |
| `track.new` | New Tracker | {layer?, kind?: transform\|stabilize\|affine\|perspective\|raw, position?, rotation?, scale?, target?: layer} |
| `track.options` | Motion Tracker Options | {layer?, tracker?, name?, channel?: rgb\|luminance\|saturation, blur? (px, 0 = off), enhance?, subpixel?, adaptEveryFrame?, threshold? (%), action?: continue\|stop\|extrapolate\|adapt, trackShape?} |
| `track.optionsDialog` | Options... | {} |
| `track.property` | Track this Property (Animation) | {layer?, source?: layer} |
| `track.reset` | Reset | {layer?, tracker?} |
| `track.select` | Current Track | {layer?, tracker?: uid\|name\|#n} |
| `track.setPoint` | Move Track Point | {layer?, tracker?, point: n (1-based), center?: [x,y], featureSize?: [w,h], searchOffset?: [x,y], searchSize?: [w,h], attachOffset?: [x,y], move?: [dx,dy], time? (s)} |
| `track.setTarget` | Edit Target | {layer?, tracker?, target: layer\|null} |
| `track.setType` | Track Type | {layer?, tracker?, kind?: transform\|stabilize\|affine\|perspective\|raw, position?, rotation?, scale?} |
| `track.stabilize` | Stabilize Motion (Animation) | {layer?} |
| `track.status` | Tracker Status | {layer?, tracker?} |
| `track.stop` | Stop Analysis | {} |
| `track.warpStabilizer` | Warp Stabilizer VFX (Animation) | {layer?, wait?} |

<!-- generated:end -->
