#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *


class Browser:
    def __init__(self, config_info, env_info, xpath):
        self.config_info = config_info
        self.env_info = env_info
        self.xpath = xpath
        self.driver = self._login()

    def __del__(self):
        self.driver.quit()

    def _login(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_driver = self.config_info["exe_driver"]  # chromedriver的路径
        driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
        driver.maximize_window()

        driver.get(URL)
        print("{0}\n请使用软件扫码登录。\n{0}".format("*" * 20))
        while True:
            try:
                text = driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/div/div/div[1]/div/a[3]/div/div[2]/div[1]/span').text
                if "学习积分" in text:
                    # print("登录成功")
                    break
            except:
                # print("请使用软件扫码登录。")
                time.sleep(1)

        return driver

    def refresh(self, sleep_time=2):
        self.driver.refresh()
        time.sleep(sleep_time)

    def operate(self, key1, key2, action, value=None, index=-1):
        if index < 0:
            if action == "click":
                return self.driver.find_element_by_xpath(self.xpath[key1][key2]).click()
            elif action == "clear":
                return self.driver.find_element_by_xpath(self.xpath[key1][key2]).clear()
            elif action == "send_keys":
                return self.driver.find_element_by_xpath(self.xpath[key1][key2]).send_keys(value)
        else:
            if action == "click":
                return self.driver.find_elements_by_xpath(self.xpath[key1][key2])[index].click()
            elif action == "clear":
                return self.driver.find_element_by_xpath(self.xpath[key1][key2])[index].clear()
            elif action == "send_keys":
                return self.driver.find_element_by_xpath(self.xpath[key1][key2])[index].send_keys(value)

    def get_page(self, page_name, sleep_time=2):
        self.driver.get(self.env_info[page_name])
        time.sleep(sleep_time)

    def get_text(self, key1, key2, index=-1, wait_time=15):
        if not wait_time:
            if index < 0:
                return self.driver.find_element_by_xpath(self.xpath[key1][key2]).text
            else:
                return self.driver.find_elements_by_xpath(self.xpath[key1][key2])[index].text
        else:
            locator = (By.XPATH, self.xpath[key1][key2])
            if index < 0:
                return WebDriverWait(self.driver, wait_time, 0.5).until(EC.presence_of_element_located(locator)).text
            elif index >= 0:
                return WebDriverWait(self.driver, wait_time, 0.5).until(EC.presence_of_all_elements_located(locator))[
                    index].text


def get_points_state(browser):
    browser.get_page("my_points")
    print("今日积分获取情况")
    read_point = browser.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]').text
    video_point = browser.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[3]/div[2]/div[1]/div[2]').text
    print("阅读积分：{0}".format(read_point))
    print("视频积分：{0}\n{1}".format(video_point, "*" * 20))
    return {
        "read_point": int(read_point.split('/')[0][0]),
        "read_point_all": int(read_point.split('/')[1][0]),
        "video_point": int(video_point.split('/')[0][0]),
        "video_point_all": int(video_point.split('/')[1][0]),
    }


def read_one_article(browser, num):
    locator = (By.XPATH, browser.xpath["read"]["news"].format(str(num)))
    WebDriverWait(browser.driver, 15, 0.5).until(EC.presence_of_element_located(locator)).click()
    # browser.driver.find_element_by_xpath(browser.xpath["read"]["news"].format(str(num))).click()
    # todo 增加滚动
    # length = 100
    # for i in range(4):
    #     js = "var q=document.body.scrollTop=" + str(length)
    #     browser.driver.execute_script(js)
    #     time.sleep(5)
    #     length += length
    print("正在阅读中...等待两分钟。")
    time.sleep(120)


def read_article(browser, num):
    need_read_num = num
    print("{0}\n开始阅读文章，总共需要阅读{1}篇".format("*" * 20, need_read_num))
    while need_read_num:
        print("尚需阅读{}篇文章".format(need_read_num))
        browser.get_page("main")
        # todo 阅读第几篇设置为随机的，8选6
        read_one_article(browser, need_read_num)
        need_read_num -= 1

    print("阅读文章结束\n{}".format("*" * 20))
    return True


def watch_video(browser, num):
    need_watch_num = num
    print("开始观看视频，共需观看{}部".format(need_watch_num))
    while need_watch_num:
        print("尚需观看视频{}部，每部观看三分钟...".format(need_watch_num))
        browser.driver.get(VIDEO_ADDR[need_watch_num])
        time.sleep(190)
        need_watch_num -= 1

    # todo 通过点击进入视频
    # browser.get_page("main")
    # # browser.driver.find_element_by_xpath('//*[@data-data-id="sider-impress-title"]/div/div[1]/span').click()
    # browser.driver.find_element_by_xpath('//*[@data-data-id="shibo-platform-title"]/div/div[1]/span').click()
    # browser.driver.find_element_by_xpath(
    #     '//*[@id="root"]/div/section/div/div/div/div/section/div/div/div/div/section/div/div/div/div/section/div/div/div/div[3]/section/div/div/div/div/div/section/div[3]/section/div/div/div[1]/div[1]/div/div/div[1]/span')
    return True


def auto_get_points(browser):
    # 获取当前积分情况
    points_state = get_points_state(browser)
    # 读文章 2分钟1篇
    while points_state["read_point"] != points_state["read_point_all"]:
        # 阅读积分未满，开始阅读文章
        read_article(browser, points_state["read_point_all"] - points_state["read_point"])
        points_state = get_points_state(browser)
    # 看视频 3分钟1部
    while points_state["video_point"] != points_state["video_point_all"]:
        # 视频积分未满，开始观看视频
        watch_video(browser, points_state["video_point_all"] - points_state["video_point"])
        points_state = get_points_state(browser)
    # 任务结束
    return True


if __name__ == '__main__':
    # 登录
    browser = Browser(CONFIG_INFO, ENV_INFO, XPATH)
    # 自动获取积分
    auto_get_points(browser)
    # 任务结束
    del browser
