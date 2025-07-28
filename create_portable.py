#!/usr/bin/env python3
"""
Create a portable distribution package for DiffMatcher
This creates a complete folder that can be copied to any computer with Python
"""

import os
import shutil
import zipfile
from pathlib import Path

def create_portable_package():
    """Create a portable distribution package"""
    print("📦 Creating portable distribution package...")
    
    # Create distribution directory
    dist_dir = Path("DiffMatcher_Portable")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # Copy main application files
    files_to_copy = [
        "diff_matcher.py",
        "cli_diff_matcher.py",
        "launch_gui.py",
        "start_gui.bat",
        "README.md"
    ]
    
    for file in files_to_copy:
        if Path(file).exists():
            shutil.copy2(file, dist_dir)
            print(f"✅ Copied {file}")
    
    # Create requirements.txt
    requirements_content = """# DiffMatcher Requirements
# Core dependencies (built into Python)
# tkinter - GUI framework (usually included with Python)

# Optional dependencies for enhanced functionality
python-docx>=0.8.11  # For Word document support

# Development dependencies (optional)
# pyinstaller>=4.0  # For building standalone executables
"""
    
    with open(dist_dir / "requirements.txt", "w", encoding='utf-8') as f:
        f.write(requirements_content)
    
    # Create installation script
    install_script = """@echo off
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
"""
    
    with open(dist_dir / "install_dependencies.bat", "w", encoding='utf-8') as f:
        f.write(install_script)
    
    # Create run script for direct execution
    run_script = """@echo off
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
"""
    
    with open(dist_dir / "run_diffmatcher.bat", "w", encoding='utf-8') as f:
        f.write(run_script)
    
    # Create comprehensive README for portable version
    portable_readme = """# DiffMatcher Portable
🚀 **Standalone File Comparison Tool**

## Quick Start
1. **For immediate use** (text files only):
   - Double-click `run_diffmatcher.bat`
   
2. **For full functionality** (including Word documents):
   - Double-click `install_dependencies.bat` (one-time setup)
   - Then run `start_gui.bat`

## What's Included
- ✅ Complete GUI application (`diff_matcher.py`)
- ✅ Command-line interface (`cli_diff_matcher.py`)
- ✅ Smart launcher (`launch_gui.py`)
- ✅ Batch launchers (`.bat` files)
- ✅ Documentation and examples

## Features
- 📄 Compare text files (.txt, .py, .md, etc.)
- 📄 Compare Word documents (.docx) - with python-docx
- 🔍 Line-by-line comparison with similarity percentages
- 📊 Detailed difference reports
- 🎯 Clean, user-friendly GUI interface
- 🔒 Completely local - no network required

## Requirements
- **Python 3.6+** (required)
- **python-docx** (optional, for Word document support)

## Installation Options

### Option 1: Quick Run (Basic functionality)
```bash
python diff_matcher.py
```

### Option 2: Full Installation (All features)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python diff_matcher.py
```

### Option 3: Use Provided Batch Files
- `install_dependencies.bat` - Install optional dependencies
- `run_diffmatcher.bat` - Basic run
- `start_gui.bat` - Run with virtual environment support

## Usage
1. **GUI Mode**: Run any of the launcher scripts or `python diff_matcher.py`
2. **CLI Mode**: `python cli_diff_matcher.py file1.txt file2.txt --verbose`

## Distribution
This portable package can be:
- ✅ Copied to any computer with Python
- ✅ Run without installation
- ✅ Used on air-gapped systems
- ✅ Shared via USB drive or network

## Privacy & Security
- 🔒 **100% Local** - No network connectivity
- 🔒 **No data transmission** - Files never leave your computer
- 🔒 **Read-only access** - Your files are never modified
- 🔒 **No logging** - No persistent data storage

## Support
For issues or questions, refer to the main README.md file.

---
**DiffMatcher** - Secure, Local File Comparison Tool
"""
    
    with open(dist_dir / "README_PORTABLE.md", "w", encoding='utf-8') as f:
        f.write(portable_readme)
    
    # Create ZIP archive
    zip_path = "DiffMatcher_Portable.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(dist_dir.parent)
                zipf.write(file_path, arc_path)
    
    print(f"\n✅ Portable package created successfully!")
    print(f"📁 Folder: {dist_dir}")
    print(f"📦 Archive: {zip_path}")
    print(f"\n🎯 The portable package includes:")
    print(f"   • Complete application with all launchers")
    print(f"   • Installation scripts for dependencies")
    print(f"   • Comprehensive documentation")
    print(f"   • Ready to copy to any Windows computer")

if __name__ == "__main__":
    create_portable_package()
