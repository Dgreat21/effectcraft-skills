# Свойства, ключи и анимация

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды anim.* (9)](#команды-anim-9)
- [Команды keys.* (37)](#команды-keys-37)
- [Команды prop.* (16)](#команды-prop-16)
<!-- toc:end -->

## Как работать

- **ANM-01.** `prop.addKey` по умолчанию считает время в секундах слоя. Для времени композиции ставь `timeBase: "comp"` и явно указывай `layer`.
- **ANM-02.** Правка — меняй нужные ключи (`keys.*`), не пересоздавай слой.
- **ANM-03.** Проверка: `ec.py -- get <comp> <layer> <path> --time S --project F --json` в нескольких точках плюс кадры `ec.py verify`.
- **ANM-04.** Линейные ключи — не сглаживание. Сглаживание и скорость — `keys.*` (`ec.py search ease`), готовые движения — `anim.*`.
- **ANM-05.** Луп: первое и последнее состояние совпадают, скорость на стыке непрерывна, конечный кадр не повторяется.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды anim.* (9)

| id | что делает | параметры |
| --- | --- | --- |
| `anim.addKeyframe` | Add Keyframe (Animation) | {} — keys the selected properties at the CTI |
| `anim.applyBuiltinPreset` | Apply Built-in Animation Preset | {preset: id\|name (see anim.builtinPresets), layers?} |
| `anim.applyPreset` | Apply Animation Preset... (Animation) | {path \| preset, layers?} — saved effects and text animators are added to each layer, with their keys at the CTI |
| `anim.applyRecentPreset` | Recent Animation Presets | {index? \| path?, layers?} |
| `anim.browsePresets` | Browse Presets... (Animation) | {} |
| `anim.builtinPresets` | Built-in Animation Presets | {category?} |
| `anim.clearRecentPresets` | Clear Recent Presets (Animation › Recent Animation Presets) | {} |
| `anim.reveal` | Reveal Properties | {kind: keyframes\|animation\|modified} |
| `anim.savePreset` | Save Animation Preset... (Animation) | {path (.ecpreset), name?} — saves the selected properties/effects; a text animator with a selected property is saved whole |

## Команды keys.* (37)

| id | что делает | параметры |
| --- | --- | --- |
| `keys.audioToKeyframes` | Convert Audio to Keyframes (Animation › Keyframe Assistant) | {comp?} |
| `keys.copy` | Copy Keyframes | {} |
| `keys.delete` | Delete Keyframes | {} |
| `keys.deselectAll` | Deselect All Keyframes and Properties | {} |
| `keys.easyEase` | Easy Ease (Animation › Keyframe Assistant) | {which?: both\|in\|out} |
| `keys.easyEaseIn` | Easy Ease In (Animation › Keyframe Assistant) | {} |
| `keys.easyEaseOut` | Easy Ease Out (Animation › Keyframe Assistant) | {} |
| `keys.exponentialScale` | Exponential Scale (Animation › Keyframe Assistant) | {} — two selected Scale keys |
| `keys.info` | Keyframe Info | {keys?: [{layer, prop, time}]} |
| `keys.interpolation` | Keyframe Interpolation... (Animation) | {interpolation?: linear\|bezier\|continuousBezier\|autoBezier\|hold, in?\|out?: linear\|bezier\|hold, autoBezier?, continuous?, spatial?: linear\|bezier\|continuousBezier\|autoBezier, roving?} |
| `keys.move` | Move Keyframes | {delta (s), merge?} |
| `keys.nudge` | Nudge Keyframes | {frames, merge?} |
| `keys.nudgeBackward` | Move Keyframes 1 Frame Earlier | {} |
| `keys.nudgeBackward10` | Move Keyframes 10 Frames Earlier | {} |
| `keys.nudgeForward` | Move Keyframes 1 Frame Later | {} |
| `keys.nudgeForward10` | Move Keyframes 10 Frames Later | {} |
| `keys.paste` | Paste Keyframes | {layers?, prop?\|path?, time?} |
| `keys.quickOffset` | Quick Offset Keyframes | {delta (comp s: the last layer's keys' move), merge?, fromStart?: bool (with merge: delta is the whole drag)} |
| `keys.rpfCameraImport` | RPF Camera Import (Animation › Keyframe Assistant) | {path: .json\|.csv camera data, comp?} |
| `keys.select` | Select Keyframes | {keys: [{layer, prop: uid \| path (or `path`), time (layer s by default)}], timeBase?: layer\|comp, add?, toggle?: bool (Shift+click: in or out of the selection), selectProperties?: bool (their properties and layers too, as a Timeline click does)} |
| `keys.selectAll` | Select All Keyframes | {layers?, visible?: [{layer, prop}] (every key of these properties)} |
| `keys.selectEqual` | Select Equal Keyframes | {} |
| `keys.selectFollowing` | Select Following Keyframes | {} |
| `keys.selectLabelGroup` | Select Keyframe Label Group | {scope: selected\|all\|visibleSelected\|visibleAll, visible?: [prop uid]} |
| `keys.selectPrevious` | Select Previous Keyframes | {} |
| `keys.set` | Edit Keyframe | {layer?, path\|prop, time (layer s by default), newTime? (same base), timeBase?: layer\|comp, value?, merge?} |
| `keys.setEase` | Set Keyframe Ease | {layer?, path\|prop, time (layer s), side: in\|out, dim?, speed?, influence? %, merge?} |
| `keys.setLabel` | Keyframe Label | {label: name\|none\|0–16} |
| `keys.setMuted` | Mute Keyframes (Animation) | {muted?: bool (default true)} |
| `keys.setSpatialTangents` | Edit Spatial Tangents | {layer?, path\|prop, time (layer s), in?: [dx,dy,dz?], out?, break?, merge?} |
| `keys.smooth` | Smoother | {tolerance? (property units, 1)} |
| `keys.timeReverse` | Time-Reverse Keyframes (Animation › Keyframe Assistant) | {} |
| `keys.toggleHold` | Toggle Hold Keyframe (Animation) | {} |
| `keys.toggleTransform` | Add or Remove Transform Keyframe | {layers?, prop: anchor\|position\|scale\|rotation\|opacity} (Alt+Shift+A/P/S/R/T) |
| `keys.transform` | Transform Keyframes | {timeScale?, timeAnchor? (comp s), timeOffset? (s), valueScale?, valueAnchor?, valueOffset?, dim? \| dims?: [d…], merge?, fromStart?: bool (with merge: values are the whole transform since the drag started)} |
| `keys.velocity` | Keyframe Velocity... (Animation) | {inSpeed?, inInfluence? %, outSpeed?, outInfluence? % (numbers or per-dimension arrays), continuous?} |
| `keys.wiggle` | Wiggler | {apply?: spatial\|temporal, noise?: smooth\|jagged, dimensions?: one\|same\|independent, dimension? (index for `one`), frequency? (keys/s, 5), magnitude?, seed?} |

## Команды prop.* (16)

| id | что делает | параметры |
| --- | --- | --- |
| `prop.addKey` | Add Keyframe | {layer?, path\|prop, time? (layer s by default), timeBase?: layer\|comp, value?} |
| `prop.deselect` | Deselect Property | {layer?, path\|prop} |
| `prop.duplicateGroup` | Duplicate Property Group | {layer?, prop: uid} → {prop: new uid} |
| `prop.editGradient` | Edit Gradient... | {layer?, path\|prop, comp?} — a gradient property; opens the Gradient Editor at the current time |
| `prop.get` | Get Property | {layer?, path\|prop, time? (comp s)} |
| `prop.moveGroup` | Reorder Property Group | {layer?, prop: uid, index (1-based among its siblings)} |
| `prop.pickWhip` | Pick Whip (Link Property) | {layer?, path\|prop, target: {layer, path\|prop, dimension?}, expression?, range?: [start, end], byIndex?: bool} → sets an AE reference expression (`dimension`: one of the target's values, `position[0]`; with `expression`: inserts it there, replacing the characters in `range`, default the end; `byIndex`: an effect's properties by their index, `effect("Color Control")(1)`, as an Alt pick whip does) |
| `prop.removeGroup` | Delete Property Group | {layer?, prop: uid} |
| `prop.renameGroup` | Rename Property Group | {layer?, prop: uid, name} |
| `prop.reset` | Reset Property | {layer?, path\|prop, default?} → removes the expression; the value becomes `default`, else the property's own (an effect parameter's, a Transform property's), as a keyframe at the current time when the property is animated |
| `prop.select` | Select Property | {layer?, path\|prop, add?, selectKeys?} |
| `prop.separateDimensions` | Separate Dimensions (Animation) | {layer?, value?} |
| `prop.set` | Set Property Value | {layer?, path\|prop, value, time? (layer s by default), timeBase?: layer\|comp, merge?, selected? (also the other selected layers), offset? (them by the same change), proportional? (with offset: Proportional Scrubbing, each layer by its share in selection order, the first none, the last all), dims? (with selected, a typed value: the components edited, e.g. [2] for Z; the other layers keep the rest of their own value), follow? (with dims: components that move on each other layer by the change its first typed component takes), factor? (with selected, a typed `*` or `/`: the other layers take their own value times it, in the dims components of a vector), addend? (the same for a typed `+`: their own value plus it)} |
| `prop.setGroupEnabled` | Enable Property Group | {layer?, prop: uid, value?} |
| `prop.toggleAnimation` | Toggle Stopwatch | {layer?, path\|prop, value?, merge?, selected?} |
| `prop.toggleKey` | Add or Remove Keyframe at Current Time | {layer?, path\|prop, selected?} |

<!-- generated:end -->
