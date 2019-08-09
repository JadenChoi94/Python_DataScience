### 커피빈 매장 크롤링하기

# 모듈 준비하기

import time
from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
import pandas as pd

chromedriver_dir = 'D:/workspace/Python_DataScience/Coffee_index/chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)

name = []
address = []
lat = []
log = []

for i in range(1, 14):

    driver.get('https://www.coffeebeankorea.com/store/store.asp')
    time.sleep(3)

    region_srh = driver.find_element_by_xpath('//*[@id="contents2"]/div[1]/div[2]/div[3]/h3[2]')
    region_srh.click()
    time.sleep(3)

    select_box = driver.find_element_by_xpath('//*[@id="contents2"]/div[1]/div[2]/div[3]/div[2]/div[1]')
    select_box.click()
    time.sleep(3)

    x1 = '//*[@id="storeLocal"]/li['
    x2 = str(i)
    x3 = ']'
    x1 + x2 + x3

    sido = driver.find_element_by_xpath(x1 + x2 + x3)
    sido.click()
    time.sleep(3)


    source = driver.page_source
    bs = bs4.BeautifulSoup(source,'html.parser')
    entire = bs.find('ul', id = 'storeListUL')
    li_list = entire.find_all('li')

    for info in li_list:

        tmp_name = info.select('span')[0].get_text()
        name.append(tmp_name)

        tmp_address = info.find_all('p')[2].get_text().split(',')[0]
        address.append(tmp_address)

        lat.append(info['data-lat'])

        log.append(info['data-lng'])

    print(i)


CoffeeBin = pd.DataFrame({'Name': name,
                          'Address': address,
                          'Lat': lat,
                          'Log': log})
len(CoffeeBin)
CoffeeBin.to_csv('CoffeeBin/Bean.csv')

data = pd.read_csv('CoffeeBin/Bean.csv')

