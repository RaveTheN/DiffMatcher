@echo off
echo DiffMatcher Portable - Dependency Installer
echo ==========================================
echo.
echo This will install optional dependencies for enhanced functionality.
echo.
echo Installing python-docx for Word document support...
pip install python-docx
echo.
if %ERRORLEVEL% EQU 0 (
    echo Dependencies installed successfully!
    echo You can now run DiffMatcher with full Word document support.
) else (
    echo Some dependencies failed to install.
    echo DiffMatcher will still work for text files.
)
echo.
echo To run DiffMatcher:
echo   • Double-click "start_gui.bat" or
echo   • Run "python diff_matcher.py"
echo.
pause
