@echo off
REM DiffMatcher Launcher Script
REM This script provides easy access to DiffMatcher tools

:menu
echo.
echo =============================================
echo        DiffMatcher Tool Launcher v2.1
echo          (Now with Word Document Support!)
echo =============================================
echo.
echo 1. Launch GUI Application (Auto-detect best Python)
echo 2. Launch GUI with Word Support (Virtual Environment)
echo 3. Run CLI with sample files
echo 4. Run CLI help
echo 5. Run tests
echo 6. Test GUI functionality
echo 7. Test file dialog
echo 8. Word Document Demo
echo 9. Exit
echo.
set /p choice="Enter your choice (1-9): "

if "%choice%"=="1" goto gui_auto
if "%choice%"=="2" goto gui_venv
if "%choice%"=="3" goto cli_sample
if "%choice%"=="4" goto cli_help
if "%choice%"=="5" goto test
if "%choice%"=="6" goto test_gui
if "%choice%"=="7" goto test_dialog
if "%choice%"=="8" goto word_demo
if "%choice%"=="9" goto exit

echo Invalid choice. Please try again.
goto menu

:gui_auto
echo.
echo Launching GUI with auto-detection...
python launch_gui.py
goto menu

:gui_venv
echo.
echo Launching GUI with Word support...
call start_gui.bat
goto menu

:cli_sample
echo.
echo Running CLI with sample files...
python cli_diff_matcher.py --sample
pause
goto menu

:cli_help
echo.
echo Showing CLI help...
python cli_diff_matcher.py --help
pause
goto menu

:test
echo.
echo Running all tests...
python test_diff_matcher.py
pause
goto menu

:test_gui
echo.
echo Testing GUI functionality...
python test_gui.py
pause
goto menu

:test_dialog
echo.
echo Testing file dialog...
python test_file_dialog.py
pause
goto menu

:word_demo
echo.
echo Running Word Document Demo...
python word_demo.py
pause
goto menu

:exit
echo.
echo Goodbye!
exit /b 0
