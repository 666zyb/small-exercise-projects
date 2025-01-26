import os
import zipfile
# import rarfile  如果里面有rar后缀的压缩包加上

def extract_zip(file_path, extract_to):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


# def extract_rar(file_path, extract_to):
#     with rarfile.RarFile(file_path, 'r') as rar_ref:
#         rar_ref.extractall(extract_to)


def main(folder_path, destination_folder):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.zip'):
                print(f"正在解压 {file_path} 到 {destination_folder}")
                extract_zip(file_path, destination_folder)
            # elif file.endswith('.rar'):
            #     print(f"正在解压 {file_path} 到 {destination_folder}")
            #     extract_rar(file_path, destination_folder)


if __name__ == "__main__":
    folder_path = "C:\\Users\\zyb\\Desktop\\爬虫"  # 替换为你需要解压的文件夹的路径
    destination_folder = "C:\\Users\\zyb\\Desktop\\实验报告"  # 替换为你想要解压到的指定文件夹的路径
    main(folder_path, destination_folder)