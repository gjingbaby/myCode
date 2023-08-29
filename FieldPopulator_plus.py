# -*- coding: utf-8 -*-

"""
给字段赋值，需提供字段的（名字：值）
"""

import arcpy

def Field_populate(shp_file, xzqdm_field, xmc_field,pici):
    #获取所有字段名称
    field_names = [field.name for field in arcpy.ListFields(shp_file)]
    # 添加唯一值字段作为替换字段
    unique_field = "UniqueID"
    if unique_field not in field_names:
        arcpy.AddField_management(shp_file, unique_field, "LONG")
        count = 1
        with arcpy.da.UpdateCursor(shp_file, [unique_field]) as cursor:
            for row in cursor:
                row[0] = count
                cursor.updateRow(row)
                count += 1
        print('-------------------------添加UniqueID字段---------------------')

    # 添加JCBH字段
    
    jcbh_field = "JCBH"
    if jcbh_field not in field_names:
        arcpy.AddField_management(shp_file, jcbh_field, "TEXT")
        print('-------------------------检查JCBH字段---------------------')
    

    # 计算XZQDM和XMC字段的值
    # 计算XZQDM和XMC字段的值    
    arcpy.CalculateField_management(shp_file, "XZQDM",xzqdm_field, "PYTHON_9.3")
    arcpy.CalculateField_management(shp_file, "XMC",'"' + xmc_field + '"', "PYTHON_9.3")
    print('-------------------------计算XZQDM、XMC字段---------------------')

    #创建临时文件
    temp_output = arcpy.CreateUniqueName("temp_output.shp", r"D:\temp")
    print('-------------------------创建临时文件---------------------')
    sort_fields = [["Shape", "ASCENDING"]]
    spatial_sort_method = "UL"
    arcpy.Sort_management(shp_file, temp_output, sort_fields, spatial_sort_method)
    print('-------------------------空间排序结束---------------------')
    order_list = []
    with arcpy.da.SearchCursor(temp_output, ["FID", "UniqueID", "XZQDM", "XMC"]) as cursor:
        for row in cursor:
            fid = row[0]
            UniqueID = row[1]

            # 更新输入文件JCBH字段的值
            with arcpy.da.UpdateCursor(shp_file, [jcbh_field, "UniqueID",'JCLX']) as update_cursor:
                for update_row in update_cursor:
                    if update_row[1] == UniqueID:
                        update_row[0] = str(pici)  + str(update_row[2]) + str(fid + 1)
                        #update_row[0] = str(fid + 1)
                        update_cursor.updateRow(update_row)
                        break

            order_list.append(fid)
        print('-------------------------计算JCBH字段结束---------------------')

    # 计算HSX字段的值
    arcpy.CalculateField_management(shp_file, "HSX", "'2023Q1'", "PYTHON_9.3")
    print('-------------------------计算HSX字段---------------------')

    # 计算XZB和YZB字段的值，根据坐标系
    arcpy.CalculateField_management(shp_file, "XZB", "!SHAPE.CENTROID.X!", "PYTHON_9.3")
    arcpy.CalculateField_management(shp_file, "YZB", "!SHAPE.CENTROID.Y!", "PYTHON_9.3")
    print('-------------------------计算XZB，YZB字段---------------------')
    
    # 计算JCMJ字段的值，亩
    arcpy.CalculateField_management(shp_file, "JCMJ", "!SHAPE.AREA!*0.0015", "PYTHON_9.3")
    print('-------------------------计算JCMJ字段(亩)---------------------')

    del cursor
    del update_cursor
    arcpy.ClearWorkspaceCache_management()  # 清除工作空间缓存


    # 删除字段
    arcpy.DeleteField_management(shp_file, "UniqueID")
    #删除临时文件
    arcpy.Delete_management(temp_output)
    print('-------------------------清理临时字段和文件完成---------------------')


if __name__ == "__main__":
    shp_ads = input(r"please input SHP_PATH:")
    xzqdm = input(r"please input XZQDM:")
    xmc = input(r"please input XMC:")
    print(shp_ads, xzqdm, xmc)
    Field_populate(shp_ads, xzqdm, xmc,"Ⅰ")
    print('-------------------------全部结束---------------------')
       


