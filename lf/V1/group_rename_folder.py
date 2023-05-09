
'''
文件组织目录如下：
一级文件夹（组文件夹）
    二级文件夹（人名文件夹:"哈哈哈"）
    二级文件夹
        PDF文件
        PDF文件

1.给所有二级文件夹重命名："哈哈哈"-->"哈哈哈-1","1"是组文件夹名称
'''

# 导入os模块
import os
# 从用户获取输入文件夹路径
input_path = input("请输入所有子文件夹所在的文件夹的路径：")
# 获取输入文件夹的名字
input_name = os.path.basename(input_path)
# 遍历输入文件夹中的所有子文件夹
for folder in os.listdir(input_path):
    # 获取子文件夹的路径
    folder_path = os.path.join(input_path, folder)
    # 判断是否是文件夹
    if os.path.isdir(folder_path):
        # 获取新的文件夹名字，添加"-"和输入文件夹的名字
        new_name = folder + "-" + input_name
        # 获取新的文件夹路径
        new_path = os.path.join(input_path, new_name)
        # 重命名文件夹
        os.rename(folder_path, new_path)
        # 打印一条信息，记录重命名的情况
        print(f"在{input_name}中，把{folder}重命名为{new_name}")