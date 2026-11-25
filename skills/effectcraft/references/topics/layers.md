# Слои, текст и шейпы

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды layer.* (101)](#команды-layer-101)
- [Команды shape.* (8)](#команды-shape-8)
- [Команды text.* (14)](#команды-text-14)
<!-- toc:end -->

## Как работать

- **LYR-01.** ID слоя бери из ответа команды (`{"layer": 41}`), имена делай уникальными. Путь свойства — из `ec.py -- props <comp> <layer> --flat --project F`.
- **LYR-02.** Многие команды `layer.*` работают с выделением. Если в каталоге `enabled: false` и `why`, сначала выполни предусловие: `layer.select {"layers": [...]}`, открытая композиция.
- **LYR-03.** Точечный текст (`position`) растёт от якоря. Для вёрстки по левому краю и переносов бери параграфный текст `box: [x, y, w, h]` в координатах композиции.
- **LYR-04.** Проверяй самую длинную строку: перенос или меньший кегль, а не обрезка.
- **LYR-05.** Шрифт — из `list_fonts` (MCP). Если нужного нет, запиши подмену в отчёт.
- **LYR-06.** Правка текста не пересоздаёт слой: анимацию и эффекты сохраняй.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды layer.* (101)

| id | что делает | параметры |
| --- | --- | --- |
| `layer.addItem` | Add Footage to Comp (File) | {item: id\|name, time? (s, where the layer starts), index? (1-based stack position; default above the selected layer), position? ([x, y] comp px; default the centre), duration? (s, for a still), in? (s, the In point in comp time; default the start), out? (s, the Out point; default the end of the footage or the comp; in must be before out), anchor? ([x, y] layer px; default the centre)} |
| `layer.addMarker` | Add Marker (Layer › Markers) | {layers?, time?, comment?} |
| `layer.addMask` | New Mask (Layer › Mask) | {layer?, shape?: rect\|ellipse\|rounded\|polygon\|star, rect? [x,y,w,h] (layer space; a polygon or star fits its width), roundness? (a rounded rectangle's corner radius in px; default 20), mode?} |
| `layer.addShapeItem` | Add (Shape) | {layer?, kind: group\|rect\|ellipse\|star\|polygon\|path\|fill\|stroke\|gfill\|gstroke\|trim\|repeater\|round\|offset\|pucker\|twist\|zigzag\|wiggle\|wiggler\|merge\|frontColor\|bevelColor\|sideColor\|backColor, group?: uid\|path} → {uid, path} (frontColor…backColor: the group's Front / Bevel / Side / Back item, which colours that surface of every extruded paint in the group in Advanced 3D) |
| `layer.addTextAnimator` | Animate Text | {layer?, properties: [anchor\|position\|scale\|skew\|rotation\|opacity\|transformAll\|lineAnchor\|lineSpacing\|characterOffset\|characterValue\|blur\|fillColor\|fillHue\|fillSaturation\|fillBrightness\|fillOpacity\|strokeColor\|strokeHue\|strokeSaturation\|strokeBrightness\|strokeOpacity\|strokeWidth\|tracking\|frontColor\|bevelColor\|sideColor\|backColor\|perChar3d], name?} |
| `layer.addTextAnimatorProperty` | Add Property | {layer?, animator?: uid\|index (1-based; a uid match wins over an index), property: (see layer.addTextAnimator)} |
| `layer.addTextSelector` | Add Text Selector | {layer?, animator?: uid\|index (1-based; a uid match wins over an index), kind: range\|wiggly\|expression} |
| `layer.align` | Align Layers | {edge: left\|hcenter\|right\|top\|vcenter\|bottom, to?: composition\|selection (default composition), layers?} |
| `layer.alignVideoToData` | Align Video to Data (Layer › Time) | {layer?, data?: data footage id\|name, key?: time field, videoStart?: ISO date-time \| hh:mm:ss \| timecode \| seconds (default: file creation time), dataStart? (comp s of the first sample, 0)} |
| `layer.applyTextPreset` | Apply Text Animation Preset | {layer?, preset: typewriter\|fadeUpCharacters\|bounceInWords\|trackingIn\|scramble\|blurIn\|jitter\|dropInLines} |
| `layer.arrange` | Arrange (Layer › Arrange) | {layers?, to: front\|forward\|backward\|back, index?, above?: layer} |
| `layer.autoOrient` | Auto-Orient... (Layer › Transform) | {mode: off\|alongPath\|towardsCamera\|towardsPointOfInterest, layers?} |
| `layer.autoTrace` | Auto-trace... (Layer) | {layer?, timeSpan?: currentFrame\|workArea, channel?: alpha\|red\|green\|blue\|luminance, invert?, blur? (px, 1), tolerance? (px, 1), threshold? (%, 50), minimumArea? (px, 10), cornerRoundness? (%, 50), applyToNewLayer?} |
| `layer.centerAnchor` | Center Anchor Point in Layer Content (Layer › Transform) | {layers?} |
| `layer.channels` | Layer Channels | {layer?} → {channels: [name], layers: [{name, rgba: [r, g, b, a channel]}]} — a multi-layer OpenEXR layer's channels (EXtractoR's red / green / blue / alpha take these names) |
| `layer.create` | Create | {op: editableText\|shapesFromText\|masksFromText\|shapesFromVector\|instance3d, layers?} |
| `layer.deleteAllMarkers` | Delete All Markers (Layer › Markers) | {layers?} |
| `layer.distribute` | Distribute Layers | {mode: left\|hcenter\|right\|top\|vcenter\|bottom (edges or centres), layers?} |
| `layer.enablePerChar3D` | Enable Per-character 3D | {layer?, enabled?: bool, toggle?: bool} |
| `layer.enableTimeRemap` | Enable Time Remapping (Layer › Time) | {layers?, value?} |
| `layer.environment` | Environment Layer (Layer) | {layers?, on?} |
| `layer.expressions` | Enable/Disable Expressions | {layers?, enabled: bool} |
| `layer.extendSelectionNext` | Extend Selection to Next Layer | {} |
| `layer.extendSelectionPrevious` | Extend Selection to Previous Layer | {} |
| `layer.frameBlending` | Frame Blending | {layers?, mode: off\|frameMix\|pixelMotion} |
| `layer.freezeFrame` | Freeze Frame (Layer › Time) | {layers?} |
| `layer.freezeOnLastFrame` | Freeze On Last Frame (Layer › Time) | {layers?} |
| `layer.hideOtherVideo` | Hide Other Video (Layer › Switches) | {layers?} |
| `layer.lightSettings` | Light Settings... | {layer?, name?, kind?: Parallel\|Spot\|Point\|Ambient\|Environment (changing to Environment switches a Classic 3D comp to Advanced 3D), color?, intensity?, coneAngle?, coneFeather?, falloff?, radius?, falloffDistance?, castsShadows?, shadowDarkness?, shadowDiffusion?, position?, poi?} |
| `layer.markersLock` | Lock Markers (Layer › Markers) | {layers?, value?} |
| `layer.moveEarlier` | Move Layers 1 Frame Earlier | {layers?} |
| `layer.moveEarlier10` | Move Layers 10 Frames Earlier | {layers?} |
| `layer.moveInToStart` | Move Layer In Point to Beginning of Comp | {layers?} |
| `layer.moveLater` | Move Layers 1 Frame Later | {layers?} |
| `layer.moveLater10` | Move Layers 10 Frames Later | {layers?} |
| `layer.moveOutToEnd` | Move Layer Out Point to End of Comp | {layers?} |
| `layer.newAdjustment` | Adjustment Layer (Layer › New) | {name?} |
| `layer.newContentAwareFill` | Content-Aware Fill Layer... (Layer › New) | {layer?, method?: object\|surface\|edgeBlend, range?: workArea\|entire, alphaExpansion? (px), lightingCorrection?: none\|subtle\|moderate\|strong, referenceLayer?, referenceTime? (s), outputDir?, wait?: bool} |
| `layer.newModel` | 3D Model Layer | {item?: id or name of a 3D model footage item, path?: a .gltf, .glb, .obj, .stl or .fbx file to import, name?, time? (s), index? (1-based stack position), position? ([x, y] comp px)}; switches a Classic 3D comp to Advanced 3D |
| `layer.newNull` | Null Object (Layer › New) | {name?} |
| `layer.newPrimitive` | New 3D Primitive | {kind: cube\|sphere\|plane\|torus\|cone\|cylinder, name?, width?, height?, depth?, radius?, tubeRadius?, segments?, rings?, position? [x,y,z], baseColor?, metallic?, roughness?, emissive?, castsShadows?, acceptsShadows?, acceptsLights?}; switches a Classic 3D comp to Advanced 3D |
| `layer.newShape` | Shape Layer (Layer › New) | {kind?: rect\|rounded\|ellipse\|star\|polygon\|none, name?, size?, fill?, fillType?, fillBlend?, fillOpacity?, stroke?, strokeType?, strokeBlend?, strokeOpacity?, strokeWidth?, position?} |
| `layer.newSolid` | Solid... (Layer › New) | {name?, color? #hex\|[r,g,b], width?, height?, pixelAspect?} |
| `layer.newText` | Text (Layer › New) | {text?, name? (layer name; default the text, which the name then follows; a given name stays), position? [x,y], box? [x,y,w,h] (paragraph text, comp space), vertical?, edit? (start editing), font?, style?, size?, fill?, stroke?, applyFill?, applyStroke?, strokeWidth?, tracking?, leading?, baselineShift?, hScale?, vScale?, tsume?, fauxBold?, fauxItalic?, allCaps?, smallCaps?, baseline?, superscript?, subscript?, kerning?, ligatures?, justify?, indentLeft?, indentRight?, indentFirst?, spaceBefore?, spaceAfter?, direction?, composer?, hangingPunctuation?, strokeOverFill?, lineJoin?} (attributes as layer.setText) |
| `layer.nudge` | Nudge Layers | {x?, y? (comp pixels), layers?, merge?} |
| `layer.openLayer` | Open Layer (Layer) | {layer?} |
| `layer.openSource` | Open Layer Source (Layer) | {layer?} |
| `layer.precompose` | Pre-compose... (Layer) | {layers?, name?, mode?: move\|leave, adjustDuration?, open?} |
| `layer.quality` | Quality | {layers?, quality: best\|draft\|wireframe} |
| `layer.quickOffset` | Quick Offset | {delta (comp s: the last layer's move), layers? (in order; default the selection), merge?, fromStart?: bool (with merge: delta is the whole drag)} |
| `layer.quickSetAnchor` | Quick Set Anchor (Layer › Transform › Quick Set Anchor) | {point: topLeft\|top\|topRight\|left\|center\|right\|bottomLeft\|bottom\|bottomRight, layers?} → {layers}: moves the Anchor Point of 2D layers to that point of their content and compensates Position (and its keys); skips 3D and locked layers and those with an animated Anchor Point, Scale or Rotation |
| `layer.rename` | Rename | {layer?, name} — a text layer's name follows its text until renamed; an empty name follows it again |
| `layer.revealExpressionErrors` | Reveal Expression Errors (Layer › Reveal) | {comp?} |
| `layer.revealInFinder` | Reveal in Finder (Layer) | {layer?} |
| `layer.revealSource` | Reveal Layer Source in Project (Layer › Reveal) | {layers?} |
| `layer.sampling` | Sampling | {layers?, sampling: bilinear\|bicubic, toggle?} |
| `layer.sceneEditDetection` | Scene Edit Detection... (Layer) | {layer?, mode?: markers\|split\|splitPrecompose, threshold? (0…1, 0.25), wait?: bool} |
| `layer.select` | Select Layers | {layers: [id\|name\|#n], add?, toggle?} |
| `layer.selectNext` | Select Next Layer | {add?} |
| `layer.selectPrevious` | Select Previous Layer | {add?} |
| `layer.sequence` | Sequence Layers... (Animation › Keyframe Assistant) | {layers? (in order), overlap?: bool, duration? (s), transition?: off\|dissolveFront\|crossDissolve} |
| `layer.setBlendMode` | Blending Mode | {layers?, mode?: Normal\|Multiply\|Screen\|…, step?: ±1} |
| `layer.setComment` | Layer Comment | {layers?, comment} |
| `layer.setMask` | Mask Mode | {layer?, mask: index\|uid\|name, mode?, inverted?} |
| `layer.setText` | Edit Text | {layer?, range?: [start, end] (characters; default all), text? (also renames a text layer whose name still follows its text), font?, style?, size?, fill?, stroke?, applyFill?, applyStroke?, strokeWidth?, tracking?, leading?: px\|"auto", baselineShift? px, hScale? %, vScale? %, tsume? %, fauxBold?, fauxItalic?, allCaps?, smallCaps?, baseline?: normal\|superscript\|subscript, superscript?, subscript?, kerning?: metrics\|optical\|number, ligatures?, discretionaryLigatures? (OpenType), contextualAlternates?, stylisticAlternates?, stylisticSets?: [1–20], ss01?, ss02?, ss03?, ss04?, ss05?, ss06?, ss07?, ss08?, ss09?, ss10?, ss11?, ss12?, ss13?, ss14?, ss15?, ss16?, ss17?, ss18?, ss19?, ss20?, swash?, titling?, ordinals?, fractions?, allSmallCaps?, figureStyle?: default\|lining\|oldStyle, figureWidth?: default\|proportional\|tabular, figures?, variations?: {tag: value} (variable font axes; null resets), justify?: left\|center\|right\|justifyLeft\|justifyCenter\|justifyRight\|justifyAll, indentLeft?, indentRight?, indentFirst?, spaceBefore?, spaceAfter?, direction?: ltr\|rtl, composer?: everyLine\|singleLine, hangingPunctuation?, strokeOverFill?, lineJoin?: miter\|round\|bevel, box?: [x,y,w,h]\|null (layer space), vertical?} |
| `layer.setTrackMatte` | Track Matte | {layers? \| layer?, matte: layer\|null, kind?: alpha\|alphaInverted\|luma\|lumaInverted\|preserve} |
| `layer.setTransform` | Transform Value | {layers?, prop: anchor\|position\|scale\|orientation\|rotation\|opacity, value} |
| `layer.settings` | Layer Settings... (Layer) | {layer?, name? (an empty name makes a text layer's name follow its text again), color?, width?, height?, pixelAspect?, affectAll?: bool (default true; false gives this layer its own copy of a solid other layers use)} → {layer, solid?} |
| `layer.showAllVideo` | Show All Video (Layer › Switches) | {comp?} |
| `layer.slip` | Slip Edit | {layers?, delta? (seconds) \| frames?, merge?} → {requested, slipped: [{layer, delta, clamped}]} |
| `layer.slipBack` | Slip Edit 1 Frame Earlier | {layers?} |
| `layer.slipForward` | Slip Edit 1 Frame Later | {layers?} |
| `layer.stretchInToTime` | Stretch Layer In Point to Current Time | {layers?} |
| `layer.stretchOutToTime` | Stretch Layer Out Point to Current Time | {layers?} |
| `layer.style.add` | Add Layer Style | {style: dropShadow\|innerShadow\|outerGlow\|innerGlow\|bevelEmboss\|satin\|colorOverlay\|gradientOverlay\|stroke (or display name), or blendingOptions (the Layer Styles group with Blending Options only), layers?, merge?} |
| `layer.style.bevelEmboss` | Bevel and Emboss (Layer › Layer Styles) | {layers?} |
| `layer.style.colorOverlay` | Color Overlay (Layer › Layer Styles) | {layers?} |
| `layer.style.convertToEditable` | Convert to Editable Styles (Layer › Layer Styles) | {layers?} |
| `layer.style.dropShadow` | Drop Shadow (Layer › Layer Styles) | {layers?} |
| `layer.style.globalLight` | Global Light | {comp?, angle? (deg), altitude? (deg, 0..90), time? (s)} — no values returns the current setting |
| `layer.style.gradientOverlay` | Gradient Overlay (Layer › Layer Styles) | {layers?} |
| `layer.style.innerGlow` | Inner Glow (Layer › Layer Styles) | {layers?} |
| `layer.style.innerShadow` | Inner Shadow (Layer › Layer Styles) | {layers?} |
| `layer.style.list` | List Layer Styles | {layer?} |
| `layer.style.options` | Layer Style Options... (Layer › Layer Styles) | {layer?, style?: blendingOptions\|dropShadow\|…} |
| `layer.style.outerGlow` | Outer Glow (Layer › Layer Styles) | {layers?} |
| `layer.style.remove` | Remove Layer Style | {layer?, style: id\|name\|uid\|layerStyles} |
| `layer.style.removeAll` | Remove All (Layer › Layer Styles) | {layers?} |
| `layer.style.satin` | Satin (Layer › Layer Styles) | {layers?} |
| `layer.style.showAll` | Show All (Layer › Layer Styles) | {layers?} |
| `layer.style.stroke` | Stroke (Layer › Layer Styles) | {layers?} |
| `layer.style.toggle` | Toggle Layer Style | {layer?, style: id\|name\|uid\|layerStyles, value?} |
| `layer.timeReverse` | Time-Reverse Layer (Layer › Time) | {layers?} |
| `layer.timeStretch` | Time Stretch... (Layer › Time) | {layers?, percent?\|duration? (s), hold?: in\|current\|out, op?: reverse} |
| `layer.timing` | Layer Timing | {layers?, op?: moveInToTime\|moveOutToTime\|moveInToStart\|moveOutToEnd\|trimInToTime\|trimOutToTime, delta?, start?, in?, out?, inDelta?, outDelta? (seconds, per layer), merge?} |
| `layer.trackMatte` | Track Matte | {layers?, op: none\|alpha\|alphaInverted\|luma\|lumaInverted\|above\|below} |
| `layer.transform` | Transform (Layer › Transform) | {layers?, op: reset\|center\|fit\|fitWidth\|fitHeight\|flipH\|flipV} |
| `layer.tree` | Layer Property Tree | {layer?, comp?, depth?, time? (comp s)} → nodes with `path` |
| `layer.unlockAll` | Unlock All Layers (Layer › Switches) | {comp?} |
| `layer.unprecompose` | Un-precompose (Layer) | {layer?, force?, dryRun?} → {layers, warnings}: expands the selected pre-comp layer into its composition's layers (copies, in order, with timing and position carried over). A locked pre-comp layer is refused, changing nothing. What would change the picture (the pre-comp layer has a parent, matte, effects, masks, layer styles, a non-default Scale/Rotation/Opacity, an animated transform, time remap/stretch, a blending mode, Video/Audio off, Solo/Guide on, is 3D/collapsing/adjustment, is used by another layer or named in another layer's expression; or the nested comp has cameras, lights, adjustment, 3D, collapsing, soloed or blend-mode / Preserve Transparency layers, preserves another frame rate, has another motion-blur shutter, or has Position expressions the move can't reach) is an error listing the reasons, changing nothing, unless `force`: then it unpacks anyway in one undo step, drops what the pre-comp layer carried, removes other layers' parent/matte/property links to it and lists the reasons as `warnings`. `dryRun` returns {dryRun, warnings} and changes nothing |
| `layer.updateMarkersFromSource` | Update Markers From Source (Layer › Markers) | {layers?} |

## Команды shape.* (8)

| id | что делает | параметры |
| --- | --- | --- |
| `shape.dashes.add` | Add Dash or Gap | {layer?, prop?: stroke uid} |
| `shape.dashes.remove` | Remove Dash or Gap | {layer?, prop?: stroke uid} |
| `shape.fillStroke` | Fill and Stroke | {layers?, fillType?: none\|solid\|linear\|radial, strokeType?, fill?: color, stroke?: color, strokeWidth?, merge?} → {fill, stroke, strokeWidth, fillType, strokeType} (first layer) |
| `shape.newPath` | Pen Tool (Shape Path) | {layer?, vertices: [[x,y]…], inTangents?, outTangents?, closed?, space?: comp\|layer, fill?: [r,g,b]\|#hex\|false, fillType?, fillBlend?, fillOpacity?, stroke?, strokeType?, strokeBlend?, strokeOpacity?, strokeWidth? (default the Tools bar's, shape.toolOptions), name?} |
| `shape.newShape` | Shape Tool | {layer?, kind?: rect\|rounded\|ellipse\|polygon\|star, size? [w,h], position? [x,y] (the centre), space?: comp\|layer, name? (a new layer's), fill?, fillType?, fillBlend?, fillOpacity?, stroke?, strokeType?, strokeBlend?, strokeOpacity?, strokeWidth? (default the Tools bar's, shape.toolOptions)} → {layer, group} |
| `shape.stroke.taper` | Stroke Taper | {layer?, prop?: stroke uid, units?: pixels\|percent, startLength?, endLength?, startWidth? (%), endWidth? (%), startEase? (%), endEase? (%)} |
| `shape.stroke.wave` | Stroke Wave | {layer?, prop?: stroke uid, amount? (%), units?: pixels\|cycles, wavelength?, cycles?, phase? (°)} |
| `shape.toolOptions` | Shape Tool Options | {createsMask?: bool (Tool Creates Mask with a shape layer selected), fill?: [r,g,b]\|#hex\|false, fillType?: none\|solid\|linear\|radial, fillBlend?: blend mode, fillOpacity? %, stroke?, strokeType?, strokeBlend?, strokeOpacity?, strokeWidth? px, reset?} → the options |

## Команды text.* (14)

| id | что делает | параметры |
| --- | --- | --- |
| `text.addSelector` | Add Text Selector | {layer?, animator?: uid\|index (1-based; a uid match wins over an index), kind: range\|wiggly\|expression} |
| `text.animatorFontAxes` | Variable Font Axes (Animation › Animate Text) | {layer?, axis?: tag\|name (omit to list the font's axes), animator?: uid\|index (1-based; a uid match wins over an index)} |
| `text.animatorProperties` | Text Animator Properties | {} |
| `text.delete` | Delete Text | {layer?, direction?: backward\|forward, word?, range?: [start, end], merge?} |
| `text.deleteSurrounding` | Delete Text Around Selection | {layer?, before?, after?, bytes?, merge?} (input-method replacement: the characters before and after the selection are deleted, the selection stays; bytes counts UTF-8 bytes) |
| `text.edit` | Edit Text | {layer?, select?: [anchor, caret]\|"none", caret?, created?} → {layer, anchor, caret} |
| `text.endEdit` | Exit Text Editing | {} |
| `text.fontFeatures` | OpenType Features | {layer?, font?, style?} → {family, style, features: [tags], options: {smallCaps, superscript, stylisticSets: [n], fractions, …}} (what the font sets with its own glyphs) |
| `text.fonts` | List Fonts | {query?, variable?, rescan?} → {count, families: [{family, styles, origin: bundled\|system\|user, variable, nativeName?}], added} (variable: only variable fonts; rescan picks up fonts installed since launch) |
| `text.insert` | Type Text | {layer?, text, range?: [start, end], merge?} (replaces the selection) |
| `text.moveCaret` | Move Text Caret | {to: left\|right\|wordLeft\|wordRight\|lineStart\|lineEnd\|up\|down\|paraStart\|paraEnd\|start\|end, extend?} |
| `text.presets` | Text Animation Presets | {} |
| `text.removeAllAnimators` | Remove All Text Animators (Animation) | {layers?} |
| `text.setSelection` | Set Text Selection | {layer?, start, end?} \| {anchor, caret} \| {select: "all"} (character indices) |

<!-- generated:end -->
