from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

def  web_driver():
    return webdriver.Chrome(executable_path='D:/chromedriver_96/chromedriver.exe')

def my_op():
    global driver
# Get Table Data and append in a list
    table = soup.find_all(
        'div',{'class':'cms_table'})[6::]
    site_uni =[]
    csv_uni =[]
    for t in table:
        tds = t.find_all('tr') 
        for t_data in tds:
            d = t_data.find_all(
                'td',{'class':'cms_table_grid_td'})[0]
            for td in d:
                site_uni.append((td.text).replace('\n',''))

# Read universities value from csv and loop through the valus
    df = pd.read_csv('unis.csv')
    str_obj = df['List'].values
    for i in str_obj:
        csv_uni.append(i)
    valid = []
    for j in csv_uni:
        if j in site_uni:
            val =j
            temp ={
                'University List':val
            }
            valid.append(temp)
            df = pd.DataFrame(valid)
            df.to_csv('University_Under_300_GRE.csv')
    print('Task Complete ..... ')
    driver.close()        

                       

if __name__ == '__main__':
    driver = web_driver()
    url= 'http://www.msinus.com/content/gre-universities-486/'
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,
        'af-form-close-button').click()
    soup = BeautifulSoup(driver.page_source,features='lxml')
    my_op()
  

    
