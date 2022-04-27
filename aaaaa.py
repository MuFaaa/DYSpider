# -*- coding: utf-8 -*-
import json

import jsonpath
import mitmproxy.http
from mitmproxy import ctx
from mitmproxy.tools.main import mitmdump

from general_purpose import MongodbClient

dy_save_data = MongodbClient.MongoDBClient('抖音', 'brand_data')

class Counter:
    def __init__(self):
        self.num = 0

    # 设置上游代理
    # def request(self, flow: mitmproxy.http.HTTPFlow):
    #     if flow.request.method == "CONNECT":
    #         return
    #     if flow.live:
    #         proxy = ('http://127.0.0.1', '9990')
    #         print(flow.request.host)
    #         flow.live.change_upstream_proxy_server(proxy)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 拦截包的信息
        if 'search-quic-lf.amemv.com' in flow.request.url:
            try:
                with open('搜索页返回结果.json','w')as f:
                    f.write(flow.response.text)
                data_json=json.loads(flow.response.text)
                name = jsonpath.jsonpath(data_json, "$..items..name")
                show_price = jsonpath.jsonpath(data_json, "$..items..show_price")
                img = jsonpath.jsonpath(data_json, "$..items..img")
                product_info = jsonpath.jsonpath(data_json, "$..items[*].product_info")
                goods_ratio = jsonpath.jsonpath(data_json, "$..items..goods_ratio")
                author = jsonpath.jsonpath(data_json, "$..author")
                sales = []
                nickname = []
                for i in product_info:
                    extra_info = jsonpath.jsonpath(i, "$.extra_info")
                    # print(extra_info)
                    if extra_info == False:
                        sales.append('NONE')
                    else:
                        sales.append(extra_info[0])
                parms = {}
                for z, x, c, v, b in zip(name, show_price, img, sales, goods_ratio):
                    parms['name'] = z
                    parms['show_price'] = str(x / 100)
                    parms['img'] = c
                    parms['sales'] = v
                    parms['goods_ratio'] = b
                    dy_save_data.sert({'name':z,'show_price':str(x / 100),'img':c,'sales':v,'goods_ratio':b})
                    print(parms)
            except:
                pass
        elif  'aweme/v2/shop/search' in flow.request.url:
            try:
                with open('搜索页返回结果.json', 'w') as f:
                    f.write(flow.response.text)
                data_json = json.loads(flow.response.text)
                name = jsonpath.jsonpath(data_json, "$..items..name")
                show_price = jsonpath.jsonpath(data_json, "$..items..show_price")
                img = jsonpath.jsonpath(data_json, "$..items..img")
                product_info = jsonpath.jsonpath(data_json, "$..items[*].product_info")
                goods_ratio = jsonpath.jsonpath(data_json, "$..items..goods_ratio")
                author = jsonpath.jsonpath(data_json, "$..author")
                sales = []
                nickname = []
                for i in product_info:
                    extra_info = jsonpath.jsonpath(i, "$.extra_info")
                    # print(extra_info)
                    if extra_info == False:
                        sales.append('NONE')
                    else:
                        sales.append(extra_info[0])
                parms = {}
                print(goods_ratio)
                print(name)
                for z, x, c, v, b in zip(name, show_price, img, sales, goods_ratio):
                    parms['name'] = z
                    parms['show_price'] = str(x / 100)
                    parms['img'] = c
                    parms['sales'] = v
                    parms['goods_ratio'] = b
                    dy_save_data.sert({'name':z,'show_price':str(x / 100),'img':c,'sales':v,'goods_ratio':b})
                    print(parms)

            except:
                pass


addons = [
    Counter()
]
if __name__ == '__main__':
    mitmdump(['-s', __file__, '-p', "9201"])