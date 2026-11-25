# Маски, пути, ротоскоп

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды layer.* (15)](#команды-layer-15)
- [Команды mask.* (18)](#команды-mask-18)
- [Команды objectMatte.* (5)](#команды-objectmatte-5)
- [Команды path.* (7)](#команды-path-7)
- [Команды roto.* (14)](#команды-roto-14)
- [Команды timeline.* (1)](#команды-timeline-1)
<!-- toc:end -->

## Как работать

- **MSK-01.** Маску создаёт `layer.addMask` (rect, ellipse, path). `layer.mask.shape` меняет только существующую маску.
- **MSK-02.** Координаты маски — в пространстве слоя. Путь замкнут, растушёвка в пикселях; проверь кадром.
- **MSK-03.** Ротоскоп и `objectMatte.*` — автоматика. Проверяй края на нескольких кадрах и не называй выделение надёжным без проверки.
- **MSK-04.** Замена экрана прямоугольной маской годится только для экрана анфас. Для перспективы нужны углы или трекинг (tracking.md); нет их — честно ставь ключи руками.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды layer.* (15)

| id | что делает | параметры |
| --- | --- | --- |
| `layer.mask.featherFalloff` | Feather Falloff | {layer?, mask?, mode: smooth\|linear} |
| `layer.mask.hideLocked` | Hide Locked Masks (Layer › Mask) | {value?} |
| `layer.mask.invert` | Inverted (Layer › Mask) | {layer?, mask?, value?} |
| `layer.mask.lock` | Locked (Layer › Mask) | {layer?, mask?, value?} |
| `layer.mask.lockOthers` | Lock Other Masks (Layer › Mask) | {layer?, mask?} |
| `layer.mask.mode` | Mask Mode | {layer?, mask?, mode: None\|Add\|Subtract\|Intersect\|Lighten\|Darken\|Difference} |
| `layer.mask.motionBlur` | Motion Blur | {layer?, mask?, mode: sameAsLayer\|on\|off} |
| `layer.mask.remove` | Remove Mask (Layer › Mask) | {layer?, mask?} |
| `layer.mask.removeAll` | Remove All Masks (Layer › Mask) | {layers?} |
| `layer.mask.reset` | Reset Mask (Layer › Mask) | {layer?, mask?} |
| `layer.mask.selectNext` | Select Next Mask | {layer?} |
| `layer.mask.selectPrevious` | Select Previous Mask | {layer?} |
| `layer.mask.set` | Mask Settings | {layer?, mask?, field: feather\|opacity\|expansion, value} |
| `layer.mask.shape` | Mask Shape... (Layer › Mask) | {layer?, mask?, rect: [x, y, w, h], shape?: rect\|ellipse} |
| `layer.mask.unlockAll` | Unlock All Masks (Layer › Mask) | {layers?} |

## Команды mask.* (18)

| id | что делает | параметры |
| --- | --- | --- |
| `mask.addVertex` | Add Mask Vertex | {layer?, mask, point: [x,y], in?, out?, index?} |
| `mask.convertVertex` | Convert Vertex | {layer?, mask: uid (mask or shape Path item), index, smooth?} |
| `mask.deleteVertices` | Delete Mask Vertices | {vertices?} |
| `mask.featherPoint.add` | Add Mask Feather Point | {layer?, mask, segment?, t?: 0..1, point?: [x,y] (layer space), radius? (px, negative = inner), tension? (%)} → {index} |
| `mask.featherPoint.list` | Mask Feather Points | {layer?, mask} |
| `mask.featherPoint.remove` | Delete Mask Feather Point | {layer?, mask, index? \| all?} |
| `mask.featherPoint.set` | Move Mask Feather Point | {layer?, mask, index, segment?, t?, point? (slide along the path), radius?, toward?: [x,y] (radius from the drag point, layer space), tension? (%), merge?} |
| `mask.insertVertex` | Add Vertex | {layer?, mask: uid (mask or shape Path item), segment, t?: 0..1} |
| `mask.interpolate` | Apply Mask Interpolation | {layer?, mask?, times?: [from, to] (s; default the selected Mask Path keys), keyframeRate?: n\|auto, keyframeFields?, linearVertexPaths?, bendingResistance? (0-100), quality? (0-100), addVertices?: n\|false, addVerticesUnit?: pixels\|total\|percent, matchingMethod?: auto\|curve\|polyline, oneToOne?, firstVerticesMatch?} |
| `mask.interpolationOptions` | Mask Interpolation Options | {keyframeRate?: n\|auto, keyframeFields?, linearVertexPaths?, bendingResistance?, quality?, addVertices?: n\|false, addVerticesUnit?: pixels\|total\|percent, matchingMethod?: auto\|curve\|polyline, oneToOne?, firstVerticesMatch?} |
| `mask.moveVertices` | Move Mask Vertices | {vertices?: [{layer, mask, index}], delta: [dx,dy], merge?} |
| `mask.new` | New Mask from Points | {layer?, vertices: [[x,y]…], inTangents?, outTangents?, closed?, mode?} |
| `mask.remove` | Remove Mask | {layer?, mask} |
| `mask.removeAll` | Remove All Masks | {layer?} |
| `mask.selectVertices` | Select Mask Vertices | {vertices: [{layer, mask, index}], add?, toggle?} |
| `mask.setClosed` | Closed | {layer?, mask, closed?} |
| `mask.setRoundness` | Set Mask Roundness | {layer?, mask, roundness (corner radius in px; 0 = square)} |
| `mask.setVertex` | Set Mask Vertex | {layer?, mask, index, point?, in?, out?, merge?} |

## Команды objectMatte.* (5)

| id | что делает | параметры |
| --- | --- | --- |
| `objectMatte.apply` | Object Matte | {layer?, effect? (uid: re-prompt this Object Matte instead of adding one), point: [x, y] (layer pixels: the object), box?: [x0, y0, x1, y1] (layer pixels, around the object), frame? (reference layer frame; default current), track?: follow the object from that frame (default true), before?, after? (frames to follow it; default 30, up to 600)} |
| `objectMatte.freeze` | Freeze Object Matte | {layer?, effect?, wait?} |
| `objectMatte.propagate` | Track Object Matte | {layer?, effect?, direction?: forward\|backward\|both, wait?: block until done} (a background job like Roto Brush propagation; roto.cancel stops it) |
| `objectMatte.status` | Object Matte Status | {layer?, effect?}: the job's progress, whether the instance is frozen, its frames and which are computed |
| `objectMatte.unfreeze` | Unfreeze Object Matte | {layer?, effect?} |

## Команды path.* (7)

| id | что делает | параметры |
| --- | --- | --- |
| `path.convertToBezier` | Convert To Bezier Path (Layer › Mask and Shape Path) | {layer?, layers?, mask?, items?: [uid]} |
| `path.freeTransform` | Free Transform Points (Layer › Mask and Shape Path) | {layer?, mask?, scale?: % \| [x%, y%], rotation?: deg, offset?: [dx, dy], anchor?: [x, y], merge?: string} |
| `path.groupShapes` | Group Shapes (Layer) | {layer?, items?: [uid]} |
| `path.rotoBezier` | RotoBezier (Layer › Mask and Shape Path) | {layer?, mask?, value?} |
| `path.setFirstVertex` | Set First Vertex (Layer › Mask and Shape Path) | {layer?, mask?: uid, index?} |
| `path.toggleClosed` | Closed (Layer › Mask and Shape Path) | {} |
| `path.ungroupShapes` | Ungroup Shapes (Layer) | {layer?, items?: [group uid]} |

## Команды roto.* (14)

| id | что делает | параметры |
| --- | --- | --- |
| `roto.cancel` | Stop Roto Brush | {} |
| `roto.clearStrokes` | Remove Roto Brush Strokes | {layer?, effect?, frame? (only this layer frame), kind?, object? (only this object's strokes)} |
| `roto.freeze` | Freeze | {layer?, effect?, wait?} |
| `roto.model.download` | Download Roto Brush Model | {id, wait?} — the official weights, verified (desktop; uses the system curl) |
| `roto.model.install` | Install Roto Brush Model | {path: weights file, id?, wait?} — verified against the registry's SHA-256 |
| `roto.model.remove` | Remove Roto Brush Model | {id} |
| `roto.model.select` | Use Roto Brush Model | {id: classical\|mobilesam\|sam2.1-hiera-tiny\|sam2.1-hiera-small\|sam2.1-hiera-base-plus\|sam2.1-hiera-large, wait?} (Roto Brush 2.0 / 3.0 use it; wait: loaded before returning) |
| `roto.models` | Roto Brush Models | {} |
| `roto.options` | Roto Brush Options | {diameter?, refineDiameter?, view?: alphaBoundary\|alpha\|alphaOverlay\|none, overlayColor?: [r,g,b], overlayOpacity?, boundaryColor?: [r,g,b], autoPropagate?, object? (the object new strokes belong to, 0–31)} |
| `roto.propagate` | Propagate Roto Brush | {layer?, effect?, direction?: forward\|backward\|both, to? (layer frame: extend the span), wait?: block until done} |
| `roto.span` | Set Segmentation Span | {layer?, effect?, start?, end? (layer frames)} |
| `roto.status` | Roto Brush Status | {layer?, effect?, frame? (layer frame: also report its matte), matte?: include the matte (RLE, base64), compute?: compute the frame if needed, compareTo?: RLE matte to report the IoU against} |
| `roto.stroke` | Roto Brush Stroke | {layer?, kind?: fg\|bg\|refine\|refineErase, points: [[x, y], …] (layer pixels), frame? (layer frame; default current), radius? (layer px; default the tool's diameter / 2), effect?, object? (0–31; default the current object: with a tracker each object is followed on its own and the mattes are united)} |
| `roto.unfreeze` | Unfreeze | {layer?, effect?} |

## Команды timeline.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `timeline.revealMask` | Reveal Created Mask | {comp, layer, mask, projectEpoch} — engine-supplied creation identity |

<!-- generated:end -->
