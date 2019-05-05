#!/usr/bin/env python 
# -*- coding:utf-8 -*-

CONFIG_INFO = {
    "exe_driver": r"D:\webdriver\chromedriver.exe",
}

URL = r"https://pc.xuexi.cn/points/login.html"
ENV_INFO = {
    "my_points": r"https://pc.xuexi.cn/points/my-points.html",
    "main": r"https://www.xuexi.cn/",


}

XPATH = {
    "login": {
        # "success": '//*[@id="app"]/div/div[2]/div/div[2]/div[2]',
        "success": '//*[@id="C9mf8i306alg00"]',
    },
    "read": {
        "news": '//*[@data-data-id="grid-business-title"]/div/div/div/div/section/div/div/div/div/section/div/div/div/div[2]/section/div/div/div[1]/div[{}]/div/div/div/span',
    }
}

VIDEO_ADDR = [
    "https://www.xuexi.cn/85c40e1e5c1c9cd1a1f5200e7190481e/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/9055eadcc926f57cdad0f8a3f4616282/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/b2e6c76c701a55c1d91859280ef2d055/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/df88e0a951ad120d62c9ec6554d90b27/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/4a849430a8138e9325953f803fc3bcb0/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/c6902003f6fc345a4f117e178475bebf/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/154d305bb6f5d0abfcfa33b83d35f06f/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/6fb7c4da38b5d93d1d48dcb1e91bc06d/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/a1edd29930d511fc16628b093823d498/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/ca634c7a2e30e9d2ae5c86bec94ea9aa/cf94877c29e1c685574e0226618fb1be.html",
    "https://www.xuexi.cn/ba388f05ef16c9a9236daab45344f0be/cf94877c29e1c685574e0226618fb1be.html",
]