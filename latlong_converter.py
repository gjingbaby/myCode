import os
import xlrd
import re
import xlwt
from xlutils.copy import copy

def dms_to_dd(dms_str):
    """
    将度分秒格式字符串转换为十进制格式
    :param dms_str: 度分秒格式字符串
    :return: 十进制格式值
    """
    pattern = r'(\d+)°\s*(\d+)\'\s*([\d.]+)"'
    matched = re.match(pattern, dms_str)
    if matched:
        deg = float(matched.group(1))
        minute = float(matched.group(2))
        second = float(matched.group(3))
        return deg + minute / 60 + second / 3600
    return None

def dd_to_dms(dd_value):
    """
    将十进制格式值转换为度分秒格式字符串
    :param dd_value:十进制格式值
    :return:度分秒格式字符串
    """
    if not isinstance(dd_value, (int,float)):
        return None
    deg, minute = divmod(abs(dd_value), 1)
    minute, second = divmod(minute * 60, 1)
    second = round(second * 60, 3)
    dms_str = str(int(deg)) + '° ' + str(int(minute)) + '\' ' + str(second) + '\"'
    if dd_value < 0:
        dms_str = '-' + dms_str
    return dms_str

def convert_cell_value(cell_value):
    """
    转换单元格格式
    :param cell_value: 原单元格值
    :return: 转换后单元格值
    """
    if isinstance(cell_value, (int, float)):
        return dd_to_dms(cell_value)
    elif isinstance(cell_value, str):
        return dms_to_dd(cell_value)
    else:
        return None

def convert_excel_file(old_excel_path, new_excel_path):
    """
    将一个excel文件中的格式转换并保存到新文件
    :param old_excel_path: 旧文件路径
    :param new_excel_path: 新文件路径
    """
    rb = xlrd.open_workbook(old_excel_path, formatting_info=True)
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for irow in range(rs.nrows):
        for jcol in range(rs.ncols):
            cell_value = rs.cell_value(irow, jcol)
            xf_index = rs.cell_xf_index(irow, jcol)
            xf_str = rb.xf_list[xf_index].format_key
            number_format_str = rb.format_map[xf_str].format_str
            new_value = convert_cell_value(cell_value)
            if new_value:
                format_str = number_format_str
                if number_format_str != 'General':
                    format_str += ';@'
                try:
                    ws.write(irow, jcol, new_value, xlwt.easyxf(format_str.replace(':', ';')))
                except:
                    ws.write(irow, jcol, new_value)
    wb.save(new_excel_path)


if __name__ == '__main__':
    old_excel_path = input('请输入待转换文件路径：')
    file_name = os.path.splitext(old_excel_path)[0]
    new_excel_path = file_name + '_new' + '.xls'
    convert_excel_file(old_excel_path, new_excel_path)
    print('转换已完成：' + new_excel_path)

    








