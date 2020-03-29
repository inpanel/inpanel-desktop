#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# import tkinter as tk
from tkinter import Tk, Label, BOTH
from lib import set_window_center

window = Tk()
window.title('InPanel Desktop')

label = Label(window, text="Hello, World")
label.pack(fill=BOTH, expand=1)

set_window_center(window, 800, 500)

window.mainloop()
