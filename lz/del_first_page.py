'''
删除pdf文件第一页
'''


import os
import PyPDF2

def remove_first_page_from_all_pdfs(directory):
    """
    递归获取目录下所有 PDF 文件名
    :param directory: 目录名
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                remove_first_page_from_pdf_file(file_path)
                print(f'Removed first page from {file_path}')

def remove_first_page_from_pdf_file(file_path):
    # 打开 PDF 文件并读取所有页面
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.getNumPages()

        # 如果 PDF 文件只有一页，无需进行操作
        if num_pages <= 1:
            return

        # 创建一个新的 PDF 文件并写入第二页及以后的所有页面
        pdf_writer = PyPDF2.PdfFileWriter()
        for page in range(1, num_pages):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open('temp.pdf', 'wb') as temp_file:
            pdf_writer.write(temp_file)

    # 删除原始文件并将新文件重命名为原始文件名
    os.remove(file_path)
    os.rename('temp.pdf', file_path)

# 指定要删除第一页的 PDF 文件所在的目录
directory = r'D:\hhhhhh'
remove_first_page_from_all_pdfs(directory)






