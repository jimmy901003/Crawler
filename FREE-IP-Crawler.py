# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 01:10:05 2023

@author: user
"""

import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import html5lib
import re
import parsel
from lxml import etree
#解析原始碼

# response = requests.get('https://api64.ipify.org?format=json')
# print(response.json()['ip'])

driver = webdriver.Chrome()
url = 'https://www.freeproxylists.net/zh/'
driver.get(url)
time.sleep(3)
# 取得網頁原始碼
response = driver.page_source
# print(response)
# 關閉 webdriver
driver.quit()

html = etree.HTML(response)

ip_list = html.xpath('/html/body/div[1]/div[2]/table/tbody/tr[position() > 1]/td[1]/a/text()')
port_list = html.xpath('/html/body/div[1]/div[2]/table/tbody/tr/td[2]/text()')
# print(ip_list)
# print(port_list)
ip_port_list = []
detail = dict(zip(ip_list, port_list))
for i in detail.items():
    result = ("{}:{}".format(i[0], i[1]))
    ip_port_list.append(result)

validips = []
for ip in ip_port_list:
    try:
        response = requests.get('https://api64.ipify.org?format=json',proxies = {'http': 'ip','https': 'ip'},timeout = 15)
        response.json()
        validips.append({'ip': ip})
        print(response.json())
    except:
        print('fail',ip)



