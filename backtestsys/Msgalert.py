# pandas处理数据

import os
import pandas as pd

# 判断文件存不存在
def alert_message(condition,msg):
    if not condition:
        raise Exception(msg)

def read_file(filepath):
    # 判断文件存不存在
    alert_message(os.path.exists(filepath),'文件不存在或路径不正确')

    return pd.read_csv(filepath, 
                       index_col = 0,
                       parse_dates = True,
                       infer_datetime_format = True)

def SMA(values,n):
    return pd.Series(values).rolling(n).mean()

def crossover(series1,series2) -> bool:
    return series1[-2] < series2[-2] and series1[-1] > series2[-1]


if __name__ == '__main__':
    bu = read_file(r'D:\pyworkspace\testtxt\bg.txt')
    alert_message(bu.__len__() > 0,'读取失败')
    print(bu.head())