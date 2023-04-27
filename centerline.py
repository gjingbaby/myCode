# -- coding:utf-8 --
# 导入arcpy模块和os模块
import arcpy
import os

def cenToline(workspace, filename, distance):
    # 设置工作空间
    arcpy.env.workspace = workspace

    # 检查Spatial Analyst扩展许可证
    arcpy.CheckOutExtension("Spatial")

    # 将多边形图层转换为线图层
    out_line = os.path.join(workspace, filename.split('.')[0] + '_line.shp')
    if arcpy.Exists(out_line):
        try:
            arcpy.Delete_management(out_line)
        except:
            # 删除失败则重命名该文件
            os.rename(out_line, out_line + '_bak')
            arcpy.AddWarning('文件已存在，重命名为 ' + out_line + '_bak')
    arcpy.PolygonToLine_management(filename, out_line)

    # 生成中心线
    out_centerline = os.path.join(workspace, filename.split('.')[0] + '_centerline.shp')
    if arcpy.Exists(out_centerline):
        try:
            arcpy.Delete_management(out_centerline)
        except:
            # 删除失败则重命名该文件
            os.rename(out_centerline, out_centerline + '_bak')
            arcpy.AddWarning('文件已存在，重命名为 ' + out_centerline + '_bak')
    arcpy.CollapseDualLinesToCenterline_cartography(out_line, out_centerline, str(distance)+' Meters')

if __name__ == '__main__':
    workspace = 'D:\data'
    filename = 'D:\Project\造林绿化\下发数据\宁陕\宁陕.shp'
    distance = 1000
    cenToline(workspace, filename, distance)

