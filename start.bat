@echo off
REM on-metacraft reader - mirrors sisters
py -3 tools\build_site.py
py -3 -m http.server 11026 --bind 127.0.0.1 --directory site
