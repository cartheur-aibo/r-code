//------------------------------------------
//  MAZE
//------------------------------------------
:1000

PLAY:ACTION:STAND
WAIT
PLAY:ACTION:CLIFF_DETECT_OFF
WAIT

DO
  PLAY:ACTION:MOVE_HEAD:0:0
  WAIT
  
  PLAY:ACTION:WALK:0:10000
	
  FOR:t:1:1000
    IF:Distance:<:300:BREAK  // If AIBO finds a wall or t=1000 then break
    WAIT:1
  NEXT

  PLAY:ACTION:STOP_WALK
  WAIT

  PLAY:ACTION:MOVE_HEAD:90:0
  WAIT
  PLAY:ACTION:MOVE_HEAD:-90:0
  SET:dd:0
  WHILE:Wait:>:0
    SET:d:Distance
    SET:p:Head_Pan
    IF:d:>:dd:THEN
      SET:dd:d
      SET:pan:p
    ENDIF
  WEND

  VDUMP:dd
  VDUMP:pan

  IF:dd:<:300:THEN           // No where to go (turn 180)
   PLAY:ACTION:TURN:180
   WAIT
  ENDIF

  PLAY:ACTION:MOVE_HEAD:pan:0
  PLAY:ACTION:TURN:pan
  WAIT

LOOP

