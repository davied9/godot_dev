@echo off

echo start setup godot_dev venv from %cd%

set GODOT_DEV_ROOT=%cd%
set VENV_ROOT=%GODOT_DEV_ROOT%\\.venv
set PYEXE=%VENV_ROOT%\\Scripts\\python.exe

echo import os, sys; sys.path.append(os.path.join(os.getcwd(), 'scripts', 'py', 'utils')); > %VENV_ROOT%\\godot_dev.pth

%PYEXE% -m pip install --upgrade pip
%PYEXE% -m pip -V
%PYEXE% -m pip install -r %GODOT_DEV_ROOT%\\scripts\\py\\requirements.txt

@echo on
