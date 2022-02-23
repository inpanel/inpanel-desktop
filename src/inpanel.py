#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''程序入口文件'''

from os.path import dirname

import utils.global_variable as g
from app import App

# from window import WinSplah

# 全局变量
g.init()
g.set_item('APP_NAME', 'InPanel')
g.set_item('APP_BOUNDLE_ID', 'org.inpanel.client.desktop')
g.set_item('APP_DISPLAY_NAME', 'InPanel 桌面客户端')
g.set_item('APP_VERSION', '0.0.1')
g.set_item('APP_COPYRIGHT', 'Copyright © 2018-2022 Crogram Inc.')
g.set_item('APP_PATH', dirname(__file__))  # 当前目录
g.set_item('DATA_DIR', 'data')
g.set_item('APP_SITE', 'https://inpanel.org?utm_source=client_desktop&client_version=0.0.1')

if __name__ == '__main__':
    # WinSplah()
    App()
