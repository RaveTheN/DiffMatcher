#!/usr/bin/env python3
"""
Build script to create a standalone executable for DiffMatcher
Uses PyInstaller to package the application into a single .exe file
"""

import subprocess
import sys
import os
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✅ PyInstaller is already installed")
        return True
    except ImportError:
        print("📦 Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install PyInstaller: {e}")
            return False

def check_and_install_docx():
    """Check if python-docx is available and install if needed"""
    try:
        import docx
        print("✅ python-docx is available")
        return True
    except ImportError:
        print("📦 Installing python-docx for Word document support...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
            print("✅ python-docx installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Failed to install python-docx: {e}")
            print("⚠️ Executable will be built without Word document support")
            return False

def build_executable():
    """Build the standalone executable"""
    if not install_pyinstaller():
        return False
    
    # Check and install python-docx for full functionality
    docx_available = check_and_install_docx()
    
    print("🔨 Building standalone executable...")
    
    # PyInstaller command to create a single executable file
    cmd = [
        sys.executable, "-m", "PyInstaller",  # Use Python module approach
        "--onefile",                    # Create a single executable file
        "--windowed",                   # No console window (GUI only)
        "--name=DiffMatcher",          # Name of the executable
        "--add-data=README.md;.",      # Include README
        "diff_matcher.py"              # Main script
    ]
    
    # Add python-docx as a hidden import if available
    if docx_available:
        cmd.extend([
            "--hidden-import=docx",
            "--hidden-import=docx.document",
            "--hidden-import=docx.shared",
            "--hidden-import=docx.oxml",
            "--hidden-import=docx.oxml.ns",
            "--hidden-import=docx.text.paragraph",
            "--hidden-import=lxml",
            "--hidden-import=lxml.etree",
        ])
    
    # Add icon parameter if icon file exists
    if Path("icon.ico").exists():
        cmd.insert(-1, "--icon=icon.ico")
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable built successfully!")
        print("📁 Location: dist/DiffMatcher.exe")
        print("\n🎯 The executable includes:")
        print("   • Complete GUI application")
        if docx_available:
            print("   • ✅ Word document support (python-docx included)")
        else:
            print("   • ❌ Word document support (python-docx not available)")
        print("   • All dependencies bundled")
        print("   • No Python installation required on target machine")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to build executable: {e}")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller not found. Please install it manually:")
        print("   pip install pyinstaller")
        return False

def create_installer_script():
    """Create a simple installer script"""
    installer_content = '''@echo off
echo DiffMatcher Installer
echo ====================
echo.
echo This will copy DiffMatcher.exe to your Programs folder
echo and create a desktop shortcut.
echo.
pause

set INSTALL_DIR=%PROGRAMFILES%\\DiffMatcher
set DESKTOP=%USERPROFILE%\\Desktop

echo Creating installation directory...
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

echo Copying executable...
copy "DiffMatcher.exe" "%INSTALL_DIR%\\"

echo Creating desktop shortcut...
echo Set oWS = WScript.CreateObject("WScript.Shell") > createshortcut.vbs
echo sLinkFile = "%DESKTOP%\\DiffMatcher.lnk" >> createshortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> createshortcut.vbs
echo oLink.TargetPath = "%INSTALL_DIR%\\DiffMatcher.exe" >> createshortcut.vbs
echo oLink.WorkingDirectory = "%INSTALL_DIR%" >> createshortcut.vbs
echo oLink.Description = "DiffMatcher - File Comparison Tool" >> createshortcut.vbs
echo oLink.Save >> createshortcut.vbs

cscript createshortcut.vbs
del createshortcut.vbs

echo.
echo Installation complete!
echo Desktop shortcut created
echo Program installed to: %INSTALL_DIR%
echo.
pause
'''
    
    with open("installer.bat", "w", encoding='utf-8') as f:
        f.write(installer_content)
    
    print("📄 Created installer.bat for easy installation")

if __name__ == "__main__":
    print("🚀 DiffMatcher Executable Builder")
    print("=" * 40)
    
    if build_executable():
        create_installer_script()
        print("\n🎉 Build process completed!")
        print("\n📋 Next steps:")
        print("1. Run 'installer.bat' to install on this machine")
        print("2. Or copy 'dist/DiffMatcher.exe' to any Windows computer")
        print("3. Double-click to run - no Python required!")
    else:
        print("\n❌ Build failed. Please check the error messages above.")
