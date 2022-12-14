import os
import shutil
import time

class doc_handler():
    #通过文件名字创建文件夹
    def get_dir_name(self,current_path):
        os.chdir(current_path)
        #获取当前目录下文件列表
        doclist = os.listdir(r'%s'%(current_path.strip()))
        folderlist = []
        #清洗列表，规范文件夹名字
        for doc in doclist:
            #通过标准分幅图工程或gdb名称确定文件夹名称
            foldername = doc[0:10].strip()
            folderlist.append(foldername)
        #返回去重的列表
        return set(folderlist) 


    #创建文件夹目录
    def create_dir(self,folderlist,cityname):
        for folder in folderlist:
            if not os.path.exists(folder):
                #创建目录
                os.mkdir(folder)
                os.mkdir(folder+'/'+cityname)
                os.mkdir(folder+'/'+cityname+'最终标准分幅图')

    #移动gdb和mxd文件
    def move_doc(self,folderlist,county_name):
        i = 0
        for folder in folderlist:
            #计数器
            i = i + 1
            print(i,'start',folder)
            #开始移动
            shutil.move(r'%s.mxd'%(folder),r'%s\%s\%s.mxd'%(folder,county_name+"最终标准分幅图",folder))
            shutil.move(r'%s.gdb'%(folder),r'%s\%s\%s.gdb'%(folder,county_name,folder))
            print('over',folder)


    #重命名文件,将gdb名称统一替换成xx县标准分幅图.gdb
    def doc_rename(self,folderlist):
        i = 0
        for folder in folderlist:
            # print(folder)
            # if os.path.exists(folder):
            i = i + 1
            print(i,'start',folder)
            # os.rename(r'%s\%s\%s.gdb'%(folder,county_name,folder),r'%s\%s\%s.gdb'%(folder,county_name,county_name+"标准分幅图"),)
            os.rename(r'%s\%s\%s.gdb'%(folder,'定边县',folder),r'%s\%s\%s.gdb'%(folder,'定边县','定边县标准分幅图'))
            # os.rename(r'%s\%s'%(folder,'石泉县最终标准分幅图'),r'%s\%s'%(folder,'定边县最终标准分幅图'))
            print('over',folder)

    #复制指定文件到指定文件夹
    def copy_doc(self,county_name,targetfolder,copyfile,):
        #整理好的目录，只有文件夹，获取文件夹名称列表
        folderlist = os.listdir(r'%s'%(targetfolder.strip()))
        
        #去掉文件路径前缀，只保留文件名称
        _copyfile = copyfile[3:11]
        # print(_copyfile)
        i = 0
        for folder in folderlist:
            i = i + 1
            if not os.path.exists(targetfolder+'/'+folder+'/'+county_name+'/'+_copyfile):
                print(i,'start',folder)
                shutil.copytree(r'%s'%(copyfile),targetfolder+'/'+folder+'/'+county_name+'/'+_copyfile)
                print('over',folder,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            else:
                print('已存在',folder+'/'+_copyfile,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    #删除指定文件
    def rm_doc(self,dirlist,current_path,cityname):
        i = 0
        for folder in dirlist:
            i = i + 1
            tpath = current_path+'/'+folder+'/'+cityname+'/'+'BKZJ.gdb'
            shutil.rmtree(tpath)
            print(i,folder)

if __name__ == "__main__":
    current_path = 'd:/定边'
    cityname = '定边县'
    dirlist = doc_handler().get_dir_name(current_path)
    # doc_handler.create_dir(dirlist,cityname)
    # doc_handler.move_doc(dirlist,cityname)

    targetfolder = "D:\定边"
    copyfile = "D:\BKZJ.gdb"

    doc_handler().copy_doc(cityname,targetfolder,copyfile)
    # doc_handler.doc_rename(dirlist)
    # doc_handler.rm_doc(dirlist,current_path,cityname)
