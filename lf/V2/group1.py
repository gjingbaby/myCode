'''
文件组织目录如下：
村名文件夹
    人名文件夹-组号
        pdf文件

重新组织为：
    村名文件夹
        组文件夹
            人名文件夹-组号
                pdf文件
'''

import os

# 遍历文件夹
def traverse_folder(folder):
    # 遍历所有子文件夹
    for root, dirs, files in os.walk(folder):
        for subfolder in dirs:
            # 获取新建文件夹名称
            new_folder_name = get_new_folder_name(subfolder)
            # 获取新建文件夹路径
            new_folder_path = os.path.join(root, new_folder_name)
            # 判断新建文件夹是否存在
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
            # 移动子文件夹到新建文件夹内
            old_folder_path = os.path.join(root, subfolder)
            os.rename(old_folder_path, os.path.join(new_folder_path, subfolder))
    # 对所有新建文件夹内的文件夹进行重命名
    rename_subfolders(folder)

# 获取新建文件夹名称
def get_new_folder_name(folder):
    new_folder_name = folder.split('-')[-1]
    return new_folder_name

# 对所有新建文件夹内的文件夹进行重命名
def rename_subfolders(folder):
    for root, dirs, files in os.walk(folder):
        for subfolder in dirs:
            old_folder_path = os.path.join(root, subfolder)
            # 获取重命名后的文件夹名字，去掉"-"及其后面的字符
            renamed_name = subfolder.split('-')[0]
            renamed_path = os.path.join(root, renamed_name)
            os.rename(old_folder_path, renamed_path)


# 测试代码
if __name__ == '__main__':
    folder = r'C:\Users\18292\Desktop\沙河村'
    traverse_folder(folder)
