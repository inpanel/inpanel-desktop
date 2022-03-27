#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import dirname
from tkinter import (Button, Entry, Frame, Label, LabelFrame, Menu, Message,
                     Scrollbar, StringVar, Tk, Toplevel, messagebox,
                     scrolledtext)
# from tkinter.ttk import Frame as tFrame
from tkinter.ttk import LabelFrame, Notebook, Scrollbar, Style, Treeview

import utils.dbcontent as dbcontent
from menu import AppMenu
from utils import global_variable as gv
from utils.functions import set_window_center, treeview_sort_column
from win import WinContentEdit, WinContentInfo, WinUserEdit, WinUserInfo
from window.about import WinAbout
from window.help import WinHelp

# 全局变量
gv.init()
gv.set('APP_NAME', 'InPanel')
gv.set('APP_ID', 'org.inpanel.client.desktop')
gv.set('APP_NAME_DISPLAY', 'InPanel 桌面客户端')
gv.set('APP_VERSION', '0.0.1')
gv.set('APP_COPYRIGHT', 'Copyright © 2018-2022 Crogram Inc. All Rights Reserved.')
gv.set('APP_COPYRIGHT2', 'Copyright © 2018-2022 Crogram Inc.')
gv.set('APP_PATH', dirname(__file__))  # 当前目录
gv.set('DATA_DIR', 'data')
gv.set('APP_SITE', 'https://inpanel.org?utm_source=client_desktop&client_version=0.0.1')


class App(Tk):
    '''
    App

    应用程序主窗体，所有窗口、组件的根级窗口
    '''

    def __init__(self):
        Tk.__init__(self)
        if not self.is_login():
            # 登录窗口
            ViewMain(self)
            # PageLogin(self)
        else:
            ViewMain(self)

        self.win_about = None
        self.win_help = None
        self.mainloop()

    def do_quit(self):
        """退出主程序"""
        self.quit()

    def is_login(self):
        """是否已登陆"""
        return gv.has("CURRENT_USER_NAME")

    def do_logout(self):
        """退出登陆"""
        return gv.remove("CURRENT_USER_NAME")

    def set_to_top(self):
        """窗口置顶"""
        self.attributes("-topmost", True)

    def set_not_top(self):
        """窗口置顶取消"""
        self.attributes("-topmost", False)

    def open_about(self):
        """打开关于窗口"""
        if self.win_about and self.win_about.destroy:
            try:
                self.win_about.lift()
            except:
                # 打开异常：销毁、新建
                self.win_about.destroy()
                self.win_about = WinAbout(self)
        else:
            self.win_about = WinAbout(self)

    def open_win_help(self):
        """打开帮助窗口"""
        if self.win_help and self.win_help.destroy:
            try:
                self.win_help.lift()
            except:
                # 打开异常：销毁、新建
                self.win_help.destroy()
                self.win_help = WinHelp(self)
        else:
            self.win_help = WinHelp(self)


class ViewMain:
    """主界面"""

    def __init__(self, parent=None):
        set_window_center(parent, 900, 600, resize=True)
        # 初始化主窗口
        self.root = parent  # 程序主窗口
        self.menubar = None  # 程序菜单
        self.page_sidebar = None  # 主界面导航菜单
        self.page_current = None  # 主界面内容

        self.init_menu()
        self.init_sidebar()
        self.pages = {
            "login": PageLogin,
            "home": PageHome,
            "settings": PageSettings,
            "contact": PageContact,
            "content_add": ContentAdd,
            "content_list": ContentList,
            "count": CountFrame,
            "user_list": UserListFrame,
            "user_add": UserAddFrame
        }
        self.open_page("home")

    def init_menu(self):
        # 定义给 self.menubar
        AppMenu(self)
        # 将菜单栏添加到窗口
        self.root.config(menu=self.menubar)

    def init_sidebar(self):
        """导航菜单界面"""
        # 定义给 self.page_sidebar
        ViewSidebar(self)
        self.page_sidebar.pack(side="left", fill="y", anchor="center")

    def open_page(self, frame_name):
        """打开/更换主界面的通用函数"""
        # 先销毁之前frame
        if self.page_current is not None and (hasattr(
                self.page_current.destroy, "__call__")):
            self.page_current.destroy()

        self.page_current = self.pages[frame_name](self.root)
        self.page_current.pack(side="left", fill="both", anchor="center")

    def open_home(self):
        """应用主界面"""
        self.open_page("home")

    def open_login(self):
        """登录界面"""
        self.page_sidebar.destroy()
        self.page_current.destroy()
        self.root.do_logout()
        self.open_page("login")

    def open_settings(self):
        """服务管理"""
        self.open_page("settings")

    def open_content_add(self):
        """文章添加"""
        self.open_page("content_add")

    def open_content_list(self):
        """文章列表"""
        self.open_page("content_list")

    def open_content_count(self):
        """文章统计"""
        self.open_page("count")

    def open_ontact(self):
        """联系我们"""
        self.open_page("contact")

    def open_user_info(self):
        """用户详情"""
        page = Toplevel()
        page.title("用户详情")
        page.resizable(False, False)
        set_window_center(page, 200, 150)

        # Label(page).grid(row=0, stick="w", pady=2)

        Label(page, text="姓名: ").grid(row=1, stick="w", pady=2)
        Label(page, text="管理员").grid(row=1, column=1, stick="e")

        Label(page, text="账户: ").grid(row=2, stick="w", pady=2)
        Label(page, text="admin").grid(row=2, column=1, stick="e")

        Label(page, text="密码: ").grid(row=3, stick="w", pady=2)
        Label(page, text="admin").grid(row=3, column=1, stick="e")

    def open_user_list(self):
        """用户列表"""
        self.open_page("user_list", "用户列表")
        # self.pages["user_list"].init_data()

    def open_user_add(self):
        """用户添加"""
        self.open_page("user_add", "用户添加")

    def open_download(self):
        """下载窗口"""
        root = Toplevel()
        root.title("下载管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_upload(self):
        """上传管理"""
        root = Toplevel()
        root.title("上传管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_synchronize(self):
        """同步管理"""
        root = Toplevel()
        root.title("同步管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()

    def open_backup(self):
        """备份管理"""
        root = Toplevel()
        root.title("备份管理")
        set_window_center(root, 400, 400)
        msg = Label(root, text="你好你好你好你好")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="类似于弹出窗口，具有独立的窗口属性。", width=150)
        msg.pack()


class ViewSidebar:
    """主界面导航菜单"""

    def __init__(self, parent=None):
        self.parent = parent
        self.root = parent.root
        self.bg = "#00b75b"
        self.bga = "#147b3d"
        self.init()

    def init(self):
        self.parent.page_sidebar = Frame(self.root, bg=self.bg)

        Label(self.parent.page_sidebar,
              text="InPanel",
              width=15,
              height=3,
              padx=20,
              bg="#279e56",
              foreground="blue").pack(side="top")

        # 可以使用管理每个视图的参数
        # self.parent.pages[0].title
        # self.parent.pages[0].page
        # self.parent.pages[0].open
        nav = ("主界面", "服务管理", "文件管理", "数据库", "插件", "工具", "设置")
        self.navs = []
        for index, item in enumerate(nav):
            i = Label(self.parent.page_sidebar,
                      text=item,
                      width=15,
                      height=3,
                      padx=20)
            i["bg"] = self.bg
            i["fg"] = "#ffffff"
            if index == 6:
                i.pack(side="bottom")
            else:
                i.pack()
            self.navs.append(i)
            self.bind_mouse(i)
        self.navs[0].bind("<Button-1>", lambda event: self.parent.open_home())
        self.navs[1].bind("<Button-1>",
                          lambda event: self.parent.open_ontact())
        self.navs[3].bind("<Button-1>",
                          lambda event: self.parent.open_ontact())
        self.navs[1].bind("<Button-1>",
                          lambda event: self.parent.open_ontact())
        self.navs[1].bind("<Button-1>",
                          lambda event: self.parent.open_ontact())
        self.navs[1].bind("<Button-1>",
                          lambda event: self.parent.open_ontact())
        self.navs[6].bind("<Button-1>",
                          lambda event: self.parent.open_settings())

    def bind_mouse(self, widget):

        def enter(event):
            widget["bg"] = self.bga

        def leave(event):
            widget["bg"] = self.bg

        # def click(event):
        #     widget.open_page()
        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)
        # widget.bind("<Button-1>", click)


class PageLogin:
    """登录界面"""

    def __init__(self, parent=None):
        parent.title("登陆")
        set_window_center(parent, 300, 200)
        # 定义当前本地变量
        self.root = parent
        self.username = StringVar(value="")
        self.password = StringVar(value="")
        self.init_menu()
        self.init_page()

    def init_page(self):
        """登录界面"""
        # 左侧空白
        # self.blank_top = Label(self.root)
        # self.blank_top.pack(side="top", fill="both", expand="yes")
        # # 左侧空白
        # self.blank_left = Label(self.root)
        # self.blank_left.pack(side="left", fill="both", expand="yes")
        # # 右侧空白
        # self.blank_right = Label(self.root)
        # self.blank_right.pack(side="right", fill="both", expand="yes")
        # # 右侧空白
        # self.blank_bottom = Label(self.root)
        # self.blank_bottom.pack(side="bottom", fill="both", expand="yes")
        # 中间功能区域
        self.page = Frame(self.root, background="#ffffff", width=100)
        self.page.pack(side="top", fill="both", anchor="center", expand="yes")
        # 头部空白
        Label(self.page).grid(row=0, column=0, sticky="ew")
        # 账户
        Label(self.page, text="账户: ").grid(row=1, column=1, stick="W", pady=10)
        username = Entry(self.page, textvariable=self.username)
        username.grid(row=1, column=2, stick="E")
        username.bind("<Return>", self.return_envent)
        # 密码
        Label(self.page, text="密码: ").grid(row=2, column=1, stick="W", pady=10)
        password = Entry(self.page, textvariable=self.password, show="*")
        password.grid(row=2, column=2, stick="E")
        password.bind("<Return>", self.return_envent)
        # 登陆按钮
        button_login = Button(self.page,
                              text="登陆",
                              command=self.do_login,
                              background="#ffffff")
        button_login.grid(row=3, column=2, stick="W", pady=10)
        # 退出按钮
        button_cancel = Button(self.page,
                               text="退出",
                               command=self.root.do_quit,
                               background="#ffffff")
        button_cancel.grid(row=3, column=2, stick="e")

    def init_menu(self):
        """创建菜单栏"""
        bar = Menu(self.root)
        menu = Menu(bar, tearoff=0)
        menu.add_command(label="关于", command=self.root.open_about)
        menu.add_separator()
        menu.add_command(label="退出", command=self.root.do_quit)

        bar.add_cascade(label="操作", menu=menu)
        self.root.config(menu=bar)

    def do_login(self):
        username = self.username.get()
        if not username:
            messagebox.showinfo(title="错误", message="账号不能为空！")
            return
        password = self.password.get()
        if not password:
            messagebox.showinfo(title="错误", message="密码不能为空！")
            return

        res = dbcontent.user_login(username, password)
        if not res:
            messagebox.showinfo(title="错误", message="账号或密码错误！")
        else:
            gv.set("CURRENT_USER_NAME", str(username))
            self.do_app()
            # if username == "admin" and password == "admin": # 测试账号

    def return_envent(self, event):
        self.do_login()

    def do_app(self):
        # 清理登录界面
        self.page.destroy()
        # self.blank_top.destroy()
        # self.blank_left.destroy()
        # self.blank_right.destroy()
        # self.blank_bottom.destroy()
        # 加载应用主界面
        ViewMain(self.root)


class PageHome(Frame):  # 继承Frame类
    """应用主界面"""

    def __init__(self, parent=None):
        parent.title("主界面")
        Frame.__init__(self, parent)
        self.root = parent  # 定义内部变量root
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self, text="用户:").pack()

        Label(self, text="欢迎" + str(gv.get("CURRENT_USER_NAME"))).pack()
        Button(self, text="查看").pack()


class ContentAdd(Frame):
    """文章添加"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        parent.title("文章添加")
        self.root = parent  # 定义内部变量root
        self.content_title = StringVar()
        self.content_textarea = None
        self.content_tag = StringVar()
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self).grid(row=0, stick="w", pady=10)

        lb1 = Label(self, text="标题: ")
        lb1.grid(row=1, stick="w", pady=10)

        et1 = Entry(self, textvariable=self.content_title)
        et1.grid(row=1, column=1, stick="we")

        lb2 = Label(self, text="内容: ")
        lb2.grid(row=2, stick="nw", pady=10)

        et2 = scrolledtext.ScrolledText(
            self,
            height=10,
            font=("Courier New", 13),
            fg="#333",
            borderwidth=1,
            highlightcolor="#ddd",
        )
        et2.grid(row=2, column=1, ipadx=10, stick="nswe")
        self.content_textarea = et2

        lb3 = Label(self, text="标签: ")
        lb3.grid(row=3, stick="w", pady=10)

        et3 = Entry(self, textvariable=self.content_tag)
        et3.grid(row=3, column=1, columnspan=2, stick="we")

        bt1 = Button(self, text="添加", command=self.do_add)
        bt1.grid(row=6, column=1, stick="e", pady=10)

    def do_add(self):
        """添加文章"""
        title = self.content_title.get()
        content = self.content_textarea.get(0.0, "end")
        tag = self.content_tag.get()
        username = str(gv.get("CURRENT_USER_NAME"))
        res = dbcontent.content_add(username, title, content, tag)
        if res is True:
            self.content_title.set("")
            self.content_tag.set("")
            self.content_textarea.delete(1.0, "end")  # 清空
            self.content_textarea.update()
            messagebox.showinfo(title="成功", message="添加成功")
        else:
            messagebox.showinfo(title="错误", message="添加失败")


class ContentList(Frame):
    """文章列表"""

    def __init__(self, parent=None):
        parent.title("文章列表")
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_content_info = None
        self.win_content_edit = None
        self.init_page()

    def init_page(self):
        """加载控件"""

        username = str(gv.get("CURRENT_USER_NAME"))
        self.list = dbcontent.content_list_by_username(username)

        head_frame = LabelFrame(self, text="文章操作")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = Button(head_frame, text="详情", command=self.info)
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="编辑", command=self.edit)
        btn_edit.pack(side="left")
        btn_delete = Button(head_frame, text="删除", command=self.delete)
        btn_delete.pack(side="left")

        # 表格
        self.tree_view = Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "title", "content", "tag")
        # 列设置
        self.tree_view.column("id", width=100)
        # self.tree_view.column("title", width=100)
        # self.tree_view.column("content", width=100)
        # self.tree_view.column("tag", width=100)
        # 显示表头
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("title", text="标题")
        self.tree_view.heading("content", text="内容")
        self.tree_view.heading("tag", text="标签")

        # 插入数据
        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["title"], item["content"],
                        item["tag"]),
            )
        # 选中行
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        # 排序
        for col in self.tree_view["columns"]:  # 给所有标题加
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False),
            )

        vbar = Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")

    def select(self, event):
        """选中"""
        # event.widget获取Treeview对象，调用selection获取选择所有选中的
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])
        # print("you clicked on ", self.selected_item)
        # print(self.selected_name)

    def info(self):
        """详情"""
        print("详情", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("提示", "请先选择")
        else:
            if self.win_content_info is not None and hasattr(
                    self.win_content_info.destroy, "__call__"):
                # if self.win_content_info and self.win_content_info.destroy:
                self.win_content_info.destroy()
            self.win_content_info = WinContentInfo(self.selected_item)
            # self.win_content_info = winAbout.Init()

    def edit(self):
        """编辑"""
        print("编辑", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("提示", "请先选择")
        else:
            if self.win_content_edit and self.win_content_edit.destroy:
                self.win_content_edit.destroy()
            self.win_content_edit = WinContentEdit(self.selected_item)

    def delete(self):
        """删除"""
        print(self.selected_item)
        messagebox.showinfo("删除？", self.selected_item)  # 弹出消息提示框


class CountFrame(Frame):
    """文章统计"""

    def __init__(self, parent=None):
        parent.title("文章统计")
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self, text="统计界面").pack()


class PageContact(Frame):
    """联系我们"""

    def __init__(self, parent=None):
        parent.title("联系我们")
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        """加载控件"""
        # Label(self, text="关于界面").grid()
        Label(self, text="你好你好你好你好").grid()
        Label(self, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()


class UserListFrame(Frame):
    """用户列表界面"""

    def __init__(self, parent=None):
        parent.title("用户列表")
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_user_info = None
        self.win_user_edit = None
        self.init_page()

    def init_page(self):
        """加载控件"""

        self.list = dbcontent.user_list()

        head_frame = LabelFrame(self, text="用户操作")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = Button(head_frame, text="详情", command=self.info)
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="编辑", command=self.edit)
        btn_edit.pack(side="left")
        btn_reset = Button(head_frame, text="重置密码", command=self.reset)
        btn_reset.pack(side="left")
        btn_delete = Button(head_frame, text="删除", command=self.delete)
        btn_delete.pack(side="left")

        # 表格
        self.tree_view = Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "name", "password", "op")
        # 列设置
        # self.tree_view.column("id", width=100) # 表示列,不显示
        # self.tree_view.column("name", width=100)
        # self.tree_view.column("password", width=100)
        # self.tree_view.column("op", width=100)
        # 显示表头
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("name", text="姓名")
        self.tree_view.heading("password", text="密码")
        self.tree_view.heading("op", text="操作")

        # 插入数据
        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["name"], item["password"], "详情"),
            )
        # 选中行
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        # 排序
        for col in self.tree_view["columns"]:  # 给所有标题加
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False),
            )

        vbar = Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")
        Label(self, text="底部操作栏").grid(sticky="swe")

    def select(self, event):
        """选中"""
        # event.widget获取Treeview对象，调用selection获取选择所有选中的
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])

    def info(self):
        """详情"""
        print("详情", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("提示", "请先选择")
        else:
            if self.win_user_info is not None and (hasattr(
                    self.win_user_info.destroy, "__call__")):
                self.win_user_info.destroy()
            self.win_user_info = WinUserInfo(self.selected_item)

    def edit(self):
        """用户编辑"""
        print("编辑", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("提示", "请先选择")
        else:
            if self.win_user_edit is not None and hasattr(
                    self.win_user_edit.destroy, "__call__"):
                self.win_user_edit.destroy()
            self.win_user_edit = WinUserEdit(self.selected_item)

    def delete(self):
        """用户删除"""
        print(self.selected_item)
        messagebox.showinfo("删除用户？", self.selected_item)  # 弹出消息提示框

    def reset(self):
        """用户删除"""
        print("用户删除")


class UserAddFrame(Frame):
    """用户添加"""

    def __init__(self, parent=None):
        parent.title("用户添加")
        Frame.__init__(self, parent)
        self.root = parent
        self.username = StringVar()
        self.password = StringVar()
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self).grid(row=0, stick="w")

        Label(self, text="账户: ").grid(row=1, stick="w", pady=10)
        username = Entry(self, textvariable=self.username)
        username.grid(row=1, column=1, stick="e")

        Label(self, text="密码: ").grid(row=2, stick="w", pady=10)
        password = Entry(self, textvariable=self.password, show="*")
        password.grid(row=2, column=1, stick="e")

        button_login = Button(self, text="添加", command=self.do_add)
        button_login.grid(row=3, column=1, stick="w", pady=10)

    def do_add(self):
        """添加帐号"""
        # print(event)
        username = self.username.get()
        password = self.password.get()
        res = dbcontent.user_add(username, password)
        if res is True:
            self.username.set("")
            self.password.set("")
            messagebox.showinfo(title="成功", message="添加成功")
        else:
            messagebox.showinfo(title="错误", message="账号已存在")


class PageSettings(Frame):
    """设置页面"""

    def __init__(self, parent=None):
        parent.title("InPanel 设置")
        Frame.__init__(self, parent)
        self.root = parent
        self.username = StringVar()
        self.password = StringVar()
        self.init_page()
        # self["padding"] = 30
        # self["background"] = "#333333"

    def init_page(self):
        """加载控件"""
        nb = Notebook(self)
        authinfo = Frame(nb, background="#ffffff")
        serverinfo = Frame(nb, background="#ffffff")
        accesskey = Frame(nb, background="#ffffff")
        upversion = Frame(nb)
        restart = Frame(nb)
        nb.add(authinfo, text="登录设置")
        nb.add(serverinfo, text="服务设置")
        nb.add(accesskey, text="远程控制")
        nb.add(upversion, text="版本升级")
        nb.add(restart, text="重启服务")
        # elf.page = Frame(self.root, background="#ffffff", width=100)
        # self.page.pack(side="top", fill="both", anchor="center", expand="yes")
        nb.pack(side="left", fill="both", anchor="center", expand="yes")

        label1 = Label(authinfo, text="标签1")
        label1.pack()
        button1 = Button(authinfo, text="按钮1", width=20)
        button1.pack()

    #     Label(authinfo).grid(row=0, stick="w")

    #     Label(authinfo, text="账户: ").grid(row=1, stick="w", pady=10)
    #     username = Entry(authinfo, textvariable=self.username)
    #     username.grid(row=1, column=1, stick="e")

    #     Label(authinfo, text="密码: ").grid(row=2, stick="w", pady=10)
    #     password = Entry(authinfo, textvariable=self.password, show="*")
    #     password.grid(row=2, column=1, stick="e")

    #     button_login = Button(authinfo, text="添加", command=self.do_add)
    #     button_login.grid(row=3, column=1, stick="w", pady=10)

    # def do_add(self):
    #     """添加帐号"""
    #     # print(event)
    #     username = self.username.get()
    #     password = self.password.get()
    #     res = dbcontent.user_add(username, password)
    #     if res is True:
    #         self.username.set("")
    #         self.password.set("")
    #         messagebox.showinfo(title="成功", message="添加成功")
    #     else:
    #         messagebox.showinfo(title="错误", message="账号已存在")


if __name__ == "__main__":
    App()
