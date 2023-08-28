'''
Author: nightmare-mio wanglongwei2009@qq.com
Date: 2023-08-28 22:27:36
LastEditTime: 2023-08-28 23:32:47
Description: 请不要恶意请求
'''
import requests
import parsel


url='https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88'
headers={}

data=requests.get(url=url,headers=headers).text
selector=parsel.Selector(data)
divs=selector.xpath('//div[@id="filter-data"]/div')
for div in divs:
    # 名字zh
    zh=div.xpath('./@data-zh').get()