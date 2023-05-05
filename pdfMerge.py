# -*- coding: utf-8 -*-

import os
import PyPDF2

def merge_pdf(file1, file2):
  pdf1 = open(file1, "rb")
  pdf1_reader = PyPDF2.PdfFileReader(pdf1)
  pdf2 = open(file2, "rb")
  pdf2_reader = PyPDF2.PdfFileReader(pdf2)
  pdf_writer = PyPDF2.PdfFileWriter()
  for page in range(pdf1_reader.numPages):
    pdf_writer.addPage(pdf1_reader.getPage(page))
  for page in range(pdf2_reader.numPages):
    pdf_writer.addPage(pdf2_reader.getPage(page))
  pdf_output = open(file1, "ab")
  pdf_writer.write(pdf_output)
  pdf_output.close()
  pdf1.close()
  pdf2.close()

input_path = input("请输入所有子文件夹所在的文件夹的路径：")
skipped_folders = []   # 存储跳过的文件夹
completed_folders = []   # 存储哪个子文件夹合并了几个pdf文件，pdf文件名称是什么
for folder in os.listdir(input_path):
  folder_path = os.path.join(input_path, folder)
  if os.path.isdir(folder_path):
    files = [file for file in sorted(os.listdir(folder_path)) if file.endswith(".pdf")]
    if "提取自-.pdf" in files:
      file2_path = os.path.join(folder_path, "提取自-.pdf")
      count = 0
      merged_files = []   # 存储已经合并的文件
      for file in files:
        if file != "提取自-.pdf":
          file1_path = os.path.join(folder_path, file)
          merge_pdf(file1_path, file2_path)
          merged_files.append(file)   # 将已经合并的文件添加到列表中
          count += 1
      os.remove(file2_path)
      completed_folders.append((folder, count, merged_files))   # 将完成合并的信息添加到列表中
    else:
      skipped_folders.append(folder)   # 将跳过的文件夹添加到列表中

# 输出完成合并的信息
for folder, count, merged_files in completed_folders:
  print(f"{folder}最终合并了{count}个pdf文件，文件名分别为：{', '.join(merged_files)}。")

# 输出跳过的文件夹
if len(skipped_folders) > 0:
  print("以下文件夹因为不包含指定文件而被跳过：")
  for folder in skipped_folders:
    print(folder)
else:
  print("所有子文件夹都已成功处理。")
