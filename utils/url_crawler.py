from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import random 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(chrome_options=options)


num=886
while(num<895):
    driver = webdriver.Chrome(chrome_options=options)
    print(num)
    url=f'https://kb.commonhealth.com.tw/library/{num}.html'
    driver.get(url)
    title = driver.find_element(By.XPATH,'//*[@id="all-content"]/article/div[1]/div/div/h1')
    # print(title.text)
    
    #寫url.json
    with open("categories/url.json",'r',encoding='utf-8') as file:
        json_data=json.load(file)
    json_data["url"].append({"name": title.text,"url":url})
    with open("categories/url.json",'w',encoding='utf-8') as file:
        json_data=json.dump(json_data,file,ensure_ascii=False,indent=4)
    
    driver.quit()
    time.sleep(random.randint(1,5))
    num+=1

# discription=driver.find_element(By.CLASS_NAME,'text-content')
# print(discription.find_element(By.TAG_NAME,'h2').text)

# ps=discription.find_elements(By.TAG_NAME,'p')

# for p in ps:
#     if p.text=="" or p.text=='&nbsp;': continue
#     print(p.text+"\n")

# img=discription.find_elements(By.TAG_NAME,'img')

# for i in img:
#     print(i.get_attribute('src')+"\n")

# pannels=driver.find_elements(By.CLASS_NAME,'panel-default')

# for pannel in pannels:
#     islist=False
#     print(pannel.find_element(By.CLASS_NAME,'panel-title').text)
#     tmp=pannel.find_element(By.CLASS_NAME,'panel-body')
#     ps=tmp.find_elements(By.TAG_NAME,'p')
#     for p in ps:
#         if p.text=="": continue
#         print(p.text+'\n')
#         if '：' in p.text and islist==False:
#             ol=tmp.find_elements(By.TAG_NAME,'ol')
#             for o in ol:
#                 c=1
#                 for li in o.find_elements(By.TAG_NAME,'li'):
#                     print(f'{c}. {li.text}')
#                     islist=True
#                     c+=1
#     if(islist==False):
#         li=tmp.find_elements(By.TAG_NAME,'li')
#         c=1
#         for l in li:
#             print(f'{c}. {l.text}')
#             c+=1

#     img=pannel.find_elements(By.TAG_NAME,'img')
#     for i in img:
#         print(i.get_attribute('src')+"\n")



driver.quit()