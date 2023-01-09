from osgeo import gdal,ogr
import numpy as np
import matplotlib.pyplot as plt

# 打开影像
ds = gdal.Open(r'D:\yyktest\yyk10cmyyk.tif')

# 影像行列数，波段数
rows = ds.RasterYSize
cols = ds.RasterXSize
bands = ds.RasterCount

# 坐标变化六元素，左上角x，y坐标[0,3]，x,y方向旋转角度和比例尺
coord_list = ds.GetGeoTransform()

# 坐标信息
projection = ds.GetProjection()

# 波段对象
fst_band = ds.GetRasterBand(1)
sec_band = ds.GetRasterBand(2)
thr_band = ds.GetRasterBand(3)

# 获取波段对象的最小值，最大值（value）
fst_min = fst_band.GetMinimum()
fst_max = fst_band.GetMaximum()

# 栅格数据转数组
# jupyter 会报错，浪费一早上时间

# 3波段转换为3维数组
ds_arr = ds.ReadAsArray()
print(ds_arr.shape)
# 单波段转换为二维数组
fst_band_arr = fst_band.ReadAsArray()
print(fst_band_arr.shape)

# 对单波段数据拉伸显示
mean = np.mean(fst_band_arr)
std = np.std(fst_band_arr)
plt.imshow(fst_band_arr,cmap='gist_earth')
plt.show()


# import sys
# from osgeo import ogr 

# driver = ogr.GetDriverByName('ESRI Shapefile') #载入驱动
# filename = r'D:\yyktest\CJDCQ.shp'  # 不止需要.shp文件，还需要附带的其它信息文件
# dataSource = driver.Open(filename, 1) #第二个参数为0是只读，为1是可写
# if dataSource is None: #判断是否成功打开
#     print('could not open')
#     sys.exit(1)
# else:
#     print('done!')

# layer = dataSource.GetLayer(0)   #读取第一个图层

'''读出上下左右边界，坐标系为地理坐标系'''
extent = layer.GetExtent()
print ('extent:', extent)
print ('ul:', extent[0], extent[1]) #左右边界
print ('lr:', extent[2], extent[3]) #下上边界

n = layer.GetFeatureCount()     #该图层中有多少个要素
print ('feature count:', n)
feat = layer.GetFeature(0)		 #提取数据层中的第一个要素
area = feat.GetField("SHAPE_Area")   #读取该要素字段名为'FieldID'的值，注意读取'shape'字段会报错
print (area)
# geom = feat.GetGeometryRef() 		#提取该要素的轮廓坐标
# print (geom)

# 2. 【获取图层中所有要素】
feat = layer.GetNextFeature()
while feat:
    feat = layer.GetFeature()
    print(feat.GetField("SHAPE_Area"))
layer.ResetReading()

from osgeo import gdal
input_shape = r'D:\yyktest\CJDCQ.shp'
output_raster=r'D:\yyktest\test.tif'   
# tif输入路径，打开文件
input_raster = r"D:\yyktest\yyk10cmyyk.tif"
# 矢量文件路径，打开矢量文件
input_raster=gdal.Open(input_raster)
# 开始裁剪
ds = gdal.Warp(output_raster,
              input_raster,
              format = 'GTiff',
              cutlineDSName = input_shape,      
              cutlineWhere="FIELD = 'whatever'",
              dstNodata = 0)

import shapefile as sp

file = sp.Reader(r'D:\yyktest\CJDCQ.shp')

print(str(file.shapeType))  # 输出shp类型
print(file.encoding)# 输出shp文件编码
print(file.bbox)  # 输出shp的文件范围（外包矩形）
print(file.numRecords)  # 输出shp文件的要素数据
print(file.fields)# 输出所有字段信息



