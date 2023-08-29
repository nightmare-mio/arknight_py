'''
Author: nightmare-mio wanglongwei2009@qq.com
Date: 2023-08-29 01:57:37
LastEditTime: 2023-08-29 16:52:40
Description: 
'''
import requests
import parsel
import os

data=""
# 此处使用笨方法 如有干员新增 需要更新img.txt文件
with open('明日方舟\\img.txt',mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        data += line
selector=parsel.Selector(data)
divs=selector.xpath('//div[@class="avatar-container"]/a/img')
for div in divs:
    # 图片路径
    img=div.xpath('./@data-src').get()
    # 文件名
    name=img.split('/')[-1]
    # 文件存储位置
    path='明日方舟\\avate\\'+name
    # 去重
    if not os.path.exists(path):
        img_data = requests.get(url=img, headers={}).content
        
        with open(path,mode='wb') as f:
                f.write(img_data)
        print(name+'打印成功！')