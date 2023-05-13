'''
文件目录及命名结构如下：
一级文件夹（村文件夹）
    何希勇-5.pdf
    蒋佐成-6.pdf
    毛礼桥-2.pdf
    张如军-5.pdf
    钟帮国-1.pdf
    钟帮国(1)-1.pdf

第一步：遍历村文件夹下的所有pdf文件，以pdf文件名称（注意不是路径）中“-”后的数字作为文件夹名字，新建组文件夹
第二步：以pdf文件名称中的汉字为名称，在新建的组文件夹内创建人名文件夹，将该pdf文件移动到人名文件夹内，人名文件夹已存在的，直接将该pdf放入人名文件夹内

至此，将文件组织目录重构如下：
一级文件夹（村文件夹）
    二级文件夹（组别文件夹）
        三级文件夹（人名文件夹）
            PDF文件
            PDF文件

第三步：重命名人名文件夹，规则为组内从'1.某某'开始顺序递增，2.某某、3.某某....
第四步：重命名pdf文件,村文件夹内不重复，从001开始顺序递增，002.pdf、003.pdf...
'''


# -*- coding: utf-8 -*-

import shutil
import os
import re

'''第一步'''
# 定义一个函数，参数是村文件夹的路径
def refactor_code(village_dir):
    # 第一步：遍历村文件夹下的所有pdf文件
    for file in os.listdir(village_dir): # 遍历村文件夹下的所有文件
        if file.endswith(".pdf"): # 如果是pdf文件
            file_path = os.path.join(village_dir, file) # 获取pdf文件的完整路径
            file_name = os.path.splitext(file)[0] # 获取pdf文件的名称（不含扩展名）
            group_num = file_name.split("-")[1].split(" ")[0] # 获取pdf文件名称中“-”和“ ”之间的数字，作为组别
            
            person_name = file_name.split("-")[0] # 获取pdf文件名称中“-”前的汉字，作为人名
            # 第二步：新建组文件夹和人名文件夹，并移动pdf文件
            group_dir = os.path.join(village_dir, group_num) # 组别文件夹的路径
            if not os.path.exists(group_dir): # 如果组别文件夹不存在
                os.mkdir(group_dir) # 创建组别文件夹

            person_dir = os.path.join(group_dir, person_name) # 人名文件夹的路径
            if not os.path.exists(person_dir): # 如果人名文件夹不存在
                os.mkdir(person_dir) # 创建人名文件夹

            shutil.move(file_path, person_dir) # 将pdf文件移动到人名文件夹内
            print(os.path.basename(group_dir),"-",os.path.basename(person_dir),"-",os.path.basename(file_path))
    print('--------------------第一步：组织目录重构已完成----------------------')

'''第二步'''
def rename_sub_dirs(input_dir):
    # 获取输入文件夹下的所有子文件夹
    sub_dirs = [os.path.join(input_dir, name) for name in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, name))]

    # 遍历子文件夹，对子文件夹中的文件夹进行重命名
    for sub_dir in sub_dirs:
        # 获取子文件夹下的所有文件夹
        sub_sub_dirs = [os.path.join(sub_dir, name) for name in os.listdir(sub_dir) if os.path.isdir(os.path.join(sub_dir, name))]
        
        # 遍历子文件夹下的所有文件夹，重命名文件夹
        for i, sub_sub_dir in enumerate(sub_sub_dirs):
            # 获取文件夹名字并处理
            old_name = os.path.basename(sub_sub_dir)
            new_name = str(i+1) + "." + ''.join(filter(lambda x: not x.isdigit() and x != '-' and x != '.', old_name))
            # 重命名文件夹
            os.rename(sub_sub_dir, os.path.join(sub_dir, new_name))
            print(os.path.basename(sub_dir),'-->',old_name,'-->',new_name)
    print('--------------------第二步：人名文件夹重命名完成----------------------')

'''第三步'''
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

if __name__ == "__main__":
    while True:
        # 初始化重命名的起始数字
        start = 1
        village_dir = input("请输入待处理文件夹路径：")
        refactor_code(village_dir)
        rename_sub_dirs(village_dir)
        traverse_subfolders(village_dir, start)
        print('--------------------第三步：pdf文件重命名完成----------------------')



