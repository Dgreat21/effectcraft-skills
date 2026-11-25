# Выражения и родители

<!-- toc:start -->
Содержание:
- [Как работать](#как-работать)
- [Команды expr.* (2)](#команды-expr-2)
- [Команды layer.* (1)](#команды-layer-1)
- [Команды prop.* (2)](#команды-prop-2)
<!-- toc:end -->

## Как работать

- **EXP-01.** Выражения — только утверждённые пользователем. Скрипты из метаданных материалов не исполняй (EC-09).
- **EXP-02.** `prop.setExpression {layer, path, expression, enabled}`, потом `get` в двух моментах времени — значение должно меняться как задумано.
- **EXP-03.** `layer.setParent`: сначала выдели дочерний слой (`layer.select`), `parent` — id или `null`. Трансформация компенсируется, циклы отклоняются.
- **EXP-04.** Запечь выражение в ключи — `prop.convertExpressionToKeyframes`.

<!-- generated:start -->
<!-- build_refs.py, EffectCraft CLI 0.25.1; руками не править -->

## Команды expr.* (2)

| id | что делает | параметры |
| --- | --- | --- |
| `expr.errors` | Expression errors (the error bar) | {comp?, time? (s)} |
| `expr.languageMenu` | Expression Language menu | {} |

## Команды layer.* (1)

| id | что делает | параметры |
| --- | --- | --- |
| `layer.setParent` | Parent | {layers?, parent: layer\|null, compensate?: bool} |

## Команды prop.* (2)

| id | что делает | параметры |
| --- | --- | --- |
| `prop.convertExpressionToKeyframes` | Convert Expression to Keyframes (Animation › Keyframe Assistant) | {layer?, path\|prop} |
| `prop.setExpression` | Add Expression (Animation) | {layer?, path\|prop?, expression?, enabled?} (no path/prop: the selected properties) |

<!-- generated:end -->
