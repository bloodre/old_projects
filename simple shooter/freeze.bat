@ECHO OFF
SET BINDIR=%~dp0

CD /D "%BINDIR%"

 "setup.py" build
PAUSE