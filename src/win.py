#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os.path
import tkinter as gui
from tkinter import Canvas, Label, Tk

import utils.global_variable as gv
from utils.functions import set_window_center


class WinSplah(Tk):
    """初始化启动屏幕窗口"""

    def __init__(self):
        Tk.__init__(self)
        self.title("程序加载中")
        self.w = 300
        self.h = 300
        set_window_center(self, self.w, self.h)
        # self.resizable(False, False)
        self.splash()

    def splash(self):
        """启动屏幕"""
        image_file = os.path.join(
            gv.get("APP_PATH"),
            gv.get("DATA_DIR"),
            "image",
            "splash.jpg",
        )
        canvas = Canvas(self, width=self.w, height=250, bg="white")
        # if os.path.exists(image_file):
        #     img = Image.open(image_file)  # 打开图片
        #     image = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
        #     canvas.create_image(self.w / 2, 250 / 2, image=image)
        # else:
        canvas.create_text(
            self.w / 2, 250 / 2, text="Crogram, Inc.", font="time 20", tags="string"
        )

        canvas.pack(fill="both")
        Label(self, text="欢迎使用", bg="green", fg="#fff", height=2).pack(
            fill="both", side="bottom"
        )

        # 设置splash显示的时间，单位是毫秒（milliseconds）
        self.after(4000, self.destroy)
        self.mainloop()


class WinUserEdit(gui.Toplevel):
    """用户编辑窗口"""

    def __init__(self, user_info=None):
        gui.Toplevel.__init__(self)
        self.current = user_info
        self.win_title = "用户编辑"
        self.title(self.win_title)
        set_window_center(self, 250, 250)
        self.resizable(False, False)
        self.init_page()

    def init_page(self):
        """加载控件"""
        gui.Label(self, text="title").pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Label(self, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(self, text=self.current, width=150)
        msg.pack()
        # gui.Label(self, text="你好你好你好你好").grid()
        # gui.Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()


class WinUserInfo(gui.Toplevel):
    """用户详情窗口"""

    def __init__(self, user_info=None):
        gui.Toplevel.__init__(self)
        self.current = user_info
        self.win_title = "用户详情"
        self.title(self.win_title)
        set_window_center(self, 200, 300)
        self.resizable(False, False)
        self.init_page()

    def init_page(self):
        """加载控件"""
        gui.Label(self, text="title").pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Label(self, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(self, text=self.current, width=150)
        msg.pack()
        # gui.Label(self, text="你好你好你好你好").grid()
        # gui.Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()


class WinContentInfo(gui.Toplevel):
    """文章详情窗口"""

    def __init__(self, info=None):
        gui.Toplevel.__init__(self)
        self.current_content = info
        self.win_title = "内容详情《" + \
            (self.current_content["values"][1] or "[暂无标题]") + "》"
        self.title(self.win_title)
        set_window_center(self, 400, 500)
        self.resizable(False, False)
        self.init_page()

    def init_page(self):
        """加载控件"""
        gui.Label(self, text="title").pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Label(self, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(self, text=self.current_content, width=150)
        msg.pack()
        # gui.Label(self, text="你好你好你好你好").grid()
        # gui.Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()


class WinContentEdit(gui.Toplevel):
    """内容编辑窗口"""

    def __init__(self, info=None):
        gui.Toplevel.__init__(self)
        self.current_content = info
        self.win_title = "内容编辑《" + self.current_content["values"][1] + "》"
        self.title(self.win_title)
        set_window_center(self, 400, 500)
        self.resizable(False, False)
        self.init_page()

    def init_page(self):
        """加载控件"""
        gui.Label(self, text="title").pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Label(self, text="你好你好你好你好")
        msg.pack(expand=gui.YES, fill=gui.BOTH)
        msg = gui.Message(self, text=self.current_content, width=150)
        msg.pack()
        # gui.Label(self, text="你好你好你好你好").grid()
        # gui.Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()

if __name__ == "__main__":
    # test
    APP_ABOUT = WinContentEdit()
    APP_ABOUT.mainloop()
