# -*- coding: utf-8 -*-

'''
这个函数的作用是对一个shp文件的属性表进行排序和分组,并添加一个新的字段。它有五个参数，分别是：

input_shp: 输入要处理的shp文件的路径,例如r"C:\Users\18292\Desktop\1.矢量空间数据\统一坐标\610632ZDJZD.shp"
fid_field: shp文件中的FID字段名,用来唯一标识每一行的数据，例如"FID"
djzq_field: shp文件中的DJZQ字段名,用来分组数据,例如"DJZQ"
xzbz_field: shp文件中的XZBZ字段名,用来排序数据，例如"XZBZ"
jzd_field: 要添加的新字段名，用来存储每一行的排名结果，例如"JZD"
函数的输出是将排名结果写入新的属性表,并打印每一行的FID值。
'''

# import arcpy
# from itertools import groupby

# # 输入要处理的shp文件
# input_shp = r"C:\Users\18292\Desktop\1.矢量空间数据\统一坐标\610632ZDJZD.shp"

# # 输出属性表中的字段名
# output_fields = ["FID", "DJZQ", "XZBZ"]

# # 添加一个新的字段名
# new_field = "JZD"

# # 读取属性表中的数据并进行排序和分组
# data = {} # 用一个字典来存储每一行的数据，用FID字段作为键
# groups = {} # 用一个字典来存储每个分组的数据，用DJZQ字段作为键
# with arcpy.da.SearchCursor(input_shp, output_fields) as cursor:
#     for row in cursor:
#         data[row[0]] = list(row) # 将每一行的数据添加到data字典中，以FID值为键
#         if row[1] not in groups: # 如果DJZQ值不在groups字典中
#             groups[row[1]] = [] # 就创建一个空列表
#         groups[row[1]].append(row[0]) # 将FID值添加到对应的DJZQ列表中
#     for djzq, rows in groups.items(): # 遍历每个分组
#         rows.sort(key=lambda x: data[x][2], reverse=True) # 在每个分组内按照XZBZ字段进行降序排名
#         prev_xzbz = None # 记录上一行的XZBZ值
#         jzd = 0 # 记录JZD值
#         rank = 1 # 记录当前的序号
#         for i, row in enumerate(rows): # 给每一行添加一个新的JZD字段
#             if i > 0 and data[row][2] == prev_xzbz: # 如果当前行的XZBZ值和上一行的XZBZ值相等
#                 jzd += 1 # 就让JZD值加一
#             else: # 否则
#                 jzd = rank # 就让JZD值等于当前的序号
#             data[row].append(jzd) # 添加JZD值到data字典中对应的行中
#             prev_xzbz = data[row][2] # 更新上一行的XZBZ值
#             rank += 1 # 更新当前的序号

# # 打印排序和分组后的结果
# for row in data.values():
#     print(row[0])

# # 将结果写入新的属性表
# arcpy.AddField_management(input_shp, new_field, "LONG") # 添加一个新的字段
# with arcpy.da.UpdateCursor(input_shp, output_fields + [new_field]) as cursor:
#     for row in cursor:
#         key = row[0] # 用FID字段作为键，匹配新的JZD字段的值
#         if key in data: # 如果键存在于data字典中，说明有对应的排名结果
#             row[-1] = data[key][-1] # 将新的JZD字段值写入属性表
#             cursor.updateRow(row)

# print("done")

import arcpy
from itertools import groupby

# 定义一个函数，参数为input_shp, fid_field, djzq_field, xzbz_field, jzd_field
def process_shp(input_shp, fid_field, djzq_field, xzbz_field, jzd_field):

    # 输出属性表中的字段名
    output_fields = [fid_field, djzq_field, xzbz_field]

    # 读取属性表中的数据并进行排序和分组
    data = {} # 用一个字典来存储每一行的数据，用FID字段作为键
    groups = {} # 用一个字典来存储每个分组的数据，用DJZQ字段作为键
    with arcpy.da.SearchCursor(input_shp, output_fields) as cursor:
        for row in cursor:
            data[row[0]] = list(row) # 将每一行的数据添加到data字典中，以FID值为键
            if row[1] not in groups: # 如果DJZQ值不在groups字典中
                groups[row[1]] = [] # 就创建一个空列表
            groups[row[1]].append(row[0]) # 将FID值添加到对应的DJZQ列表中
        for djzq, rows in groups.items(): # 遍历每个分组
            rows.sort(key=lambda x: data[x][2], reverse=True) # 在每个分组内按照XZBZ字段进行降序排名
            prev_xzbz = None # 记录上一行的XZBZ值
            jzd = 0 # 记录JZD值
            rank = 1 # 记录当前的序号
            for i, row in enumerate(rows): # 给每一行添加一个新的JZD字段
                if i > 0 and data[row][2] == prev_xzbz: # 如果当前行的XZBZ值和上一行的XZBZ值相等
                    jzd += 1 # 就让JZD值加一
                else: # 否则
                    jzd = rank # 就让JZD值等于当前的序号
                data[row].append(jzd) # 添加JZD值到data字典中对应的行中
                prev_xzbz = data[row][2] # 更新上一行的XZBZ值
                rank += 1 # 更新当前的序号

    # 打印排序和分组后的结果
    for row in data.values():
        print(row[0])

    # 将结果写入新的属性表
    arcpy.AddField_management(input_shp, jzd_field, "LONG") # 添加一个新的字段
    with arcpy.da.UpdateCursor(input_shp, output_fields + [jzd_field]) as cursor:
        for row in cursor:
            key = row[0] # 用FID字段作为键，匹配新的JZD字段的值
            if key in data: # 如果键存在于data字典中，说明有对应的排名结果
                row[-1] = data[key][-1] # 将新的JZD字段值写入属性表
                cursor.updateRow(row)

# 调用函数，传入参数，例如：
process_shp(r"C:\Users\18292\Desktop\1.矢量空间数据\统一坐标\610632ZDJZD.shp", "FID", "DJZQ", "XZBZ", "JZD")
