# ERS-111 PMS Sample Control Flow

This note describes the control flow style used in the sample R-CODE files under `ERS-111/PMS-RCODE11x_E/sample`.

## Core Idea

R-CODE normally runs top to bottom, one line at a time.

Control flow changes when the script uses:
- labels such as `:100`
- jumps such as `GO:100`
- conditionals such as `IF:...`
- branch tables such as `SWITCH` and `CASE`
- loops such as `DO ... LOOP` or `WHILE ... WEND`
- subroutines such as `CALL:label` and `RETURN`

## Main Pieces

### Labels

`:<label>` marks a destination in the script.

Example:

```txt
:100
```

This defines a label named `100`.

Labels are often used as the top of a main loop or as named action blocks.

### Unconditional Jump

`GO:<label>` jumps directly to a label.

Example:

```txt
GO:100
```

This sends execution back to label `100`.

### Conditional Branching

`IF` checks a condition and changes flow when the condition matches.

Examples:

```txt
IF:<:Touch_head_press:200:100
IF:t:>=:100:CALL:120
```

These patterns mean:
- jump to label `100` if the condition is true
- call subroutine `120` if the condition is true

R-CODE also supports block form:

```txt
IF:x:=:0:THEN
  ...
ELSE
  ...
ENDIF
```

### Multi-Way Branching

`SWITCH` and `CASE` are used when the script has several possible actions.

Example:

```txt
SWITCH:head
CASE:0:MOVE:HEAD:ABS:-30:0:0:500
CASE:1:MOVE:HEAD:ABS:-30:-30:0:500
CASE:2:MOVE:HEAD:ABS:-30:-60:0:500
```

This means the script chooses one command based on the current value of `head`.

### Loops

The samples use several loop styles:

- `DO ... LOOP`
- `WHILE ... WEND`
- `REPEAT ... UNTIL`
- `FOR ... NEXT`

Examples:

```txt
DO
  ...
LOOP
```

```txt
WHILE:Distance:>:500
  ...
WEND
```

These repeat blocks of commands until the loop condition changes or control exits elsewhere.

### Subroutines

`CALL:<label>` jumps into a labeled routine and `RETURN` comes back.

Example:

```txt
IF:t:>=:100:CALL:120
...
:120
...
RETURN
```

This is used when the same action logic should be reused without duplicating lines.

## Common Pattern In These Samples

Many of the sample programs use a central label such as `:100` as the main loop entry point.

Example pattern:

```txt
:100
IF:=:mode:0:1000
GO:100

:1000
...do work...
GO:100
```

Flow:

1. Execution reaches `:100`.
2. The script checks a condition.
3. If the condition is true, it jumps to another labeled block such as `:1000`.
4. That block performs an action.
5. The action block jumps back with `GO:100`.

This creates a simple event loop:

`main label -> test -> action block -> return to main label`

## About `:100`

A line like this:

```txt
:100       //A condition branches off only with a main loop.
```

means:

- `:100` is a label
- it acts as the main loop branch point
- other conditions jump back to it or jump away from it

So `:100` is not itself an action command. It is a control-flow marker that organizes the script.

## Typical Sample Behavior

A lot of these ERS-111 scripts follow this rhythm:

1. Initialize variables with `SET`.
2. Move AIBO into a safe starting pose with `POSE`.
3. Enter a main loop at a label like `:100` or with `DO`.
4. Check sensors or state using `IF`, `SWITCH`, or `CASE`.
5. Run motions with `MOVE` or `PLAY`.
6. Pause or wait with `WAIT`.
7. Jump or loop back to continue monitoring.

That makes the programs feel more like reactive behavior scripts than one-pass linear programs.
