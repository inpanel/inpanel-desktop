#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Label, Toplevel
from tkinter.font import Font
from webbrowser import open as url_open

from utils.functions import set_window_center


class WinHelp(Toplevel):
    '''帮助窗口'''

    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.title('帮助信息')
        set_window_center(self, 350, 160)
        # 依附主窗体
        self.transient(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        author_name = Label(self, text='软件：', anchor='e')
        author_text = Label(self, text='InPanel 桌面客户端', anchor='w')

        github_name = Label(self, text='开发者：', anchor='e')
        github_text = Label(self,
                            text='Jackson Dou',
                            anchor='w',
                            fg='blue',
                            cursor='hand',
                            font=Font(underline=True))
        github_text.bind('<Button-1>', self.open_github)

        source_name = Label(self, text='Github：', anchor='e')
        source_text = Label(self,
                            text='https://github.com/inpanel/inpanel',
                            anchor='w',
                            fg='blue',
                            cursor='hand',
                            font=Font(underline=True))
        source_text.bind('<Button-1>', self.open_source)

        site_name = Label(self, text='官方网站：', anchor='e')
        site_text = Label(self,
                          text='https://inpanel.org',
                          anchor='w',
                          fg='blue',
                          cursor='hand',
                          font=Font(underline=True))
        site_text.bind('<Button-1>', self.open_site)

        email_name = Label(self, text='邮箱反馈：', anchor='e')
        email_text = Label(self,
                           text='admin@inpanel.org',
                           anchor='w',
                           fg='blue',
                           cursor='hand',
                           font=Font(underline=True))
        email_text.bind('<Button-1>', self.open_email)

        author_name.grid(row=0, column=0, sticky='nswe')
        author_text.grid(row=0, column=1, sticky='nswe')
        github_name.grid(row=1, column=0, sticky='nswe')
        github_text.grid(row=1, column=1, sticky='nswe')
        source_name.grid(row=2, column=0, sticky='nswe')
        source_text.grid(row=2, column=1, sticky='nswe')
        site_name.grid(row=3, column=0, sticky='nswe')
        site_text.grid(row=3, column=1, sticky='nswe')
        email_name.grid(row=4, column=0, sticky='nswe')
        email_text.grid(row=4, column=1, sticky='nswe')

    def open_github(self, _):
        url_open('https://github.com/doudoudzj')

    def open_source(self, _):
        url_open('https://github.com/inpanel/inpanel')

    def open_site(self, _):
        url_open('https://inpanel.org')

    def open_email(self, _):
        url_open('mailto:admin@inpanel.org')


if __name__ == '__main__':
    app = WinHelp()
    app.mainloop()
