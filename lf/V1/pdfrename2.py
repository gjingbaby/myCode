'''
文件组织目录如下：
一级文件夹（村文件夹）
  二级文件夹（人名文件夹）
  二级文件夹
    PDF文件
    PDF文件

1.重命名所有pdf文件，给pdf名称加"-"后缀，如："001.pdf"-->"001-.pdf"
2.避免在按自然编号命名时因二级文件夹内pdf名称重复造成的程序中断。
  二级文件夹
    xxx.pdf
    001.pdf
  在重命名xxx为001.pdf时会造成命名冲突
'''


# 导入os模块
import os

# 从用户获取输入文件夹路径
input_path = input("请输入所有子文件夹所在的文件夹的路径：")

# 遍历输入文件夹中的所有子文件夹
for folder in os.listdir(input_path):
  # 获取子文件夹的路径
  folder_path = os.path.join(input_path, folder)
  # 判断是否是文件夹
  if os.path.isdir(folder_path):
    # 获取子文件夹中的所有pdf文件
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]
    # 遍历每个pdf文件
    for pdf_file in pdf_files:
      # 获取pdf文件的旧路径和新路径
      old_path = os.path.join(folder_path, pdf_file)
      new_path = os.path.join(folder_path, pdf_file[:-4] + "-.pdf")
      # 重命名pdf文件
      os.rename(old_path, new_path)
      # 打印一条信息，记录重命名的情况
      print(f"在{folder}中，把{pdf_file}重命名为{pdf_file[:-4] + '-.pdf'}")

