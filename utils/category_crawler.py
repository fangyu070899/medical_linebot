from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
url='https://kb.commonhealth.com.tw/library/category/1'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get(url)
driver.maximize_window()

cookie_btn= driver.find_element(By.CLASS_NAME,'btn')
cookie_btn.click()

elements= driver.find_elements(By.CLASS_NAME,'result-item')

for e in elements:
    href=e.find_element(By.TAG_NAME,'a')
    print(href.get_attribute('href'))
    title=href.find_element(By.TAG_NAME,'h3')
    print(title.text)

count=0
while(True):
    button = driver.find_element(By.XPATH,'box-btn').find_element(By.CLASS_NAME,'btn')
    driver.execute_script("arguments[0].scrollIntoView();", button)
    if(button.is_displayed()==False):
        print("done")
        break
    else :
        driver.execute_script("arguments[0].click();", button)
        print(button.text)
        # button.click()
        time.sleep(1)
        count+=1
    if count>1:
        print("done")
        break

elements= driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div/div[1]/div[13]').find_elements(By.CLASS_NAME,'result-item')
for e in elements:
    href=e.find_element(By.TAG_NAME,'a')
    print(href.get_attribute('href'))
    title=href.find_element(By.TAG_NAME,'h3')
    print(title.text)

driver.close()
driver.quit()