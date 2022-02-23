#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Menu, messagebox, Toplevel

class AppMenu():
    """程序菜单"""

    def __init__(self, app):
        """初始化"""
        self.app = app  # 上级
        self.root = app.root  # 主程序
        self.init()
        self.root.createcommand('tk::mac::ShowPreferences', self.root.open_about)

    def init(self):
        """创建菜单栏"""
        self.menubar = Menu(self.root)

        # 关于
        # 系统内置菜单：name='apple'，针对 Mac
        m_app = Menu(self.menubar, name='apple')
        m_app.add_command(label='关于 InPanel', command=self.root.open_about)
        m_app.add_command(label='检查更新', command=self.root.open_about)
        m_app.add_separator()

        # 文件下拉菜单
        m_file = Menu(self.menubar, tearoff=0)
        m_file.add_command(label="新建", command=self.file_new)
        m_file.add_command(label="打开", command=self.file_open)
        m_file.add_command(label="保存", command=self.file_save)
        m_file.add_command(label="另存为", command=self.file_save)
        m_file.add_separator()
        m_file.add_command(label="回收站", command=self.file_save)
        m_file.add_command(label="重新登录", command=self.app.open_login)
        m_file.add_command(label="退出", command=self.root.do_quit)

        # 功能菜单
        m_section = Menu(self.menubar, tearoff=0)
        m_section.add_command(label="文件管理", command=self.app.open_user_list)
        m_section.add_command(label="服务管理", command=self.app.open_user_add)
        m_section.add_command(label="网站管理", command=self.app.open_user_info)
        m_section.add_command(label="数据库", command=self.app.open_user_info)
        m_section.add_command(label="应用", command=self.app.open_user_info)

        # 工具菜单
        m_utils = Menu(self.menubar, tearoff=0)
        m_utils.add_command(label="基础设置", command=self.app.open_content_list)
        m_utils.add_command(label="系统管理", command=self.app.open_content_add)
        m_utils.add_command(label="系统安全", command=self.app.open_content_count)
        m_utils.add_command(label="磁盘存储", command=self.app.open_content_count)
        m_utils.add_command(label="磁盘存储", command=self.app.open_content_count)
        m_utils.add_separator()
        m_utils.add_command(label="重启服务器", command=self.app.open_content_count)

        # 设置下拉菜单
        m_config = Menu(self.menubar, tearoff=0)
        m_config.add_command(label="登录设置", command=self.app.open_download)
        m_config.add_command(label="服务设置", command=self.app.open_upload)
        m_config.add_command(label="远程控制", command=self.app.open_synchronize)
        m_config.add_command(label="版本升级", command=self.app.open_backup)
        m_config.add_separator()
        m_config.add_command(label="本地配置", command=self.app.open_backup)

        # 窗口下拉菜单
        # 系统内置菜单：name='window'
        window_menu = Menu(self.menubar, name='window')
        # window_menu.add_command(label="最大化")
        # window_menu.add_command(label="最小化")
        window_menu.add_separator()
        window_menu.add_command(label="窗口置顶", command=self.root.set_to_top)
        window_menu.add_command(label="取消置顶", command=self.root.set_not_top)
        window_menu.add_separator()
        window_menu.add_command(label="主界面", command=self.app.open_home)
        # window_menu.add_command(label="切换到: 用户")
        # window_menu.add_command(label="切换到: 文章列表")

        # 帮助下拉菜单
        # 系统内置菜单：name='help'
        m_help = Menu(self.menubar, tearoff=0, name='help')
        # m_help.add_command(label="欢迎使用", command=self.help_about)
        # m_help.add_command(label="文档", command=self.help_about)
        # m_help.add_command(label="版权声明", command=self.help_about)
        # m_help.add_command(label="隐私声明", command=self.help_about)
        m_help.add_separator()
        m_help.add_command(label="帮助信息", command=self.root.open_win_help)
        m_help.add_command(label="关于", command=self.root.open_about)

        # 将下拉菜单加到菜单栏
        self.menubar.add_cascade(label="InPanel", menu=m_app)
        self.menubar.add_cascade(label="文件", menu=m_file)
        self.menubar.add_cascade(label="功能", menu=m_section)
        self.menubar.add_cascade(label="工具", menu=m_utils)
        self.menubar.add_cascade(label="设置", menu=m_config)
        self.menubar.add_cascade(label='窗口', menu=window_menu) 
        self.menubar.add_cascade(label="帮助", menu=m_help)

        # 变量传递回去
        self.app.menubar = self.menubar

    def file_open(self):
        messagebox.showinfo("打开", "文件-打开！")  # 消息提示框

    def file_new(self):
        messagebox.showinfo("新建", "文件-新建！")  # 消息提示框

    def file_save(self):
        messagebox.showinfo("保存", "文件-保存！")  # 消息提示框

    def edit_cut(self):
        messagebox.showinfo("剪切", "编辑-剪切！")  # 消息提示框

    def edit_copy(self):
        messagebox.showinfo("复制", "编辑-复制！")  # 消息提示框

    def edit_paste(self):
        messagebox.showinfo("粘贴", "编辑-粘贴！")  # 消息提示框

    def help_about(self):
        """关于"""
        messagebox.showinfo(
            "关于", "作者: doudoudzj \n verion 1.0 \n 感谢您的使用！ \n doudoudzj@qq.com"
        )
