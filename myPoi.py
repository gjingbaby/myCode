import requests
import matplotlib.pyplot as plt
import json
import geopandas as gpd
from shapely.geometry import Polygon



# search_parameter = {
#     'query':'二级',
#     'tag':'一级',
#     'region':'行政区',
#     'ak':'token',
# }

# location_api = 'https://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=长安区&output=json&ak=G2vA8DVGuVk3ed4M7r7uHzIO5lHDDu40'

# test_url= 'http://api.map.baidu.com/place/v2/search?query=美食&page_size=10&page_num=0&scope=1&bounds=39.915,116.404,39.975,116.414&output=json&ak=G2vA8DVGuVk3ed4M7r7uHzIO5lHDDu40'

# c = requests.get(test_url)
# items = c.json()
# print(items)

class mypoispider():

    #获取行政区范围
    def districts(district_code):
        #根据行政代码获取行政边界json
        url='https://geo.datav.aliyun.com/areas_v2/bound/'+str(district_code)+'.json'
        #读取到geopandas
        district_coord = gpd.read_file(url)
        #获取四至
        #X,经度；Y,纬度
        X1 = district_coord.iloc[0].geometry.bounds[0]  # 最左
        Y1 = district_coord.iloc[0].geometry.bounds[1]  # 最下
        X2 = district_coord.iloc[0].geometry.bounds[2]  # 最右
        Y2 = district_coord.iloc[0].geometry.bounds[3]  # 最上
        
        # #构造外接矩形面
        # bounds=Polygon([(X1,Y1),(X1,Y2),(X2,Y2),(X2,Y1)])
        # #转换成geopandas数据格式，crs为坐标系
        # region = gpd.GeoDataFrame(geometry=gpd.GeoSeries([bounds]),crs=4326)

        # district_coord.plot()
        # region.plot()
        # plt.show()

        return [X1, Y1, X2, Y2]
        

    #创建格网
    def creat_grid(rectangle_coordinates,grid_num):
        
        x1 = rectangle_coordinates[0]
        y1 = rectangle_coordinates[1]
        x2 = rectangle_coordinates[2]
        y2 = rectangle_coordinates[3]

        x_item = abs((x1-x2)/grid_num)
        y_item = abs((y1-y2)/grid_num)
        
        print("y_item:",y_item,'/n',"x_item:",x_item)

        grid_list = []
        #左，右，上，下
        for row in range(grid_num):
            for column in range(grid_num):
                x_l = x1+row*x_item
                x_r = x1+(row+1)*x_item
                y_d = y1+column*y_item
                y_u = y1+(column+1)*y_item
                
                grid_list.append([(x_l,y_d),(x_l,y_u),(x_r,y_u),(x_r,y_d)])
                
                #可视化
                # grid_bounds=Polygon([(x_l,y_d),(x_l,y_u),(x_r,y_u),(x_r,y_d)])
                
                # grid_region = gpd.GeoDataFrame(geometry=gpd.GeoSeries([grid_bounds]),crs=4326)
                
                # grid_region.plot()
                
                # plt.show()
        
        return grid_list
        

    #poi爬取
    def poi_spider(grid_list,query,ak):
        n = 0
        for i in grid_list:
            bounds = "%f,%f,%f,%f"%(list(i[1])[::-1][0],list(i[1])[::-1][1],list(i[3])[::-1][0],list(i[3])[::-1][1])
            print(bounds)
            for j in range(20):
                params = {
                    "query":query,
                    'bounds':bounds,
                    'page_size':20,
                    'page_num':j,
                    'output':'json',
                    'ak':ak,
                }
                headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'
                }

                url = 'http://api.map.baidu.com/place/v2/search?'
                grid_poi = requests.get(url, params=params,headers=headers)
                print('切片%d'%n,"第%d页"%j)
                print(grid_poi.json())
                
            n+=1

    def save_poi():
        pass


    #启动函数
    def run(district_code,grid_num,query,ak):
        rectangle_coordinates = mypoispider.districts(district_code)
        grid_list = mypoispider.creat_grid(rectangle_coordinates,grid_num)       
        mypoispider.poi_spider(grid_list,query,ak)
        


if __name__ == '__main__':
    mypoispider.run('610116',2,'美食','G2vA8DVGuVk3ed4M7r7uHzIO5lHDDu40')