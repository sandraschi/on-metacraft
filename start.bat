@echo off
REM on-metacraft reader - proper launcher (build + serve :11026 in its own window)
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -File "%~dp0start.ps1"

