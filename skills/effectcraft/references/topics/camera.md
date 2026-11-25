# Камера, свет, 3D

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды camera.* (20)](#команды-camera-20)
- [Команды layer.* (6)](#команды-layer-6)
- [Команды light.* (3)](#команды-light-3)
- [Команды material.* (4)](#команды-material-4)
- [Команды view.* (16)](#команды-view-16)
<!-- toc:end -->

## Как работать

- **CAM-01.** 3D-примитивы рендерятся только при `renderer: advanced3D`. 2D-слою в 3D-сцене нужен переключатель 3D (`layer.setSwitch`).
- **CAM-02.** У двухузловой камеры (twoNode) `camera.dolly` двигает и позицию, и точку интереса — проверяй обе.
- **CAM-03.** Виды `view.3d.*` — состояние сессии, не проекта. В проект попадает только камера.
- **CAM-04.** Фокус: `camera.linkFocus*` сохраняет выражение, `camera.setFocusToLayer` — текущее значение. Размытие видно только при включённой глубине резкости.
- **CAM-05.** Камера по видео: `track.camera` → `camera.analyze` → `camera.solveStatus` → `camera.points`. Без решения точки не выдумывай.
- **CAM-06.** Тени: `layer.castsShadows` и свет, который их отбрасывает. Проверяй кадром.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды camera.* (20)

| id | что делает | параметры |
| --- | --- | --- |
| `camera.analyze` | Analyze | {layer?, effect?: uid\|name\|index, wait?: block until done} |
| `camera.cancel` | Cancel | {} |
| `camera.create` | Create Camera | {layer?, effect?} |
| `camera.createFromSolve` | Create from Camera Solve | {kind: text\|solid\|null\|shadowCatcher\|camera, points?: [id] (default: selected), target?: {center, normal, size?} (comp world), multiple?, layer?, effect?} |
| `camera.deletePoints` | Delete Selected Points | {points?: [id] (default: selected), layer?, effect?, wait?} |
| `camera.dolly` | Dolly Camera | {amount (px, + = forward), layer?, merge?} |
| `camera.exportBlender` | Export Scene to Blender... | {path: .py, comp?, layer?, effect?, sensorWidth?: mm (default 36), unitScale?: Blender units per comp pixel (default 0.01), startFrame?: positive integer (default 1), includePoints?: true} |
| `camera.fromModel` | Create Cameras from 3D Model (Layer › Camera) | {comp?, layers?: 3D model layers (default selected)} |
| `camera.fromView` | Create Camera from 3D View (Layer › Camera) | {comp?} |
| `camera.linkFocusToLayer` | Link Focus Distance to Layer (Layer › Camera) | {comp?, camera?, layer?} |
| `camera.linkFocusToPoi` | Link Focus Distance to Point of Interest (Layer › Camera) | {comp?, camera?} |
| `camera.orbit` | Orbit Camera | {yaw\|dx deg, pitch\|dy deg, layer?, merge?} — current 3D view (camera layer in Active Camera) |
| `camera.orbitNull` | Create Orbit Null (Layer › Camera) | {comp?, layer?: camera (default selected/active)} |
| `camera.pan` | Pan Camera | {dx, dy (comp px), layer?, merge?} |
| `camera.points` | 3D Camera Tracker Points | {layer?, effect?, time?: comp seconds} → visible solved points |
| `camera.selectPoints` | Select Track Points | {points: [id], add?, toggle?} |
| `camera.setFocusToLayer` | Set Focus Distance to Layer (Layer › Camera) | {comp?, camera?, layer?} |
| `camera.setGroundPlane` | Set Ground Plane and Origin | {points?: [id] (default: selected), layer?, effect?} |
| `camera.solveStatus` | 3D Camera Tracker Status | {layer?, effect?} |
| `camera.stereoRig` | Create Stereo 3D Rig (Layer › Camera) | {comp?, configuration?: stereoPair\|centerRight\|centerLeft, sceneDepth? (% of comp width, default 3), convergence?: bool, convergenceOf?: poi\|zoom, zOffset?, view3d?: 3D Glasses view index (default 5 Balanced Colored Red Blue)} |

## Команды layer.* (6)

| id | что делает | параметры |
| --- | --- | --- |
| `layer.cameraSettings` | Camera Settings... (Layer › Camera) | {layer?, name?, type?, preset?, zoom?, focalLength?, angleOfView?, dof?, focusDistance?, aperture?, fStop?, blurLevel?, position?, poi?} |
| `layer.castsShadows` | Casts Shadows | {layers?, value?} |
| `layer.new3dPrimitive` | 3D Primitive | {kind: cube\|sphere\|plane\|torus\|cone\|cylinder, name?, width?, height?, depth?, radius?, tubeRadius?, segments?, rings?, position? [x,y,z], baseColor?, metallic?, roughness?, emissive?, castsShadows?, acceptsShadows?, acceptsLights?}; switches a Classic 3D comp to Advanced 3D |
| `layer.newCamera` | Camera... (Layer › New) | {name?, type?: oneNode\|twoNode (default twoNode), preset?: 15mm\|20mm\|24mm\|28mm\|35mm\|50mm\|80mm\|135mm\|200mm, zoom?, focalLength? mm, angleOfView? deg, dof?, focusDistance?, aperture?, fStop?, blurLevel?, lockToZoom?, position? [x,y,z], poi? [x,y,z]} |
| `layer.newLight` | Light... (Layer › New) | {kind?: Parallel\|Spot\|Point\|Ambient\|Environment (default Spot; Environment lights and reflects from an equirectangular image layer: prop.set its lightOptions/source to that layer's id, or leave it empty for the comp's Environment Layer or a flat default environment of its colour and intensity, see layer.environment; an Environment light switches a Classic 3D comp to Advanced 3D), name?, color?, intensity?, coneAngle?, coneFeather?, falloff?: None\|Smooth\|Inverse Square Clamped, radius?, falloffDistance?, castsShadows?, shadowDarkness?, shadowDiffusion?, position? [x,y,z], poi? [x,y,z]} |
| `layer.setSwitch` | Layer Switch | {layers?, switch: video\|audio\|solo\|lock\|shy\|collapse\|quality\|fx\|frameBlend\|motionBlur\|adjustment\|threeD\|guide\|preserveTransparency, value?, merge?, others? (the named layers alone: the other layers get the opposite state, or come back)} |

## Команды light.* (3)

| id | что делает | параметры |
| --- | --- | --- |
| `light.controlWithCamera` | Control Light with Camera (Layer › Light) | {comp?, layers?: lights (default selected), camera? (default active), on?: bool (default toggle)} |
| `light.environmentBackground` | Create Environment Light Background Layer (Layer › Light) | {comp?, layer?: environment light (default selected / first)} |
| `light.fromModel` | Create Lights from 3D Model (Layer › Light) | {comp?, layers?: 3D model layers (default selected)} |

## Команды material.* (4)

| id | что делает | параметры |
| --- | --- | --- |
| `material.duplicateAssign` | Duplicate and Assign Material (Layer › Material) | {layers? (first = source)} |
| `material.reset` | Reset Material (Layer › Material) | {layers?} |
| `material.revealSource` | Reveal Material Source in Project (Layer › Material) | {layer?} |
| `material.set` | Material Options | {layers?, time?, castsShadows?: off\|on\|only, acceptsShadows?: off\|on\|only, acceptsLights?, appearsInReflections? (model and primitive layers), baseColor?, metallic?, roughness?, emissive? (primitive layers; a model layer keeps its file's materials), lightTransmission?, ambient?, diffuse?, specularIntensity?, specularShininess?, metal? (footage, solid, text, shape and precomp layers)}; a parameter none of the layers has is an error |

## Команды view.* (16)

| id | что делает | параметры |
| --- | --- | --- |
| `view.3d.activeCamera` | Active Camera (View › Switch 3D View) | {comp?} |
| `view.3d.back` | Back (View › Switch 3D View) | {comp?} |
| `view.3d.bottom` | Bottom (View › Switch 3D View) | {comp?} |
| `view.3d.custom1` | Custom View 1 (View › Switch 3D View) | {comp?} |
| `view.3d.custom2` | Custom View 2 (View › Switch 3D View) | {comp?} |
| `view.3d.custom3` | Custom View 3 (View › Switch 3D View) | {comp?} |
| `view.3d.default` | Default (View › Switch 3D View) | {comp?} |
| `view.3d.front` | Front (View › Switch 3D View) | {comp?} |
| `view.3d.last` | Switch to Last 3D View (View) | {comp?} |
| `view.3d.left` | Left (View › Switch 3D View) | {comp?} |
| `view.3d.right` | Right (View › Switch 3D View) | {comp?} |
| `view.3d.top` | Top (View › Switch 3D View) | {comp?} |
| `view.get3D` | 3D View State | {comp?} → current 3D view, view camera, active camera layer, lights |
| `view.reset3DView` | Reset 3D View (View) | {comp?} |
| `view.set3DView` | Switch 3D View | {view: activeCamera\|default\|front\|left\|top\|back\|right\|bottom\|custom1\|custom2\|custom3, comp?} |
| `view.set3DViewCamera` | Set 3D View Camera | {view, eye? [x,y,z], poi? [x,y,z], zoom?} |

<!-- generated:end -->
