import geopandas as gpd
import matplotlib.pyplot as plt
import json,requests


test_url= 'http://api.map.baidu.com/place/v2/search?query=美食&page_size=10&page_num=0&scope=1&bounds=39.915,116.404,39.975,116.414&output=json&ak=G2vA8DVGuVk3ed4M7r7uHzIO5lHDDu40'

c = requests.get(test_url)
items = c.json()
print(items)