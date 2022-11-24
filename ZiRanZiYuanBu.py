import requests
from bs4 import BeautifulSoup
from lxml import etree

url_pool = []
url_ex = "http://www.mnr.gov.cn/gk/tzgg"
targeturl = "http://www.mnr.gov.cn/gk/tzgg/"
first_level = requests.get(targeturl)

contenttree = etree.HTML(first_level.content)
alists = contenttree.xpath('//ul[@class = "ky_open_list"]/li/a')
for url in alists:
    article_title = url.xpath('./text()')[0]
    article_url = url.xpath('./@href')[0]
    if article_url[0] == "h":
        url_pool.append(article_url)
    else:
        article_url = url_ex + article_url[1:]
        url_pool.append(article_url)



second_level = requests.get(url_pool[0])
second_level.encoding = 'utf-8'

second_tree = etree.HTML(second_level.text)
tdlists = second_tree.xpath("//tr/td/text()")

mongo_content=[]
text_info = second_tree.xpath('//div[@class = "xx"]//text()')

# for text_if in text_info:
#     if '\n' not in text_if:
#         mongo_content.append(text_if.strip())

from pymongo import MongoClient

client = MongoClient()
db = client.zrzyb
tzgg = db.tzgg

tzgg.insert_one(
    {
    "名称":tdlists[0],
    "索引号":tdlists[1],
    "主题":tdlists[2],
    "发文字号":tdlists[3],
    "发布机构":tdlists[4],
    "生成日期":tdlists[5],
    "体裁":tdlists[6],
    "内容":text_info,
    }
)