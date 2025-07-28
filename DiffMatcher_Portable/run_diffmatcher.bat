@echo off
echo Starting DiffMatcher...
python diff_matcher.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error: Python might not be installed or not in PATH
    echo.
    echo Please ensure Python is installed and try again.
    echo You can download Python from: https://python.org
    echo.
    pause
)
