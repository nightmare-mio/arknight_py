'''
Author: nightmare-mio wanglongwei2009@qq.com
Date: 2023-08-28 22:27:36
LastEditTime: 2023-08-29 00:03:49
Description: 请不要恶意请求
'''
import requests
import parsel



url='https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88'
headers={}

data=requests.get(url=url,headers=headers).text
selector=parsel.Selector(data)
divs=selector.xpath('//div[@id="filter-data"]/div')
row_count=0;
for div in divs:
    # 以下为wiki中所有的属性，有些本人并不认识
    # 名字zh
    
    zh=div.xpath('./@data-zh').get()
    # 职业
    profession=div.xpath('./@data-profession').get()
    # 稀有度
    rarity= div.xpath('./@data-rarity').get()
    logo= div.xpath('./@data-logo').get()
    birth_place= div.xpath('./@data-birth_place').get()
    team=div.xpath('./@data-team').get()
    race=div.xpath('./@data-race').get()
    en=div.xpath('./@data-en').get()
    ja=div.xpath('./@data-ja').get()
    id= div.xpath('./@data-id').get()
    hp=div.xpath('./@data-hp').get()
    atk=div.xpath('./@data-atk').get()
    D_def=div.xpath('./@data-def').get()
    res=div.xpath('./@data-res').get()
    re_deploy=div.xpath('./@data-re_deploy').get()
    cost=div.xpath('./@data-cost').get()
    block=div.xpath('./@data-block').get()
    interval=div.xpath('./@data-interval').get()
    sex=div.xpath('./@data-sex').get()
    position=div.xpath('./@data-position').get()
    tag=div.xpath('./@data-tag').get()
    obtain_method=  div.xpath('./@data-obtain_method').get()
    potential=div.xpath('./@data-potential').get()
    trust=div.xpath('./@data-trust').get()
    phy=div.xpath('./@data-phy').get()
    flex=div.xpath('./@data-flex').get()
    tolerance=div.xpath('./@data-tolerance').get()
    plan=div.xpath('./@data-plan').get()
    skill=div.xpath('./@data-skill').get()
    adapt=div.xpath('./@data-adapt').get()
    sortid=div.xpath('./@data-sortid').get()
    subprofession=div.xpath('./@data-subprofession').get()
    nation=div.xpath('./@data-nation').get()
    group=div.xpath('./@data-group').get()
    
    row = (
    zh + "|" + profession + "|" + rarity + "|" + logo + "|" +
    birth_place + "|" + team + "|" + race + "|" + en + "|" +
    ja + "|" + id + "|" + hp + "|" + atk + "|" + D_def + "|" +
    res + "|" + re_deploy + "|" + cost + "|" + block + "|" +
    interval + "|" + sex + "|" + position + "|" + tag + "|" +
    obtain_method + "|" + potential + "|" + trust + "|" +
    phy + "|" + flex + "|" + tolerance + "|" + plan + "|" +
    skill + "|" + adapt + "|" + sortid + "|" + subprofession + "|" +
    nation + "|" + group
)

    name="data.txt"
    row_count+=1
    with open('明日方舟\\'+name,mode='a', encoding='utf-8') as f:
            f.write(row+ '\n')
    print(str(row_count)+'打印成功！')

