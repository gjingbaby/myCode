'''
文件组织目录如下：
一级文件夹（村文件夹）
    二级文件夹（组别文件夹）
    二级文件夹
        三级文件夹（人名文件夹）
        三级文件夹
            PDF文件
            PDF文件

1.给所有pdf文件重命名,命名从001开始递增，如：001.pdf、002.pdf...
2.保证在一级文件夹内不重不漏
'''


# 导入os和re模块
import os
import re

# 定义一个函数，按照子文件夹名字中的数字排序
def sort_by_number(subfolder):
    # 获取子文件夹的名字，不包括路径
    subfolder_name = os.path.basename(subfolder)
    # 使用正则表达式找到子文件夹名字中的整个数字
    match = re.search(r"\d+", subfolder_name)
    # 如果有数字，就返回它的整数值
    if match:
        return int(match.group())
    # 否则，返回一个很大的数字，把子文件夹放到最后
    else:
        return 999999
    
# 定义一个函数，重命名子文件夹中的pdf文件
def rename_pdf_files(subfolder, start):
    # 获取子文件夹中的pdf文件列表
    pdf_files = [f for f in os.listdir(subfolder) if f.endswith(".pdf")]
    # 按照文件名排序pdf文件
    pdf_files.sort()
    # 遍历pdf文件
    for i, pdf_file in enumerate(pdf_files):
        # 生成一个新的名字，包含三个数字和.pdf扩展名
        new_name = f"{start + i:03d}.pdf"
        # 获取pdf文件的旧路径和新路径
        old_path = os.path.join(subfolder, pdf_file)
        new_path = os.path.join(subfolder, new_name)
        # 重命名pdf文件
        os.rename(old_path, new_path)
        # 打印一条信息，记录重命名的情况
        print(f"在{subfolder}中，把{pdf_file}重命名为{new_name}")
    # 返回下一个子文件夹的起始数字
    return start + len(pdf_files)

# 定义一个函数，遍历所有层级的子文件夹，并且重命名pdf文件
def traverse_subfolders(input_folder, start):
    # 获取输入文件夹中的子文件夹列表
    subfolders = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, f))]
    # 按照子文件夹名字中的数字排序
    subfolders.sort(key=sort_by_number)
    # 遍历子文件夹
    for subfolder in subfolders:
        # 如果子文件夹中还有子文件夹，就递归调用这个函数
        if any(os.path.isdir(os.path.join(subfolder, f)) for f in os.listdir(subfolder)):
            start = traverse_subfolders(subfolder, start)
        # 否则，就重命名子文件夹中的pdf文件，并更新起始数字
        else:
            start = rename_pdf_files(subfolder, start)
    # 返回最终的起始数字
    return start

# 从用户获取输入文件夹路径
input_folder = r"C:\Users\18292\Desktop\沙河村"

# 初始化重命名的起始数字
start = 1

# 调用遍历所有层级的子文件夹，并且重命名pdf文件的函数
traverse_subfolders(input_folder, start)

# 打印一条信息，表示任务完成
print("所有的pdf文件已经重命名完成！")

