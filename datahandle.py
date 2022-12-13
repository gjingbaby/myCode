import xlwings as xw
from tqdm import tqdm
import time

class Mergecell():
    '''
    1.提取每行作为一个tuple，汇集成list
        [(A1,B1,...),(A2,B2,...),...]
    2.创建空dict，循环list进行去重，追加
    3.写入文件
    
    初始化参数：
        column：区域左上角
        row：区域右下角
        xls_path：文件地址
        sheet_name：sheet名称
        save_path:输出文件保存地址
    '''

    # 初始化参数
    def __init__(self,column,row,xls_path,sheet_name,save_path):
        self.column = column
        self.row = row
        self.xls_path = xls_path
        self.sheet_name = sheet_name
        self.save_path = save_path

    # 连接excel表格，返回range对象
    def open_xls(self):
        wb = xw.Book(self.xls_path)
        a = wb.sheets[self.sheet_name].range(self.column,self.row)
        # wb.save()
        # wb.close()
        print('1.文件连接成功，正在提取单元格内容')
        return a

    # 对range对象zip形成组，返回组形成的list
    def zip_abc(self):
        a_li = []
        b_li = []
        for cell in tqdm(self.open_xls(),desc = '提取中',unit='个'):
            if cell.column == 1:
                a_li.append(cell.value)
            else:
                b_li.append(cell.value)
            time.sleep(0.000001)   
        c_li = list(zip(a_li, b_li))
        print('2.单元格内容提取完成，正在合并单元格内容')
        return c_li     

    # 去重并合并不同单元格内容，存储到字典value
    def cell_merge(self):
        results = {}
        for i,ele in tqdm(enumerate(self.zip_abc()),desc='合并中',unit='个'):
            if ele[0] not in results:
                results[ele[0]] = ele[1]
            else:
                results[ele[0]] = results[ele[0]] + ',' + ele[1]
            time.sleep(0.000001)
        print('3.单元格内容合并完成，正在写入文件')
        return results

    # 写入文件，进行保存
    def run_and_save(self):
        with open(self.save_path,'w')as f:
            for k,v in tqdm(self.cell_merge().items(),desc='写入中',unit='个'): # 加入进度条
                f.write(k+':'+v+'\n')
                time.sleep(0.000001)
        print('4.写入完成')



if __name__ == '__main__':
    mc = Mergecell('A2','B11442',r'C:\Users\18292\Desktop\data.xls','sheet1','results.txt')
    mc.run_and_save()
        


