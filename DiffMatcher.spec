# -*- mode: python ; coding: utf-8 -*-

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
