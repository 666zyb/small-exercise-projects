"""
模块名称: 图形化界面框架
作者: zyb
创建日期: 2025/2/21
功能描述: 这是我写的模板，能够专注于爬虫核心逻辑的实现，简化创建用户交互界面的流程。
        通过复用此模板，可快速搭建起具备基本功能的爬虫操作界面。
使用方法: 替换start_crawling函数中的zyb模块为自己的爬虫代码文件并调用其中的主函数文件。
        实现具体的网络爬虫逻辑，使其能够根据输入的关键词获取所需数据。
"""

import tkinter as tk  # 导入GUI库
from tkinter import ttk  # 导入tkinter的主题模块
from tkinter import filedialog  # 导入文件对话框模块
import os  # 导入操作系统模块


class CrawlerGUI:
    """
    爬虫程序的图形用户界面类
    实现了一个用于爬取数据的界面，包含关键词输入、文件保存设置等功能
    """

    def __init__(self):
        """
        初始化GUI界面
        设置窗口属性、创建控件、配置样式等
        """
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("网络爬虫工具")  # 设置窗口标题
        self.root.geometry("600x500")  # 设置窗口大小

        # 设置主题样式
        style = ttk.Style()
        style.theme_use('clam')  # 使用clam主题，外观更现代

        # 设置窗口背景色
        self.root.configure(bg='#f0f0f0')  # 使用浅灰色背景

        # 创建主框架，用于容纳所有控件
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题标签 - 显示程序名称
        title_label = ttk.Label(
            main_frame,
            text="内容爬取工具",
            font=('微软雅黑', 16, 'bold')  # 设置字体样式
        )
        title_label.pack(pady=20)

        # 关键词输入区域 - 用于输入搜索关键词
        keyword_frame = ttk.LabelFrame(main_frame, text="搜索设置", padding="10")
        keyword_frame.pack(fill=tk.X, pady=10)

        ttk.Label(keyword_frame, text="请输入关键词：").pack(anchor='w')
        self.keyword_entry = ttk.Entry(keyword_frame, width=50)  # 关键词输入框
        self.keyword_entry.pack(fill=tk.X, pady=5)

        # 文件保存区域 - 用于设置文件名和保存路径
        save_frame = ttk.LabelFrame(main_frame, text="保存设置", padding="10")
        save_frame.pack(fill=tk.X, pady=10)

        # 文件名输入区域
        filename_container = ttk.Frame(save_frame)
        filename_container.pack(fill=tk.X, padx=5, pady=(0, 5))

        ttk.Label(
            filename_container,
            text="文件名：",
            background='white'
        ).pack(side=tk.LEFT)

        # 文件名输入框，默认为data.txt
        self.filename_entry = ttk.Entry(
            filename_container,
            width=40,
            font=('微软雅黑', 10)
        )
        self.filename_entry.pack(side=tk.LEFT, padx=5)
        self.filename_entry.insert(0, "data.txt")  # 设置默认文件名

        # 路径选择区域
        path_container = ttk.Frame(save_frame)
        path_container.pack(fill=tk.X, padx=5)

        ttk.Label(
            path_container,
            text="保存路径：",
            background='white'
        ).pack(side=tk.LEFT)

        # 保存路径输入框
        self.save_path = tk.StringVar()  # 用于存储选择的路径
        path_entry = ttk.Entry(
            path_container,
            textvariable=self.save_path,
            width=40,
            font=('微软雅黑', 10)
        )
        path_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        # 路径选择按钮
        browse_btn = ttk.Button(
            path_container,
            text="选择路径",
            command=self.browse_path,
            style='Secondary.TButton'
        )
        browse_btn.pack(side=tk.LEFT)

        # 按钮容器 - 用于居中显示开始按钮
        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.pack(fill=tk.X, pady=(10, 15))

        # 开始爬取按钮
        start_btn = ttk.Button(
            button_frame,
            text="开始爬取",
            command=self.start_crawling,
            style='Accent.TButton'
        )
        start_btn.pack(anchor='center')

        # 状态显示标签 - 用于显示程序运行状态
        self.status_label = ttk.Label(
            main_frame,
            text="准备就绪",
            font=('微软雅黑', 11),
            foreground='#666666',
            background='#f0f0f0'
        )
        self.status_label.pack(pady=20)

        # 自定义主按钮样式
        style.configure(
            'Accent.TButton',
            background='#007acc',
            foreground='white',
            padding=10,
            font=('微软雅黑', 10)
        )

    def save_data(self, data, save_path):
        """
        保存爬取的数据到文件

        Args:
            data: 要保存的数据内容
            save_path: 文件保存路径
        """
        path = save_path + '/' + 'data.txt'
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(data)

    def browse_path(self):
        """
        打开文件对话框让用户选择保存路径
        选择后自动更新路径显示
        """
        directory = filedialog.askdirectory()
        if directory:
            self.save_path.set(directory)

    def start_crawling(self):
        """
        开始爬取数据的主要方法
        - 验证输入
        - 调用爬虫代码
        - 保存数据
        - 显示状态
        """
        # 获取用户输入
        keyword = self.keyword_entry.get()
        save_path = self.save_path.get()
        filename = self.filename_entry.get()

        # 输入验证
        if not keyword:
            self.status_label.config(
                text="⚠️ 请输入关键词！",
                foreground='#dc3545'
            )
            return

        if not save_path:
            self.status_label.config(
                text="⚠️ 请选择保存路径！",
                foreground='#dc3545'
            )
            return

        if not filename:
            self.status_label.config(
                text="⚠️ 请输入文件名！",
                foreground='#dc3545'
            )
            return

        # 更新状态显示
        self.status_label.config(
            text="🔄 正在爬取中...",
            foreground='#007acc'
        )
        self.root.update()  # 立即更新界面显示

        try:
            # 调用爬虫代码
            import zyb
            data = str(zyb.main(keyword))
            # 保存数据
            path = os.path.join(save_path, filename)
            with open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(data)
            # 显示成功消息
            self.status_label.config(
                text=f"✅ 数据爬取成功！文件已保存为：{filename}",
                foreground='#28a745'
            )
        except Exception as e:
            # 显示错误消息
            self.status_label.config(
                text=f"❌ 爬取失败：{str(e)}",
                foreground='#dc3545'
            )

    def run(self):
        """
        启动GUI程序的主循环
        """
        self.root.mainloop()


if __name__ == "__main__":
    app = CrawlerGUI()  # 创建GUI实例
    app.run()  # 运行程序