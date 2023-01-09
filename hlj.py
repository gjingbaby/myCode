import os
import shutil
import time

def get_folder_name(folderpath):
    os.chdir(folderpath)
    doclist = os.listdir(r'%s'%(folderpath.strip()))
    new_doclist = []
    for i in doclist:
        if os.path.isdir(os.path.join(folderpath,i)):
            new_doclist.append(i)
    print('文件夹数量：%d:文件数量:%d'%(len(new_doclist),len(doclist)-len(new_doclist)))
    return new_doclist

def folder_rename(folderlist,folder_path):
    for i in range(0,len(folderlist)):
        new_name = folder_path + r"\%d-%s"%(i+1,folderlist[i])
        old_name = folder_path + r"\%s"%(folderlist[i])
        os.rename(old_name, new_name)
        print('已完成：'+new_name)

if __name__ == '__main__':
    while True:
        folder_path = input('请输入待编号文件夹所在的文件夹路径：')
        folderlist = get_folder_name(folder_path)
        folder_rename(folderlist,folder_path)
    