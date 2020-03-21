@echo off

echo start setup godot_dev env from %cd%

set GODOT_DEV_ROOT=%cd%

python %GODOT_DEV_ROOT%/scripts/py/init.py

@echo on
