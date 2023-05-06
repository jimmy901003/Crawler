# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:54:52 2023

@author: user
"""
# Request URL: https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20230319&stockNo=2330&response=json&_=1679208780934

import requests as r
import json 
import pandas as pd
from datetime import datetime,date
import matplotlib.pyplot as plt
import time
import random



month_list = pd.date_range(start='2022-01-01',end='2023-01-01', freq='m').strftime('%Y%m%d').tolist()
stock_code = str(input('輸入股票代碼 : '))


headers = {'User-Agent':'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20230319&stockNo=2330&response=json&_=1679208780934'}
stock_overview = []
for month in month_list :
    url = 'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date='+ month +'&stockNo='+stock_code+'&response=json&_=1679208780934'
    res = r.get(url,headers=headers)
    stock_json = pd.DataFrame(res.json()['data'])    
    stock_json.columns =  ['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
    stock_overview.append(stock_json)
    delay_times = [12, 10, 16, 20, 14, 13, 18, 13]  # 延遲的秒數
    time.sleep(random.choice(delay_times))
stock_overview = pd.concat(stock_overview)

# 轉換日期格式 
stock_overview['日期'] = stock_overview['日期'].apply(lambda x: [i.replace('/', '') for i in x.split('/')])
stock_overview['日期'] = stock_overview['日期'].apply(lambda x: ''.join(x))
stock_overview['日期'] = stock_overview['日期'].astype(int)
stock_overview['日期'] = (stock_overview['日期']+19110000).astype(str)
stock_overview['日期'] = pd.to_datetime(stock_overview['日期'],format='%Y%m%d').dt.date

# 輸出成csv
stock_overview.to_excel('stock.xlsx',encoding='utf-8-sig')
 



