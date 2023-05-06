# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:18:41 2023

@author: user
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager    #自動下載driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import bs4, time
import pandas as pd 


page = int(input("請輸入頁面向下捲動次數:"))
browser = webdriver.Chrome() 
url = 'https://www.dcard.tw/f/mood'
browser.get(url)

number = 0
counter = 0
post_title = []
post_df = pd.DataFrame(columns=(['文章編號','文章標題','心情數量','留言數量']))

while page > counter:
    move = browser.find_element(By.TAG_NAME, 'body')
    time.sleep(1)
    move.send_keys(Keys.PAGE_DOWN) 
    time.sleep(1)

    objsoup = bs4.BeautifulSoup(browser.page_source, 'lxml')
    articles = objsoup.find_all('article', class_ = 'atm_40_ncl75p atm_gi_1d1uzc4 atm_mk_h2mmj6 atm_lo_1lq3voq atm_le_1lq3voq atm_lk_18fnu1o atm_ll_18fnu1o atm_9s_11p5wf0 atm_dy_m63k86 atm_dz_1ghlemp atm_9j_tlke0l atm_r2_1j28jx2 atm_e0_jok701 c122gkvw')

    for article in articles:
        title = article.find('a')
        emotion = article.find('div', class_ = 'atm_lk_i2wt44 c1jkhqx5')
        comment = article.find_all('div', class_ = 'atm_9s_1txwivl atm_h_1h6ojuz atm_ll_exct8b atm_dz43bx_idpfg4 atm_1pqnrs9_gktfv atm_1dlbvfv_gktfv atm_1in2ljq_i2wt44 atm_leio7s_nmbu2e fnja3xi')
        second_class = comment[1]
        if title.text not in post_title:
            number += 1
            post_title.append(title.text)
            print("文章編號:", number)
            print("文章標題:", title.text)
            print("心情數量:", emotion.text)
            print("留言數量:", second_class.text)
            print("="*100)
            post_df = post_df.append({'文章編號':number,'文章標題':title.text,'心情數量':emotion.text,'留言數量':second_class.text},ignore_index=True)
    counter += 1
# post_df.to_csv('dcard_clear.csv')

