import asyncio
import time

import sentry_sdk
from selenium import webdriver
from selenium.webdriver import ChromeOptions

import RedisClient
# from utilslog import GetLog
from general_purpose.utilslog import HandleLog, SQLEngine

log = SQLEngine(name='get_isg.py')
# log = HandleLog('')
# log=GetLog().get_log()
db = RedisClient.RedisClient(key='唯品会:isg')
sentry_sdk.init(
    "http://f6a6fd98b8a54de087c42e85a7d7d9fb@127.0.0.1:9000/3",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

class GetKey(object):
    def __init__(self):
        option = ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(options=option)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => false
                })
                """
        })
        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})
        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})

    async def initialize(self):
        """
        创建多携程任务
        :return:
        """
        await asyncio.gather(*[self.main() for _ in range(1)])

    async def main(self):
        """
        关键函数生成key，并保存到数据库
        :return:
        """
        self.driver.get('https://www.vip.com/')
        time.sleep(0.4)

        cook={}
        cookies=self.driver.get_cookies()
        # print(cookies)
        for i in cookies:
            cook[i['name']]=i['value']
        # print(cook['isg'])
        log.info(cook)
        try:
            db.save_key(str(cook['mars_cid']).split('_')[1],int(time.time())+300)
        except:
            log.error('当前文件get_isg请检查redis服务器')
        # db.set(cook['isg'])


    def run_coroutines(self):
        """
        启动多携程任务
        :return:
        """
        try:
            asyncio.get_event_loop().run_until_complete(self.initialize())
        except Exception as f:
            print(f)
        # print(data)


if __name__ == '__main__':
    while True:
        GetKey().run_coroutines()
        db.del_key(0, int(time.time()))
    # print(aaa)