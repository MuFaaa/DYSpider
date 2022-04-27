import json

import jsonpath

with open('json测试.json','r')as f:
    data=f.read()
data_json = json.loads(data)
name = jsonpath.jsonpath(data_json, "$..items..name")
show_price = jsonpath.jsonpath(data_json, "$..items..show_price")
img = jsonpath.jsonpath(data_json, "$..items..img")
product_info = jsonpath.jsonpath(data_json, "$..items[*].product_info")
goods_ratio = jsonpath.jsonpath(data_json, "$..items..goods_ratio")
author = jsonpath.jsonpath(data_json, "$..author")
sales=[]
nickname=[]
for i in product_info:
    extra_info = jsonpath.jsonpath(i, "$.extra_info")
    # print(extra_info)
    if extra_info==False:
        sales.append('NONE')
    else:
        sales.append(extra_info[0])
parms={}
for z,x,c,v,b in zip(name,show_price,img,sales,goods_ratio):
    parms['name']=z
    parms['show_price']=str(x/10)
    parms['img']=c
    parms['sales']=v
    parms['goods_ratio']=b
    print(parms)
