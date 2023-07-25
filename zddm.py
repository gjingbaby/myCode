# -*- coding: utf-8 -*-
"""
python3.9

解决相同字段内容，添加序号问题，示例：
dm_field, dmxh_field
xxxx，1
xxxx，2
yyyy，1
yyyy，2
yyyy，3
"""

import arcpy
# 定义一个函数，参数为feature_class, zddm_field, zddmxh_field
def number_zddm(feature_class, dm_field, dmxh_field):
    # 创建一个字典，用来存储DM和DMXH（序号）的对应关系
    dm_dict = {}
    # 创建一个游标，用来遍历要素类中的每一行
    with arcpy.da.UpdateCursor(feature_class, [dm_field, dmxh_field]) as cursor:
        # 对于每一行
        for row in cursor:
            # 获取当前行的DM值
            dm = row[0]
            # 如果这个值已经在字典中，说明已经有一个序号了
            if dm in dm_dict:
                # 就把这个序号加一，作为新的序号
                dmxh = dm_dict[dm] + 1
                # 把这个序号赋值给当前行的DMXH字段
                row[1] = dmxh
                # 并且更新字典中的这个DM值对应的序号
                dm_dict[dm] = dmxh
            # 否则，说明这是一个新的ZDDM值，还没有序号
            else:
                # 就把序号设为1
                dmxh = 1
                # 把这个序号赋值给当前行的ZDDMXH字段
                row[1] = dmxh
                # 并且把这个ZDDM和ZDDMXH的对应关系存入字典中
                dm_dict[dm] = dmxh
            # 更新当前行的值
            cursor.updateRow(row)

# 调用函数，传入参数，例如：
feature_class = arcpy.GetParameterAsText(0)
dm_field = arcpy.GetParameterAsText(1)
dmxh_field = arcpy.GetParameterAsText(2)
number_zddm(feature_class, dm_field, dmxh_field)