# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

datas=[
    (os.path.join('src', 'data', 'database.db'), 'data'),
    (os.path.join('src', 'data', 'image', 'logo_about.png'), 'data/image')
]

a = Analysis(['src/inpanel.py'],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='InPanel',
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
               name='InPanel')
app = BUNDLE(coll,
             name='InPanel.app',
             icon='resources/app.icns',
             bundle_identifier='org.inpanel.client.desktop',
            info_plist={
                'CFBundleName': 'InPanel',
                'CFBundleDisplayName': 'InPanel桌面客户端',
                'CFBundleGetInfoString': "Crogram Inc.",
                'CFBundleIdentifier': "org.inpanel.client.desktop",
                'CFBundleVersion': "0.0.1",
                'CFBundleShortVersionString': "0.0.1",
                'NSHumanReadableCopyright': "Copyright © 2018-2022 Crogram Inc. All Rights Reserved.",
                'NSHighResolutionCapable': 'True'
            })
