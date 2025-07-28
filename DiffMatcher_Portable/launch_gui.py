#!/usr/bin/env python3
"""
DiffMatcher GUI Launcher
Automatically detects and uses the correct Python environment for Word document support
"""

import sys
import subprocess
from pathlib import Path
import os

def find_python_with_docx():
    """Find a Python executable that has python-docx installed"""
    
    # Check current Python
    try:
        import docx
        print("✅ Current Python has python-docx support")
        return sys.executable
    except ImportError:
        pass
    
    # Check virtual environment
    venv_python = Path(".venv/Scripts/python.exe")
    if venv_python.exists():
        try:
            result = subprocess.run([str(venv_python), "-c", "import docx; print('OK')"], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print("✅ Virtual environment Python has python-docx support")
                return str(venv_python)
        except (subprocess.TimeoutExpired, subprocess.SubprocessError):
            pass
    
    # Fallback to current Python (will show warning in GUI)
    print("⚠️ python-docx not found in any Python environment")
    print("   GUI will start but Word document support will be disabled")
    return sys.executable

def main():
    """Launch the DiffMatcher GUI"""
    print("🚀 DiffMatcher GUI Launcher")
    print("=" * 40)
    
    # Find appropriate Python executable
    python_exe = find_python_with_docx()
    
    # Launch the GUI
    gui_script = Path("diff_matcher.py")
    if not gui_script.exists():
        print("❌ Error: diff_matcher.py not found in current directory")
        print("   Please run this script from the DiffMatcher project directory")
        sys.exit(1)
    
    print(f"🎯 Launching GUI with: {python_exe}")
    print("   Loading DiffMatcher...")
    
    try:
        # Launch the GUI application
        subprocess.run([python_exe, str(gui_script)], check=True)
        print("✅ DiffMatcher GUI closed normally")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching GUI: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️ GUI launch interrupted by user")
        sys.exit(1)

if __name__ == "__main__":
    main()
