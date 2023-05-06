from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("https://ic.nkust.edu.tw/p/412-1075-3220.php?Lang=zh-tw")

time.sleep(3)

# 取得網頁原始碼
page_source = driver.page_source

# 關閉 webdriver
driver.quit()

# 解析網頁
soup = BeautifulSoup(page_source, "html.parser")

name_th_tags = soup.find_all('th', text='姓名')
name_list=[]

for name_th in name_th_tags:
    next_th = name_th.find_next_sibling('th')
    if next_th is not None:
        name = next_th.text.strip()
        mail_td = name_th.find_next('td', text='電郵')
        if mail_td is not None:
            mail = mail_td.find_next_sibling('td').text.strip()
        else:
            mail = ""
        name_list.append((name, mail))
print(name_list)


        


