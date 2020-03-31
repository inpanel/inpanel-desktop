#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""程序入口文件"""

from os.path import dirname

import lib.global_variable as g
from frames import App
# from window import WinSplah

# 全局变量
g.init_global_variable()
g.set_variable("APP_NAME", "InPanel")
g.set_variable("APP_PATH", dirname(__file__))  # 当前目录
g.set_variable("DATA_DIR", "data")

if __name__ == "__main__":
    # WinSplah()
    App()
