#!/usr/bin/env python3

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent


COMMON = r'''
digraph G {
  graph [
    pad="0.3",
    nodesep="0.35",
    ranksep="0.5",
    splines=true,
    bgcolor="white"
  ];
  node [
    shape=box,
    style="rounded,filled",
    color="#263238",
    fillcolor="#F7F3E8",
    fontname="Helvetica",
    fontsize=11,
    margin="0.12,0.08"
  ];
  edge [
    color="#455A64",
    fontname="Helvetica",
    fontsize=10,
    arrowsize=0.7
  ];
'''


DIAGRAMS = {
    "CommandRelationships": COMMON + r'''
  rankdir=LR;
  graph [fontname="Helvetica", compound=true];

  node [shape=box, style="rounded,filled", margin="0.14,0.1"];

  subgraph cluster_setup {
    label="Setup";
    color="#C7D8C6";
    style="rounded";
    Start [label="Program Start", fillcolor="#E8F1E7"];
    State [label="State & Data\nSET / LET / ADD / MOD /\nDIV / MUL / RND / LOAD / SAVE / DEF", fillcolor="#F7F3E8"];
  }

  subgraph cluster_flow {
    label="Core Flow";
    color="#D9CBAE";
    style="rounded";
    MainLoop [label="Main Loop\n:label / GO / DO-LOOP", fillcolor="#FBE9D0"];
    Sense [label="Conditions\nIF / CSET / SWITCH / CASE", fillcolor="#E7EEF7"];
    Action [label="Body & Media\nPOSE / MOVE / PLAY / STOP / QUIT / REC", fillcolor="#F6E7D8"];
    Sync [label="Timing & Gating\nWAIT / WHILE-WEND /\nREPEAT-UNTIL / FOR-NEXT", fillcolor="#EFE3F8"];
  }

  subgraph cluster_support {
    label="Support Flow";
    color="#D8C7DE";
    style="rounded";
    Subroutine [label="Subroutines & Events\nCALL / RETURN / ONCALL / RESUME / EXIT", fillcolor="#F7D9D9"];
    EndBlock [label="Block Ends\nELSE / ENDIF / END", fillcolor="#F1F5F9"];
  }

  Start -> State [label="initialize"];
  State -> MainLoop [label="enter main loop"];
  MainLoop -> Sense [label="poll / test"];
  Sense -> Action [label="condition matched"];
  Action -> Sync [label="perform / pace"];
  Sync -> MainLoop [label="reevaluate"];

  Sense -> State [label="set or update state"];
  State -> Sense [label="read variables"];

  Sense -> Subroutine [label="CALL / ONCALL"];
  Subroutine -> State [label="return data"];
  Subroutine -> MainLoop [label="resume"];

  Sense -> EndBlock [label="THEN / ELSE form"];
  EndBlock -> MainLoop [label="block closes"];
  Action -> MainLoop [label="GO:label"];
}
''',
    "EmbodiedBehaviors": COMMON + r'''
  rankdir=LR;

  Boot [label="Boot /\nSafe Pose", fillcolor="#E8F1E7"];
  Sense [label="Sense /\nDecide", fillcolor="#FBE9D0"];
  Action [label="Action\nLoop", fillcolor="#F6E7D8"];
  Sync [label="Synchronize", fillcolor="#E7EEF7"];
  Recover [label="Recover", fillcolor="#F7D9D9"];
  Specialize [label="Task-Specific\nExtension", fillcolor="#EFE3F8"];

  Boot -> Sense;
  Sense -> Action [label="continue"];
  Action -> Sync;
  Sync -> Sense [label="reevaluate"];
  Sense -> Recover [label="fall / fault"];
  Recover -> Boot [label="restore"];
  Sense -> Specialize [label="ball, obstacle,\ncontact, expression"];
  Specialize -> Sync [label="return"];
}
''',
    "CTracking": COMMON + r'''
  rankdir=TB;

  Start [label="Start"];
  Track [label="C-Tracking\nActivate Tracking", fillcolor="#FBE9D0"];
  Stop [label="Quit /\nHand Back Control", fillcolor="#E7EEF7"];

  Start -> Track;
  Track -> Stop [label="done"];
}
''',
    "BootSafePose": COMMON + r'''
  rankdir=TB;

  Boot [label="Boot", fillcolor="#E8F1E7"];
  Pose [label="Boot /\nSafe Pose", fillcolor="#E8F1E7"];
  Listen [label="Resume\nListener", fillcolor="#E7EEF7"];
  Main [label="MainLoop\nReady State", fillcolor="#FBE9D0"];

  Boot -> Pose;
  Pose -> Listen;
  Listen -> Main [label="ready"];
}
''',
    "Move": COMMON + r'''
  rankdir=TB;

  Boot [label="Boot /\nSafe Pose", fillcolor="#E8F1E7"];
  Walk [label="Repeat\nForward Walk", fillcolor="#FBE9D0"];
  Sense [label="Sense Fall\nState", fillcolor="#E7EEF7"];
  Recover [label="Recover", fillcolor="#F7D9D9"];

  Boot -> Walk;
  Walk -> Sense;
  Sense -> Walk [label="stable"];
  Sense -> Recover [label="fallen"];
  Recover -> Boot [label="reset posture"];
}
''',
    "ContactResponse": COMMON + r'''
  rankdir=TB;

  Boot [label="Boot /\nSafe Pose", fillcolor="#E8F1E7"];
  Sense [label="Sense /\nDecide", fillcolor="#E7EEF7"];
  Hug [label="Happy Hug\nResponse", fillcolor="#F6E7D8"];
  Idle [label="Idle Thought", fillcolor="#FBE9D0"];
  Recover [label="Recover", fillcolor="#F7D9D9"];

  Boot -> Idle;
  Idle -> Sense;
  Sense -> Hug [label="contact"];
  Sense -> Idle [label="none"];
  Hug -> Sense [label="complete"];
  Sense -> Recover [label="instability"];
  Recover -> Boot;
}
''',
    "Maze": COMMON + r'''
  rankdir=TB;

  Start [label="Start /\nLoad Stored Poses", fillcolor="#E8F1E7"];
  Scan [label="Head Scan\nPosition", fillcolor="#E7EEF7"];
  Compare [label="When Distance\nbecame < 300", fillcolor="#FBE9D0"];
  Obstacle [label="When there was\nan obstacle in front", fillcolor="#F7D9D9"];
  Turn [label="Turn / Shift /\nAdvance", fillcolor="#F6E7D8"];
  Forward [label="Forward Walk", fillcolor="#F6E7D8"];
  Retry [label="Reset Sample /\nScan Counter", fillcolor="#EFE3F8"];

  Start -> Scan;
  Scan -> Compare;
  Compare -> Forward [label="clear"];
  Compare -> Obstacle [label="blocked"];
  Obstacle -> Turn;
  Turn -> Retry;
  Retry -> Scan [label="re-sample"];
  Forward -> Scan [label="next check"];
}
''',
    "Football": COMMON + r'''
  rankdir=TB;

  Boot [label="Boot /\nSafe Pose", fillcolor="#E8F1E7"];
  Search [label="Set Search Mode /\nSearch Turn", fillcolor="#E7EEF7"];
  Track [label="Start Ball Tracking /\nApproach by Head Angle", fillcolor="#FBE9D0"];
  Advance [label="Advance Left /\nAdvance Right /\nForward Walk", fillcolor="#F6E7D8"];
  Kick [label="Left Kick /\nRight Kick", fillcolor="#EFE3F8"];
  Lost [label="Increment / Reset\nLost Counter", fillcolor="#F7D9D9"];
  Recover [label="Recover", fillcolor="#F7D9D9"];

  Boot -> Search;
  Search -> Track [label="ball found"];
  Search -> Lost [label="not found"];
  Lost -> Search [label="resume scan"];
  Track -> Advance [label="aligned"];
  Track -> Search [label="head reorient"];
  Advance -> Kick [label="within range"];
  Advance -> Track [label="adjust"];
  Kick -> Search [label="resume"];
  Track -> Recover [label="fall"];
  Advance -> Recover [label="fall"];
  Recover -> Boot [label="restore"];
}
''',
}


def render(name: str, dot_source: str) -> None:
    dot_path = ROOT / f"{name}.dot"
    pdf_path = ROOT / f"{name}.pdf"
    jpg_path = ROOT / f"{name}.jpg"
    dot_path.write_text(dot_source, encoding="ascii")
    subprocess.run(
        ["dot", "-Tpdf", str(dot_path), "-o", str(pdf_path)],
        check=True,
    )
    subprocess.run(
        ["dot", "-Tjpg", str(dot_path), "-o", str(jpg_path)],
        check=True,
    )


def main() -> None:
    for name, dot_source in DIAGRAMS.items():
        render(name, dot_source)


if __name__ == "__main__":
    main()
