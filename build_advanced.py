#!/usr/bin/env python3
"""
Advanced build script for DiffMatcher with full Word document support
Creates a PyInstaller spec file for better control over the build process
"""

import subprocess
import sys
import os
from pathlib import Path

def create_spec_file():
    """Create a custom PyInstaller spec file with all necessary imports"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Check if python-docx is available
try:
    import docx
    DOCX_AVAILABLE = True
    docx_hiddenimports = [
        'docx',
        'docx.document',
        'docx.shared',
        'docx.oxml',
        'docx.oxml.ns',
        'docx.text.paragraph',
        'docx.table',
        'docx.section',
        'lxml',
        'lxml.etree',
        'lxml._elementpath',
        'lxml.objectify',
    ]
except ImportError:
    DOCX_AVAILABLE = False
    docx_hiddenimports = []

a = Analysis(
    ['diff_matcher.py'],
    pathex=[],
    binaries=[],
    datas=[('README.md', '.')],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.scrolledtext',
        'difflib',
        'pathlib',
    ] + docx_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DiffMatcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
'''
    
    with open("DiffMatcher.spec", "w", encoding='utf-8') as f:
        f.write(spec_content)
    
    print("📄 Created DiffMatcher.spec file")
    return True

def install_dependencies():
    """Install all required dependencies"""
    dependencies = ["pyinstaller"]
    
    # Try to install python-docx for Word support
    try:
        import docx
        print("✅ python-docx is already installed")
        docx_available = True
    except ImportError:
        print("📦 Installing python-docx for Word document support...")
        dependencies.append("python-docx")
        docx_available = False
    
    for dep in dependencies:
        try:
            if dep == "pyinstaller":
                import PyInstaller
                print(f"✅ {dep} is already installed")
            elif dep == "python-docx" and not docx_available:
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
                print(f"✅ {dep} installed successfully")
        except ImportError:
            print(f"📦 Installing {dep}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
                print(f"✅ {dep} installed successfully")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install {dep}: {e}")
                if dep == "python-docx":
                    print("⚠️ Continuing without Word document support")
                else:
                    return False
    
    return True

def build_with_spec():
    """Build the executable using the spec file"""
    if not install_dependencies():
        return False
    
    if not create_spec_file():
        return False
    
    print("🔨 Building standalone executable with full Word support...")
    
    try:
        # Build using the spec file
        cmd = [sys.executable, "-m", "PyInstaller", "DiffMatcher.spec", "--clean"]
        subprocess.check_call(cmd)
        
        print("✅ Executable built successfully!")
        print("📁 Location: dist/DiffMatcher.exe")
        
        # Check if python-docx was included
        try:
            import docx
            print("\n🎯 The executable includes:")
            print("   • Complete GUI application")
            print("   • ✅ Full Word document support (.docx files)")
            print("   • All required dependencies bundled")
            print("   • Optimized with UPX compression")
            print("   • No Python installation required on target machine")
        except ImportError:
            print("\n🎯 The executable includes:")
            print("   • Complete GUI application")
            print("   • ❌ Word document support not available")
            print("   • Text file comparison only")
            print("   • No Python installation required on target machine")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to build executable: {e}")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller not found. Please install it manually:")
        print("   pip install pyinstaller")
        return False

def test_executable():
    """Test the built executable"""
    exe_path = Path("dist/DiffMatcher.exe")
    if exe_path.exists():
        file_size = exe_path.stat().st_size / (1024 * 1024)  # Size in MB
        print(f"\n📊 Executable Information:")
        print(f"   • File size: {file_size:.1f} MB")
        print(f"   • Location: {exe_path.absolute()}")
        
        # Check if we can determine Word support
        try:
            import docx
            print(f"   • Word support: ✅ Included (python-docx bundled)")
        except ImportError:
            print(f"   • Word support: ❌ Not included")
        
        print(f"\n🚀 Ready for distribution!")
        return True
    else:
        print("❌ Executable not found!")
        return False

if __name__ == "__main__":
    print("🚀 DiffMatcher Advanced Executable Builder")
    print("=" * 50)
    print("📋 This script will create a standalone .exe with full Word support")
    print()
    
    if build_with_spec():
        test_executable()
        print("\n🎉 Build process completed successfully!")
        print("\n📋 Next steps:")
        print("1. Test the executable: dist/DiffMatcher.exe")
        print("2. Try comparing .docx files to verify Word support")
        print("3. Distribute to any Windows computer - no Python needed!")
    else:
        print("\n❌ Build failed. Please check the error messages above.")
