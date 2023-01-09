import os
import shutil
import time

def get_pdf_name(folderpath):
    os.chdir(folderpath)
    doclist = os.listdir(r'%s'%(folderpath.strip()))
    return doclist

def move_pdf(pdflist,target_folderlist,folderpath,targetfolderpath):
    for name in pdflist:
        for foldername in target_folderlist:
            new_path = r"%s\%s\%s"%(targetfolderpath,foldername,name)
            if name.split('登记')[0] in foldername:
                if not os.path.exists(new_path):
                    shutil.move(r"%s\%s"%(folderpath,name),r"%s\%s\%s"%(targetfolderpath,foldername,name))
                    print(new_path,'移动完成')
    check_file_exists(target_folderlist,targetfolderpath)
              

def check_file_exists(target_folderlist,targetfolderpath):
    lostfile = []
    for  f in target_folderlist:
        file_path = r'%s\%s'%(targetfolderpath,f)
        file_num = len(os.listdir(file_path))
        if file_num == 0:
            print(f,'缺文件')
            lostfile.append(f)
    print(r'共%d个文件夹缺失pdf文件'%(len(lostfile)))
                
if __name__ == '__main__': 
    # folderpath = r'D:\Project\qqq\三合村-分户登记资料'
    # targetfolderpath = r'D:\Project\qqq\三合村成果\饶峰镇三合村二组'
    try:
        folderpath = input('请输入pdf文件所在文件夹目录:')
        targetfolderpath = input('请输入目标文件夹所在文件夹目录:')
        if os.path.exists(folderpath) and os.path.exists(targetfolderpath):
            pdflist = get_pdf_name(folderpath)
            target_folderlist = get_pdf_name(targetfolderpath)
            move_pdf(pdflist,target_folderlist,folderpath,targetfolderpath)
        else:
            print('文件目录不存在')
    except Exception as e:
        print(e)
    time.sleep(240)
        