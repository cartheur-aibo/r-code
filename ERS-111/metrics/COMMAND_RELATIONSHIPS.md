# ERS-111 Command Relationships

Diagram outputs:
- `ERS-111/export/CommandRelationships.dot`
- `ERS-111/export/CommandRelationships.pdf`

## What The Diagram Shows

The diagram groups the ERS-111 sample commands by role and shows how they usually relate during execution:

- `Program Start`
Initial entry into the script.

- `State & Data`
Setup and state mutation commands such as `SET`, `LET`, `ADD`, `MOD`, `DIV`, `MUL`, `RND`, `LOAD`, `SAVE`, and `DEF`.

- `Main Loop`
The recurring control point, usually built from labels like `:100`, `GO`, or `DO ... LOOP`.

- `Conditions`
Decision-making commands such as `IF`, `CSET`, `SWITCH`, and `CASE`.

- `Body & Media`
Commands that make AIBO do something: `POSE`, `MOVE`, `PLAY`, `STOP`, `QUIT`, and `REC`.

- `Timing & Gating`
Commands that hold, pace, or repeat execution: `WAIT`, `WHILE ... WEND`, `REPEAT ... UNTIL`, and `FOR ... NEXT`.

- `Subroutines & Events`
Commands that shift execution to reusable or event-driven logic: `CALL`, `RETURN`, `ONCALL`, `RESUME`, and `EXIT`.

- `Block Ends`
Structural closers such as `ELSE`, `ENDIF`, and `END`.

## Typical Relationship Pattern

The common execution pattern is:

`Start -> State -> Main Loop -> Conditions -> Action -> Timing -> Main Loop`

with side paths for:

- subroutine delegation and return
- direct `GO:label` jumps back to the main loop
- block-based branching with `ELSE` and `ENDIF`

This is meant to be an efficient map of how the command families fit together, rather than a full syntax reference.
