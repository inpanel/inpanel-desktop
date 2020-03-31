#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Menu, StringVar, Tk, messagebox, scrolledtext
from tkinter.ttk import (Button, Entry, Frame, Label, LabelFrame, Scrollbar,
                         Treeview)

import lib.dbcontent as dbcontent
from lib import global_variable
from lib.functions import set_window_center, treeview_sort_column
from menu import MainMenu
from window import (WinAbout, WinContentEdit, WinContentInfo, WinUserEdit,
                    WinUserInfo)


class App(Tk):
    """Application Class"""

    def __init__(self):
        Tk.__init__(self)
        # WinSplah()
        # 登录窗口
        Login(self)
        self.mainloop()

class Login():
    """登录"""

    def __init__(self, master=None):
        if self.isLoggedIn() is True:
            MainPage(master)
        else:
            self.root = master
            master.title("账号登陆")
            set_window_center(self.root, 300, 180)
            self.root.resizable(False, False)
            # 定义变量
            self.username = StringVar()
            self.password = StringVar()
            self.init_menu()
            self.init_page()

    def init_page(self):
        """登录界面"""

        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()

        Label(self.page).grid(row=0, stick="W")

        Label(self.page, text="账户: ").grid(row=1, stick="W", pady=10)
        username = Entry(self.page, textvariable=self.username)
        username.grid(row=1, column=1, stick="E")
        username.bind("<Return>", self.returnEnvent)

        Label(self.page, text="密码: ").grid(row=2, stick="W", pady=10)
        password = Entry(self.page, textvariable=self.password, show="*")
        password.grid(row=2, column=1, stick="E")
        password.bind("<Return>", self.returnEnvent)

        button_login = Button(self.page, text="登陆", command=self.doLogin)
        button_login.grid(row=3, column=1, stick="W", pady=10)

        button_cancel = Button(self.page, text="退出", command=self.doCancel)
        button_cancel.grid(row=3, column=1, stick="e")

    def init_menu(self):
        """创建菜单栏"""
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="退出", command=self.root.quit)
        menubar.add_cascade(label="文件", menu=filemenu)
        self.root.config(menu=menubar)

    def doLogin(self):
        username = self.username.get()
        password = self.password.get()
        res = dbcontent.user_login(username, password)
        if res is True:
            # if username == "admin" and password == "admin": # 测试账号
            self.page.destroy()

            global_variable.set_variable("CURRENT_USER_NAME", str(username))
            MainPage(self.root)
        else:
            messagebox.showinfo(title="错误", message="账号或密码错误！")

    def doCancel(self):
        self.page.quit()

    def returnEnvent(self, event):
        self.doLogin()

    def isLoggedIn(self):
        # return True
        return False

class MainPage():
    """主界面"""

    def __init__(self, master=None):
        self.root = master  # 主窗口
        set_window_center(self.root, 800, 600)
        self.root.resizable(True, True)
        MainMenu(self)  # 使用self可以传递主窗口和主窗口操作函数
        # 初始化Frames
        self.current_frame = None
        self.page_frame = {
            "home": HomeFrame,
            "content_add": ContentAdd,
            "content_list": ContentList,
            "count": CountFrame,
            "contact": AboutFrame,
            "user_list": UserListFrame,
            "user_add": UserAddFrame
        }
        self.open_home()
        self.win_about = None

    def open_page(self, frame_name, title):
        """打开/更换主界面的通用函数"""
        self.root.title(title)
        # 先销毁之前frame
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.root)
        self.current_frame.pack()

    def open_home(self):
        """应用主界面"""
        self.open_page("home", "应用主界面")

    def open_content_add(self):
        """文章添加"""
        self.open_page("content_add", "文章添加")

    def open_content_list(self):
        """文章列表"""
        self.open_page("content_list", "文章查询")

    def open_content_count(self):
        """文章统计"""
        self.open_page("count", "文章统计")

    def open_ontact(self):
        """联系我们"""
        self.open_page("contact", "联系我们")

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
        # self.page_frame['user_list'].init_data()

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

    def open_about(self):
        """关于窗口"""
        if self.win_about and self.win_about.destroy:
            self.win_about.destroy()
        self.win_about = WinAbout()

    def window_to_top(self):
        """窗口置顶"""
        self.root.attributes('-topmost', True)

    def window_not_top(self):
        """窗口置顶"""
        self.root.attributes('-topmost', False)


class HomeFrame(Frame):  # 继承Frame类
    """应用主界面"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # 定义内部变量root
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self, text="用户:").pack()

        Label(self, text="欢迎" +
              str(global_variable.get_variable("CURRENT_USER_NAME"))).pack()
        Button(self, text="查看").pack()


class ContentAdd(Frame):
    """文章添加"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
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
        username = str(global_variable.get_variable("CURRENT_USER_NAME"))
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

        username = str(global_variable.get_variable("CURRENT_USER_NAME"))
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
                values=(item["id"], item["title"],
                        item["content"], item["tag"]),
            )
        # 选中行
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        # 排序
        for col in self.tree_view["columns"]:  # 给所有标题加
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )

        vbar = Scrollbar(self, orient="vertical",
                             command=self.tree_view.yview)
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
            if self.win_content_info is not None and hasattr(self.win_content_info.destroy, "__call__"):
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
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self, text="统计界面").pack()


class AboutFrame(Frame):
    """关于界面"""

    def __init__(self, parent=None):
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
                    self.tree_view, _col, False
                ),
            )

        vbar = Scrollbar(self, orient="vertical",
                             command=self.tree_view.yview)
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
            if self.win_user_info is not None and (
                hasattr(self.win_user_info.destroy, "__call__")
            ):
                self.win_user_info.destroy()
            self.win_user_info = WinUserInfo(self.selected_item)

    def edit(self):
        """用户编辑"""
        print("编辑", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("提示", "请先选择")
        else:
            if self.win_user_edit is not None and hasattr(
                self.win_user_edit.destroy, "__call__"
            ):
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


if __name__ == "__main__":
    App()
