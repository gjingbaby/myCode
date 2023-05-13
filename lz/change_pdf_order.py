'''
除只有1页的pdf外,交换pdf文件第一页和第二页的位置.

注：rb+ 是以读写方式打开二进制文件的模式。在此模式下，文件指针可以移动到文件的任意位置，以进行读取和写入。同时，该模式允许读取和写入操作重叠进行，可以在不关闭文件的情况下进行多个读写操作。这种模式常用于需要同时读取和修改文件的场景，比如在上述代码中需要在原始文件中插入新的PDF页
'''


import os
from PyPDF2 import PdfFileReader, PdfFileWriter

#调换1，2页位置
def swap_first_and_second_pages(pdf_file_path):
    with open(pdf_file_path, 'rb+') as f:
        pdf = PdfFileReader(f)
        page_count = pdf.getNumPages()
        if page_count < 2:
            print(f"Skipped: {pdf_file_path} (total pages: {page_count})")
            return
        first_page = pdf.getPage(0)
        second_page = pdf.getPage(1)

        writer = PdfFileWriter()
        writer.addPage(second_page)
        writer.addPage(first_page)

        for i in range(2, page_count):
            writer.addPage(pdf.getPage(i))
        #游标跳到最开始
        f.seek(0)
        writer.write(f)
        f.truncate()
        print(f"Processed: {os.path.basename(pdf_file_path)} (total pages: {page_count})")


#遍历文件夹下的所有pdf文件，对pdf文件调用1，2页调换位置的函数
def swap_first_and_second_pages_in_folder(input_folder):
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path) and file.lower().endswith('.pdf'):
            swap_first_and_second_pages(file_path)
        elif os.path.isdir(file_path):
            swap_first_and_second_pages_in_folder(file_path)


if __name__ == '__main__':
    input_folder = r'D:\hhhhhh\hhhhhh'
    # Example usage:
    swap_first_and_second_pages_in_folder(input_folder)