# -*- coding: utf-8 -*-
'''
r"C:\Users\18292\Desktop\zrz\610632ZRZ.shp"

功能描述：
1.对一个要素类的属性表进行编号
2.给每个ZDDM值分配一个ZDDMXH值,表示它在同一个ZDDM分组中的序号
3.将编号结果写入属性表中的ZDDMXH字段
参数说明：
1.要处理的要素类的路径,例如r"C:\Users\18292\Desktop\zrz\610632ZRZ.shp"
2.要素类中的ZDDM字段,表示宗地代码
3.要素类中的ZDDMXH字段,表示宗地代码序号
'''


# import arcpy
# # 假设你的要素类是feature_class，ZDDM和ZDDMXH是两个字段
# # 创建一个字典，用来存储ZDDM和ZDDMXH的对应关系
# zddm_dict = {}
# # 创建一个游标，用来遍历要素类中的每一行
# with arcpy.da.UpdateCursor(r"C:\Users\18292\Desktop\zrz\610632ZRZ.shp", ["ZDDM", "ZDDMXH"]) as cursor:
#     # 对于每一行
#     for row in cursor:
#         # 获取当前行的ZDDM值
#         zddm = row[0]
#         # 如果这个值已经在字典中，说明已经有一个序号了
#         if zddm in zddm_dict:
#             # 就把这个序号加一，作为新的序号
#             zddmxh = zddm_dict[zddm] + 1
#             # 把这个序号赋值给当前行的ZDDMXH字段
#             row[1] = zddmxh
#             # 并且更新字典中的这个ZDDM值对应的序号
#             zddm_dict[zddm] = zddmxh
#         # 否则，说明这是一个新的ZDDM值，还没有序号
#         else:
#             # 就把序号设为1
#             zddmxh = 1
#             # 把这个序号赋值给当前行的ZDDMXH字段
#             row[1] = zddmxh
#             # 并且把这个ZDDM和ZDDMXH的对应关系存入字典中
#             zddm_dict[zddm] = zddmxh
#         # 更新当前行的值
#         cursor.updateRow(row)


import arcpy
# 定义一个函数，参数为feature_class, zddm_field, zddmxh_field
def number_zddm(feature_class, zddm_field, zddmxh_field):
    # 创建一个字典，用来存储ZDDM和ZDDMXH的对应关系
    zddm_dict = {}
    # 创建一个游标，用来遍历要素类中的每一行
    with arcpy.da.UpdateCursor(feature_class, [zddm_field, zddmxh_field]) as cursor:
        # 对于每一行
        for row in cursor:
            # 获取当前行的ZDDM值
            zddm = row[0]
            # 如果这个值已经在字典中，说明已经有一个序号了
            if zddm in zddm_dict:
                # 就把这个序号加一，作为新的序号
                zddmxh = zddm_dict[zddm] + 1
                # 把这个序号赋值给当前行的ZDDMXH字段
                row[1] = zddmxh
                # 并且更新字典中的这个ZDDM值对应的序号
                zddm_dict[zddm] = zddmxh
            # 否则，说明这是一个新的ZDDM值，还没有序号
            else:
                # 就把序号设为1
                zddmxh = 1
                # 把这个序号赋值给当前行的ZDDMXH字段
                row[1] = zddmxh
                # 并且把这个ZDDM和ZDDMXH的对应关系存入字典中
                zddm_dict[zddm] = zddmxh
            # 更新当前行的值
            cursor.updateRow(row)

# 调用函数，传入参数，例如：
number_zddm(r"C:\Users\18292\Desktop\zrz\610632ZRZ.shp", "ZDDM", "ZDDMXH")