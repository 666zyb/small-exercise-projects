import tkinter as tk
from tkinter import filedialog
from PIL import Image

def select_file():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(title="选择图片文件",
                                           filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    root.destroy()  # 关闭对话框窗口
    return file_path

def select_folder():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory(title="选择目录")
    root.destroy()  # 关闭对话框窗口
    return folder_path

def convert_to_icon(image_path, icon_path, sizes=[(32, 32), (64, 64)]):
    image = Image.open(image_path)
    icon_images = []

    for size in sizes:
        # 调整图像大小
        resized_image = image.resize(size, Image.LANCZOS)
        icon_images.append(resized_image)

    # 保存所有尺寸的图标到一个单一的 .ico 文件
    icon_images[0].save(icon_path, format='ICO', sizes=[size for img, size in zip(icon_images, sizes)])

# 用户选择文件和目录
selected_file = select_file()
selected_folder = select_folder()
x = selected_file.split("/")

# 确保选择了文件和目录
if selected_file and selected_folder:
    # 调用转换图标函数
    convert_to_icon(selected_file, f"{selected_folder}/{x[len(x)-1]}.ico")
    print(f"图标已保存到: {selected_folder}")
else:
    print("未选择文件或目录")