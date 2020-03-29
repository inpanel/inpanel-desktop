# -*- coding: utf-8 -*-


def set_window_center(window, width, height):
    '''窗口居中显示'''
    # 获取屏幕 宽、高
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
