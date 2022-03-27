#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import join
from tkinter import Label, PhotoImage, Toplevel
from tkinter.font import Font
from webbrowser import open as url_open

import utils.global_variable as gv
from utils.functions import set_window_center


class WinAbout(Toplevel):
    '''关于窗口'''

    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.title('关于')
        # 依附主窗体
        self.transient(master)
        # 设置大小位置
        set_window_center(self, 400, 200)
        self.configure(padx=10, pady=10)

        self.img = join(gv.get('APP_PATH'), gv.get('DATA_DIR'),
                        'image', 'logo_about.png')
        self.logo = PhotoImage(width=128, height=128, file=self.img)

        Label(self, image=self.logo, width=150, height=128).pack(side='left')

        Label(self,
              text=gv.get('APP_NAME_DISPLAY'),
              height=3,
              font=Font(size=15, weight='bold')).pack()

        Label(self,
              text='版本: %s' % gv.get('APP_VERSION'),
              font=Font(size=13)).pack()
        Label(self, text='', pady=1).pack()

        site = Label(self,
                     text='官方网站',
                     cursor='hand',
                     font=Font(size=11, underline=True))
        site.bind('<Button-1>', self.open_site)
        site.pack()

        Label(self, text=gv.get('APP_COPYRIGHT2'),
              font=Font(size=10)).pack()
        Label(self, text='All rights reserved.', font=Font(size=10)).pack()

    def open_site(self, _):
        url_open(gv.get('APP_SITE'), new=0)


if __name__ == '__main__':
    app = WinAbout()
    app.mainloop()
