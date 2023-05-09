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



'''

import shutil
import os

# 定义一个函数，参数是村文件夹的路径
def refactor_code(village_dir):
    # 第一步：遍历村文件夹下的所有pdf文件
    for file in os.listdir(village_dir): # 遍历村文件夹下的所有文件
        if file.endswith(".pdf"): # 如果是pdf文件
            file_path = os.path.join(village_dir, file) # 获取pdf文件的完整路径
            file_name = os.path.splitext(file)[0] # 获取pdf文件的名称（不含扩展名）
            group_num = file_name.split("-")[1].split(" ")[0] # 获取pdf文件名称中“-”和“ ”之间的数字，作为组别
            
            person_name = file_name.split("-")[0] # 获取pdf文件名称中“-”前的汉字，作为人名
            print(group_num,person_name)
            # 第二步：新建组文件夹和人名文件夹，并移动pdf文件
            group_dir = os.path.join(village_dir, group_num) # 组别文件夹的路径
            if not os.path.exists(group_dir): # 如果组别文件夹不存在
                os.mkdir(group_dir) # 创建组别文件夹

            person_dir = os.path.join(group_dir, person_name) # 人名文件夹的路径
            if not os.path.exists(person_dir): # 如果人名文件夹不存在
                os.mkdir(person_dir) # 创建人名文件夹

            shutil.move(file_path, person_dir) # 将pdf文件移动到人名文件夹内

# 调用函数，传入村文件夹的路径
village_dir = r"C:\Users\18292\Desktop\sss" # 村文件夹的路径
refactor_code(village_dir)

