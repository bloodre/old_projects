@ECHO OFF
SET BINDIR=%~dp0

CD /D "%BINDIR%"

"shooter.py"
PAUSE