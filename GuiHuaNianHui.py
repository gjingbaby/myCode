
import requests
import os

url = ' http://yd.planning.cn/api/user/bookMenus/1' #2020年数据
# url = ' http://yd.planning.cn/api/user/bookMenus/2' #2021年数据

headers = {
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Host': 'yd.planning.cn',
'Referer': 'http://yd.planning.cn/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

ctt = requests.get(url,headers= headers)
ctt_dic = ctt.json()

print(len(ctt_dic['result']))

for i in range(5,len(ctt_dic['result'])):
    field_id = ctt_dic['result'][i]['id']
    field_name = ctt_dic['result'][i]['name']
    field_children = ctt_dic['result'][i]['children']
    print(i,field_id,field_name,len(field_children))
    if not os.path.isdir(field_name):
        os.mkdir(field_name)
    for j in range(0,len(field_children)):
        artical_url = 'http://47.104.3.138:18081/pdfs/' + str(field_id) + '/' + field_children[j]['name'] + '.pdf'
        artical_content = requests.get(artical_url).content
        filename = field_children[j]['name']+'.pdf'
        filepath = '%s/%s'%(field_name,filename)
    
        with open(filepath,'wb') as f:
            f.write(artical_content)
        f.close()
        print('     finished....',j,field_children[j]['name'])
      
       