# import os

# # 输入文件夹路径
# input_dir = r"C:\Users\18292\Desktop\sss"

# # 获取输入文件夹下的所有子文件夹
# sub_dirs = [os.path.join(input_dir, name) for name in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, name))]

# # 遍历子文件夹，对子文件夹中的文件夹进行重命名
# for sub_dir in sub_dirs:
#     # 获取子文件夹下的所有文件夹
#     sub_sub_dirs = [os.path.join(sub_dir, name) for name in os.listdir(sub_dir) if os.path.isdir(os.path.join(sub_dir, name))]
    
#     # 遍历子文件夹下的所有文件夹，重命名文件夹
#     for i, sub_sub_dir in enumerate(sub_sub_dirs):
#         # 获取文件夹名字并处理
#         old_name = os.path.basename(sub_sub_dir)
#         new_name = str(i+1) + "." + ''.join(filter(lambda x: not x.isdigit() and x != '-' and x != '.', old_name))
#         # 重命名文件夹
#         os.rename(sub_sub_dir, os.path.join(sub_dir, new_name))



import os

# 定义一个函数，参数是输入文件夹的路径
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

# 调用函数，传入输入文件夹的路径
input_dir = r"C:\Users\18292\Desktop\sss"
rename_sub_dirs(input_dir)

