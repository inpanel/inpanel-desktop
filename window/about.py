#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from webbrowser import open
from tkinter import (Label, Toplevel, PhotoImage)

import utils.global_variable as glv
from utils.functions import set_window_center

class WinAbout(Toplevel):
    """关于窗口"""

    def __init__(self):
        Toplevel.__init__(self)
        self.title("关于")
        set_window_center(self, 300, 220)
        self.app_name = glv.get_item('APP_DISPLAY_NAME')
        # self.app_name = 'InPanel 桌面客户端'
        self.app_version = '版本: %s' % glv.get_item('APP_VERSION')
        # self.app_version = '版本:0.0.1'
        self.img = os.path.join(
            glv.get_item("APP_PATH"),
            glv.get_item("DATA_DIR"),
            'image',
            'logo_about.png'
        )
        self.logo = PhotoImage(width=64, height=64, file=self.img)

        """加载控件"""
        Label(self, image=self.logo, width=64, height=80).pack()
        Label(self, text=self.app_name, font=('Arial', 15, 'bold')).pack()
        Label(self, text=self.app_version, font=(None, 13)).pack()
        site = Label(self, text='官方网站', pady=10, cursor='hand', highlightcolor='blue')
        site.bind("<Button-1>", self.open_site)
        site.pack()
        Label(self, text='Copyright © 2018-2022 Crogram Inc.', font=(None, 10)).pack()
        Label(self, text='All rights reserved.', font=(None, 10)).pack()

    # 此处必须注意，绑定的事件函数中必须要包含event参数
    def open_site(self, event):
        app_site = glv.get_item('APP_SITE')
        # app_site = "https://inpanel.org"
        open(app_site, new=0)


if __name__ == "__main__":
    APP_ABOUT = WinAbout()
    APP_ABOUT.mainloop()
