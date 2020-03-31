# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['inpanel.py'],
             pathex=['.'],
             binaries=[],
             datas=[(os.path.join('.', "data", 'database.db'), 'data')],
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
          console=False )
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
             bundle_identifier=None,
            info_plist={
                'CFBundleName': 'InPanel',
                'CFBundleDisplayName': 'InPanel',
                'CFBundleGetInfoString': "Crogram Inc.",
                'CFBundleIdentifier': "org.inpanel.desktop",
                'CFBundleVersion': "0.0.1",
                'CFBundleShortVersionString': "0.0.1",
                'NSHumanReadableCopyright': "Copyright © 2020, Crogram Inc., All Rights Reserved",
                'NSHighResolutionCapable': 'True'
            })
