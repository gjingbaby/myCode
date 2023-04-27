# -*- coding: utf-8 -*-

'''
代码实现了以下功能：
    1. 获取要素类中字段 "a" 的唯一值列表；
    2. 对于每个唯一的 "a" 值，使用数据访问搜索游标获取所有该值的行和 "b" 值；
    3. 将 "b" 值排序，然后为每个 "b" 值计算逆序等级，并将结果存储在字典中；
    4. 使用数据访问更新游标，为所有匹配要素的 "c" 值分配逆序值；
    5. 成功更新后输出消息 "Sorting and ranking complete."。
该代码实现了通过 Python 脚本对要素类进行排序和排名的功能，当要素类中存在多个 "a" 值时，可以为每个唯一的 "a" 值值的所有 "b" 值分别排序并分配排名（以逆序值的形式）。

以下是代码中每个参数的说明：
    input_fc：输入要素类的路径，其中需要进行排序和排名的字段包括 "a"、"b" 和 "c"；
    a_field：字符串类型，需要进行排序和排名的要素类的字段 "a" 的名称；
    b_field：浮点类型，需要进行排序和排名的要素类的字段 "b" 的名称；
    c_field：字符串类型，需要进行排序和排名的要素类的字段 "c" 的名称。
更具体地说，这些参数用于指定代码将在哪个要素类中执行排序和排名操作，以及要基于哪些字段执行排序和排名。 a_field 字段的唯一值将被用作分组标准，b_field 字段中的数值将被排序，c_field 的数值将设置为针对 "a" 和 "b" 字段的逆序等级。
'''

import arcpy

def sort_and_rank(input_fc, a_field, b_field, c_field):
    
    field_names = [a_field, b_field, c_field]

    # 获取 "a" 字段中的唯一值列表
    values_a = set([r[0] for r in arcpy.da.SearchCursor(input_fc, a_field)])

    # 针对 "a" 字段中每个唯一值，获取 "b" 值的所有行
    for a_value in values_a:

        # 创建一个列表来存储 "b" 值
        b_values = []

        # 使用搜索游标获取所有匹配 "a" 值的行和 "b" 值
        with arcpy.da.SearchCursor(input_fc, field_names, "{}='{}'".format(a_field, a_value)) as cursor:
            for row in cursor:
                b_values.append(row[1])

        # 对 "b" 值进行升序排列
        b_values.sort()

        # 创建字典来存储 b-value/count 对
        count_dict = {}
        for idx, b_value in enumerate(b_values, start=1):
            count_dict[b_value] = len(b_values) - idx + 1

        # 使用更新游标更新 "c" 值
        with arcpy.da.UpdateCursor(input_fc, field_names, "{}='{}'".format(a_field, a_value)) as cursor:
            for row in cursor:
                row[2] = count_dict[row[1]]
                cursor.updateRow(row)

    arcpy.AddMessage("排序和排名完成。")


input_fc = r"C:\Users\18292\Desktop\maqinqin\610632黄陵县\1.矢量空间数据\统一坐标\610632ZDJZD.shp"
sort_and_rank(input_fc, "GG", "XZBZ", "OLD_JZD")
