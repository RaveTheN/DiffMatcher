@echo off
REM DiffMatcher GUI Launcher with Word Document Support
REM This script launches the GUI using the virtual environment where python-docx is installed

echo Starting DiffMatcher GUI with Word Document Support...
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\python.exe" (
    echo Error: Virtual environment not found!
    echo Please run the following commands first:
    echo   python -m venv .venv
    echo   .venv\Scripts\activate
    echo   pip install python-docx
    echo.
    pause
    exit /b 1
)

REM Launch GUI with virtual environment Python
".venv\Scripts\python.exe" diff_matcher.py

echo.
echo DiffMatcher GUI closed.
pause
