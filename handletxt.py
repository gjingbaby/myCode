'''
功能：将txt文件处理成中国工具可以识别的省标准txt
python3.9
'''


import os
import chardet

def get_file_encoding(filepath):
    """检测文件编码"""
    with open(filepath, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']

def process_file(filepath, encoding='gbk'):
    """处理单个文件"""
    file_num = 1
    
    with open(filepath, 'r+', encoding=encoding) as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()

        for i, line in enumerate(lines):
            if i < 7:
                continue

            if line.strip() == '':
                f.close()
                break

            parts = line.split(',', 1)

            if len(parts) == 1:
                line = parts[0]  
            else:
                line = parts[0] + ',' + parts[1].replace('1,', '', 1)

            f.write(f'{i+1-7},1,1,{line}')
        
def process_files(folder):
    """处理文件夹中的文件"""
    for filename in os.listdir(folder):
        try:
            process_file(os.path.join(folder, filename)) 
        except UnicodeDecodeError:
            encoding = get_file_encoding(os.path.join(folder, filename))
            process_file(os.path.join(folder, filename), encoding)
            
if __name__ == '__main__':
    folder = r'D:\Project\临时工作\李婵\神木原始数据TXT'
    process_files(folder)