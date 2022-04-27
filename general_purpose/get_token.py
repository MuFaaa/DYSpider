import asyncio
import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions

from general_purpose import RedisClient
from general_purpose.utilslog import HandleLog

log = HandleLog()

db = RedisClient.RedisClient(key='淘宝:token')


class GetKey(object):
    def __init__(self):
        option = ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        # option.add_argument(
        #     "--user-data-dir=" + '/Users/xianguowangguo/Library/Application Support/Google/Chrome/Default')
        option.add_argument('--headless')
        # option.add_argument(
        #     'user-agent=Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36')
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
        self.driver.quit()

    async def main(self):
        """
        关键函数生成key，并保存到数据库
        :return:
        """
        # self.driver.get('http://127.0.0.1:8000/a.html')
        self.driver.get('https://main.m.taobao.com/search/index.html?pageType=3&q=%E6%89%8B%E6%9C%BA')
        # self.driver.get(
        #     'https://item.taobao.com/item.htm?id=659653547177')
        time.sleep(0.4)

        cook = {}
        cookies = self.driver.get_cookies()
        # print(cookies)
        for i in cookies:
            cook[i['name']] = i['value']
        log.info(cook)
        # log.info(cook['isg'])
        # input('zzzz')
        db.save_key(str(cook), int(time.time()) + 1800)
        # db.set(str(cook))

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

def token_run():
    while True:
        GetKey().run_coroutines()
        db.del_key(0, int(time.time()))

if __name__ == '__main__':
    token_run()
    # while True:
    #     GetKey().run_coroutines()
    #     db.del_key(0, int(time.time()))
    # print(aaa)
