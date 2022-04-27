# -*- encoding=utf8 -*-
__author__ = "xianguowangguo"

import logging
import random
import threading
import time



import RedisClient
from airtest.core.api import *
auto_setup(__file__)

log = logging.getLogger('airtest')
log.setLevel(logging.ERROR)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

dy_save_data = RedisClient.RedisClient(key='抖音:search')
# 连接本机默认端口连的设备号为123和456的两台手机
# auto_setup(__file__,devices=["Android://127.0.0.1:5037/192.168.0.105:5555","Android://127.0.0.1:5037/456"])




def page_commodity():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    while 1:
        try:
            if poco(name="com.ss.android.ugc.aweme:id/a=u").exists():
                print('当前处于商品页')
                time.sleep(2)
                # if poco(name="com.ss.android.ugc.aweme:id/bs0").exists():
                #     print('找到网络')
                #     continue
                # else:
                # poco(name="com.ss.android.ugc.aweme:id/et_search_kw").click()
                # poco(name="com.ss.android.ugc.aweme:id/btn_clear").click()
                # poco.click([0.808,0.069])
                touch(885,130)
                # poco(name="com.ss.android.ugc.aweme:id/et_search_kw").set_text('db5461-601')
                # poco(name="com.ss.android.ugc.aweme:id/jw=").click()
            else:
                if poco(name="com.ss.android.ugc.aweme:id/tv_title").exists():
                    print('搜索结果为空')
                    poco(text="综合").click()
                    if poco(name="com.ss.android.ugc.aweme:id/tv_title").exists():
                        print('点击地点依然为空')
                        start_app("com.yztc.studio.plugin")
                        time.sleep(10)
                        poco(text="抹机清理").click()
                        while 1:
                            if poco(name="com.yztc.studio.plugin:id/wipe_task_tv_msg").exists():
                                print('正在刷机')
                                sleep(30)
                                poco.click([0.438,0.189])
                            # if poco(text="任务结束-点击返回").exists():
                            #     poco(text="任务结束-点击返回").click()
                                home()
                                break
                    # m4.join()
                    # if poco(text="登录后可体验完整搜索功能").exists():
                    #     print('达到每日上线，需刷机后再次爬取，启动刷机流程')
                    #     # 返回桌面
                    #     home()
                    # else:
                    #     poco(name="com.ss.android.ugc.aweme:id/et_search_kw").click()
                    # poco(name="com.ss.android.ugc.aweme:id/btn_clear").click()
                continue
        except:
            continue


# def search_error():
#     if poco(text="登录后可体验完整搜索功能").exists():
#         print('达到每日上线，需刷机后再次爬取，启动刷机流程')

def search_color():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    while 1:
        if poco(text="欢迎体验抖音浅色模式").exists():
            print('发现浅色模式')
            poco(name="com.ss.android.ugc.aweme:id/iv_close").click()
        else:
            sleep(20)


def page_synthesize():

     poco(text="商品").click()


# def page_search_two():
#     poco(name="com.ss.android.ugc.aweme:id/btn_clear").click()

def index():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    while 1:
        try:

            if poco(name="浏览器").exists():
                print('桌面')
                # 返回手机桌面
                # home()
                # 根据包名启动app
                poco(name="net.oneplus.launcher:id/all_apps_handle").click()
                # stop_app("com.ss.android.ugc.aweme")
                # time.sleep(5)
                # start_app("com.ss.android.ugc.aweme")
        except:
            continue


def index_list():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    while 1:
        try:
            if poco(name="net.oneplus.launcher:id/icon").exists():
                print('当前在应用列表')
                poco(text="抖音").click()
                time.sleep(10)
                poco.swipe([0.5, 0.8], [0.5, 0.2],duration=0.5)
                time.sleep(2)
        except:
            continue


def index_dy():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    while 1:
        try:
            if poco(name="com.ss.android.ugc.aweme:id/a_w").exists():
                print('出现个人信息保护指引')
                poco(text="同意").click()
                time.sleep(10)
        except:
            continue




def index_young():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    while 1:
        try:
            if poco(name="com.ss.android.ugc.aweme:id/inq").exists():
                print('出现青少年提示')
                poco(name="com.ss.android.ugc.aweme:id/-c").click()
        except:
            continue


def page_search():

        data = random.choice(list(dy_save_data.getall())).decode()
        # poco.click([0.418,0.072])
        touch([594,137])
        text(data)
        touch([996, 130])
        # poco(name="com.ss.android.ugc.aweme:id/et_search_kw").click()
        # text(data)
        # poco(name="com.ss.android.ugc.aweme:id/et_search_kw").set_text(data)
        # poco.click([0.916, 0.066])



def page_video():
        try:
            if exists(Template('img/个人信息保护.png'),timeout=2):
                print('出现个人信息保护指引')
                touch(Template("img/同意.png"))

                # poco(text="同意").click()
                time.sleep(2)
                poco.swipe([0.5, 0.8], [0.5, 0.2],duration=0.5)
                time.sleep(2)
                poco.click([0.918, 0.059])
        except:
            poco.swipe([0.5, 0.8], [0.5, 0.2],duration=0.5)
            time.sleep(1)
            poco.click([0.918, 0.059])
            pass

                    # if poco(name="com.ss.android.ugc.aweme:id/dqy").exists():
                        #         # 如果出现欢迎搜索图标点击
                        # poco(name="com.ss.android.ugc.aweme:id/dqy").click()
def qingli():
    # poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    # poco(exists(Template("img/抹机清理.png"))).click()
    poco.click([0.473,0.182])
    while 1:
        if poco(name="com.yztc.studio.plugin:id/wipe_task_tv_msg").exists():
            print('正在刷机')
            sleep(60)
            poco.click([0.438, 0.189])
            home()
            break

def judge():
    if poco(text="推荐").exists():
        print('当前处于视频页')
        time.sleep(2)
        page_video()
    elif poco(name="android.widget.ImageButton").exists():
        print('当前处于搜索页')
        page_search()
    elif poco(text="综合排序").exists():
        print('当前处于综合页')
        poco.swipe([0.821, 0.132],[0.195, 0.132],duration=0.5)
        sleep(1)
        poco(text="商品").click()
    elif poco(name="com.ss.android.ugc.aweme:id/a=u").exists():
        print('当前处于商品页')
        sleep(1)
        # while 1:
            # if poco(name="com.ss.android.ugc.aweme:id/bs0").exists():
            #     print('等待网络')
            # else:
        touch([876,127])
                # break
        # poco.click([0.808, 0.069])
                # break
    elif poco(name="com.ss.android.ugc.aweme:id/tv_title").exists():
        print('搜索结果为空')
        poco.swipe([0.195, 0.132],[0.821, 0.132],duration=0.5)
        sleep(1)
        poco(text="综合").click()
        if poco(name="com.ss.android.ugc.aweme:id/tv_title").exists():
            print('点击综合依然为空')
            poco.swipe([0.821, 0.132], [0.195, 0.132],duration=0.5)
            sleep(1)
            poco(text="地点").click()
            if poco(name="com.ss.android.ugc.aweme:id/gc4").exists():
                poco(text="商品").click()
                poco.click([0.808, 0.069])
        else:
            poco.click([0.808, 0.069])

        if poco(name="com.ss.android.ugc.aweme:id/tv_title").exists():
            print('多次检查都为空,查看热榜搜索是否为空')
            keyevent("BACK")
            # poco.click([0.808, 0.069])
            time.sleep(1)
            poco.click([0.371, 0.747])
            time.sleep(1)
        if poco(name="com.ss.android.ugc.aweme:id/tv_title").exists():
            print('热榜为空，开始刷机')
            time.sleep(1)
            start_app("com.yztc.studio.plugin")
            time.sleep(5)
            poco.click([0.473, 0.182])
            while 1:
                if poco(text="一键清理玩命运行中").exists():
                    print('正在刷机')
                elif poco(text="任务结束-点击返回").exists():
                    poco(text="任务结束-点击返回").click()
                    time.sleep(1)
                    home()
                    break
                # poco.click([0.46, 0.255])
                # home()

                # AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


    elif poco(name="com.ss.android.ugc.aweme:id/gc4").exists():
        print("当前地点页")
        poco(text="商品").click()
    elif poco(name="浏览器").exists():
        print('桌面')
        # 返回手机桌面
        # home()
        # 根据包名启动app
        touch([536,1667])
        print('点击应用列表')
        # poco(name="net.oneplus.launcher:id/all_apps_handle").click()
        # stop_app("com.ss.android.ugc.aweme")
        time.sleep(2)
    elif poco(name="net.oneplus.launcher:id/icon").exists():
        print('当前在应用列表')
        poco(text="抖音").click()
        time.sleep(5)
        # poco.swipe([0.5, 0.8], [0.5, 0.2])
        # time.sleep(2)
    elif poco(name="com.ss.android.ugc.aweme:id/a_w").exists():
                print('出现个人信息保护指引')
                poco(text="同意").click()
                time.sleep(3)
    elif poco(text="拒绝").exists():
        print('授权权限')
        poco(text="拒绝").click()
        time.sleep(2)
        poco.swipe([0.5, 0.8], [0.5, 0.2],duration=0.5)
        time.sleep(2)
        poco.click([0.918, 0.059])
    elif poco(name="com.ss.android.ugc.aweme:id/inq").exists():
            print('出现青少年提示')
            poco(name="com.ss.android.ugc.aweme:id/-c").click()
    elif poco(text="欢迎体验抖音浅色模式").exists():
            print('发现浅色模式')
            poco(name="com.ss.android.ugc.aweme:id/iv_close").click()
    else:
        home()

# page_video()
while 1:
    try:
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        judge()
        # time.sleep(120)
    except:
        # time.sleep(10)
        while 1:
            try:
                auto_setup(__file__, devices=["Android://127.0.0.1:5037/192.168.0.100:5555"])
                break
            except:
                continue
        continue

