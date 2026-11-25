# Композиции и время

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды comp.* (33)](#команды-comp-33)
- [Команды time.* (17)](#команды-time-17)
<!-- toc:end -->

## Как работать

- **CMP-01.** `comp.new`: явно задавай `width`, `height`, `frameRate`, `duration` (секунды).
- **CMP-02.** Последний кадр — `duration − 1/fps`: при 25 fps и 4 с это 3.96. Время 4.0 уже за концом.
- **CMP-03.** 3D-примитивы рендерятся только с `renderer: advanced3D` (см. camera.md, CAM-01).
- **CMP-04.** Рабочая область задаёт диапазон превью и `render --work-area`. Превью и финал считай по одному диапазону.
- **CMP-05.** Во вложенных композициях проверяй время и размер и внутри, и снаружи.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды comp.* (33)

| id | что делает | параметры |
| --- | --- | --- |
| `comp.activateRecent` | Activate Most Recent Composition in Hierarchy | {comp?} |
| `comp.addMarker` | Add Marker | {time?, comment?} |
| `comp.close` | Close Composition | {comp?} |
| `comp.copyFrame` | Copy Frame to Clipboard (Composition) | {comp?, time?, scale?} |
| `comp.cropToLayerBounds` | Crop Comp to Selected Layer(s) Bounds (Composition) | {layers?} |
| `comp.cropToRegionOfInterest` | Crop Comp to Region of Interest (Composition) | {comp?} |
| `comp.deleteAllMarkers` | Delete All Markers | {comp?} |
| `comp.deletePreset` | Delete Composition Preset | {name} |
| `comp.flowchart` | Composition Flowchart (Composition) | {} |
| `comp.info` | Composition Info | {comp?} |
| `comp.miniFlowchart` | Composition Mini-Flowchart (Composition) | {} |
| `comp.new` | New Composition... (Composition) | {name?, width?, height?, frameRate?, duration? (s), startTime? (s) \| startTimecode?, background? [r,g,b]\|#hex, pixelAspect?, shutterAngle?, shutterPhase?, motionBlurSamples?, adaptiveSampleLimit? (16–256), preserveFrameRate?: bool, preserveResolution?: bool, renderer?: classic3D\|advanced3D, anchor?, open?} |
| `comp.open` | Open Composition | {comp: id\|name} |
| `comp.openInEssentialGraphics` | Open in Essential Graphics (Composition) | {comp?} → makes it the Essential Graphics panel's Primary composition and shows the panel |
| `comp.presets` | Composition Presets | {} |
| `comp.renderer` | Renderer | {renderer?: advanced3d\|classic3d (omit to read), value?} |
| `comp.responsiveTime` | Responsive Design — Time | {op: intro\|outro\|workArea} |
| `comp.revealInProject` | Reveal Composition in Project (Layer › Reveal) | {comp?} |
| `comp.saveFrameAs` | File... (Composition › Save Frame As) | {path (.png; with queue: an output path or template), time?, scale?, queue?: bool (add a Render Queue item from the Frame Default templates instead of writing now), transparent?: bool (default true)} |
| `comp.saveFrameAsExr` | ProEXR... (Composition › Save Frame As) | {path (.exr), comp?, time?, scale?} → a multi-layer OpenEXR: composite R,G,B,A + `<layer>.R/G/B/A` per layer (linear, premultiplied) |
| `comp.saveFrameAsPsd` | Photoshop Layers... (Composition › Save Frame As) | {path (.psd), comp?, time?, scale?} → a layered PSD: one layer per visible comp layer (blend mode, opacity) + the merged frame |
| `comp.savePreset` | Save Composition Preset | {name, width, height, pixelAspect, frameRate} (replaces a saved preset with the same name) |
| `comp.scale` | Scale Composition | {comp?, factor? (2 = twice the size) \| width? \| height? (the other side keeps the aspect ratio)} |
| `comp.setPosterTime` | Set Poster Time (Composition) | {} |
| `comp.setSwitch` | Composition Switch | {switch: hideShy\|motionBlur\|frameBlending\|draft3d, value?} |
| `comp.settings` | Composition Settings... (Composition) | {comp?, name?, width?, height?, anchor? 0-8 (resize anchor, 4 = center), frameRate?, duration?, startTime? (s) \| startTimecode?, background?, shutterAngle?, shutterPhase?, motionBlurSamples?, adaptiveSampleLimit? (16–256), preserveFrameRate?: bool (nested or in the render queue it shows only its own frames), preserveResolution?: bool (nested, it renders at full size), pixelAspect?, renderer?: classic3D\|advanced3D} |
| `comp.trimToWorkArea` | Trim Comp to Work Area (Composition) | {comp?} |
| `comp.vr.createEnvironment` | Create VR Environment... (Composition › VR) | {comp?, size?: face pixels (1024), position?: [x,y,z]} |
| `comp.vr.environments` | VR Environments | {} → [{output, name, cubeMap, faces: [{face, comp, camera}], view: [x, y, z]}] |
| `comp.vr.extractCubemap` | Extract Cubemap... (Composition › VR) | {comp?, faceSize?} |
| `comp.vr.setView` | VR View Orientation | {comp? (an environment's output / cube map / face comp), orientation?: [x, y, z] degrees, pan?, tilt?, roll?} → turns the six face cameras together |
| `comp.workArea` | Set Work Area | {start?, end?, set?: begin\|end (at CTI)} |
| `comp.workAreaToSelection` | Set Work Area to Selected Layers | {comp?, layers? (default the selected layers; the whole composition with none)} |

## Команды time.* (17)

| id | что делает | параметры |
| --- | --- | --- |
| `time.back10` | Back 10 Frames | {} |
| `time.end` | Go to End | {} |
| `time.forward10` | Forward 10 Frames | {} |
| `time.go` | Go To | {to: start\|end\|workStart\|workEnd\|layerIn\|layerOut\|nextInOut\|prevInOut\|nextKey\|prevKey, prop?: uid, visible?: [{layer, prop}]} |
| `time.layerIn` | Go to Layer In Point | {} |
| `time.layerOut` | Go to Layer Out Point | {} |
| `time.nextFrame` | Next Frame | {} |
| `time.nextInOut` | Go to Next In or Out Point | {} |
| `time.nextKey` | Go to Next Keyframe or Marker | {visible?: [{layer, prop}] (only these properties' keys, as the Timeline shows them)} |
| `time.previousFrame` | Previous Frame | {} |
| `time.previousInOut` | Go to Previous In or Out Point | {} |
| `time.previousKey` | Go to Previous Keyframe or Marker | {visible?: [{layer, prop}]} |
| `time.set` | Go to Time... (View) | {time? (s) \| frame? \| timecode?} |
| `time.start` | Go to Start | {} |
| `time.step` | Step Frames | {frames} |
| `time.workAreaEnd` | Go to Work Area End | {} |
| `time.workAreaStart` | Go to Work Area Start | {} |

<!-- generated:end -->
