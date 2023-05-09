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

input_path = r"C:\Users\18292\Desktop\0506\新堰"
file2_path = r"C:\Users\18292\Desktop\0506\新堰\提取自-.pdf"   # 指定要追加的pdf文件
completed_folders = []   # 存储哪个人名文件夹合并了几个pdf文件，pdf文件名称是什么
for root, dirs, files in os.walk(input_path):
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        files = [file for file in sorted(os.listdir(dir_path)) if file.endswith(".pdf")]
        count = 0
        merged_files = []   # 存储已经合并的文件
        for file in files:
            file1_path = os.path.join(dir_path, file)
            merge_pdf(file1_path, file2_path)
            merged_files.append(file)   # 将已经合并的文件添加到列表中
            count += 1
        completed_folders.append((dir_path, count, merged_files))   # 将完成合并的信息添加到列表中

# 输出完成合并的信息
for folder, count, merged_files in completed_folders:
    print(f"{folder}最终合并了{count}个pdf文件，文件名分别为：{', '.join(merged_files)}。")







