# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

datas=[
    (os.path.join('src', 'data', 'database.db'), 'data'),
    (os.path.join('src', 'data', 'image', 'logo_about.png'), 'data/image')
]

APP_ID = 'org.inpanel.client.desktop'
APP_APP = 'InPanel.app'
APP_VERSION = '0.0.1'
APP_NAME = 'InPanel'
APP_NAME_DISPLAY = 'InPanel 桌面客户端'


a = Analysis(['src/app.py'],
    pathex=['src'],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None)
coll = COLLECT(exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME)
app = BUNDLE(
    coll,
    name=APP_APP,
    icon='resources/app.icns',
    bundle_identifier=APP_ID,
    info_plist={
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME_DISPLAY,
        'CFBundleGetInfoString': "Crogram Inc.",
        'CFBundleIdentifier': APP_ID,
        'CFBundleVersion': APP_VERSION,
        'CFBundleShortVersionString': APP_VERSION,
        'CFBundleInfoDictionaryVersion': APP_VERSION,
        'CFBundlePackageType': 'APPL',
        'CFBundleSupportedPlatforms': ['MacOSX'],
        'LSMinimumSystemVersion': '11.0', # 最低系统版本
        'NSHumanReadableCopyright': "Copyright © 2018-2022 Crogram Inc. All Rights Reserved.",
        'NSHighResolutionCapable': True,
        'LSApplicationCategoryType': 'public.app-category.utilities'
    })
