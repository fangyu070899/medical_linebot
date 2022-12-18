import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from linebot.models import TextSendMessage,ImageSendMessage,QuickReplyButton,MessageAction


option = webdriver.ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-logging'])
# option.add_argument('--ignore-certificate-errors')
# option.add_argument('--ignore-ssl-errors')

#for heroku
option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
option.add_argument("--headless") #無頭模式
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--no-sandbox")

# 爬所有文章網址對應的標題 寫在url.json

# num=886
# while(num<895):
#     driver = webdriver.Chrome(chrome_options=options)
#     print(num)
#     url=f'https://kb.commonhealth.com.tw/library/{num}.html'
#     driver.get(url)
#     title = driver.find_element(By.XPATH,'//*[@id="all-content"]/article/div[1]/div/div/h1')
#     # print(title.text)
    
#     #寫url.json
#     with open("categories/url.json",'r',encoding='utf-8') as file:
#         json_data=json.load(file)
#     json_data["url"].append({"name": title.text,"url":url})
#     with open("categories/url.json",'w',encoding='utf-8') as file:
#         json_data=json.dump(json_data,file,ensure_ascii=False,indent=4)
    
#     driver.quit()
#     time.sleep(random.randint(1,5))
#     num+=1


def search_discription(title,url):
    message=[]
    num=0
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=option)
    driver.get(url)
    discription=driver.find_element(By.CLASS_NAME,'text-content')
    d=discription.find_element(By.TAG_NAME,'h2').text
    print(d)
    if(num<4 and len(d)>0 and d!=' '):
        message.append(TextSendMessage(text=d))
        num+=1

    islist=False
    ol_num=0
    ul_num=0
    ps=discription.find_elements(By.TAG_NAME,'p')
    for p in ps:
        if p.text=="" or p.text=='&nbsp;': continue
        print(p.text+"\n")
        tmp_num=num
        if '：' in p.text:
            ol_tmp_num=0
            ol=discription.find_elements(By.TAG_NAME,'ol')
            for o in ol:
                if(ol_tmp_num==ol_num):
                    c=1
                    list=p.text+'\n\n'
                    for li in o.find_elements(By.TAG_NAME,'li'):
                        is_p=False
                        for test_p in li.find_elements(By.TAG_NAME,'p'):
                            is_p=True
                        if(is_p==False):
                            print(f'{c}. {li.text}')
                            list+=f'{c}. {li.text}\n'
                            islist=True
                            c+=1
                    if(num<4 and len(list)>0 and list!='\n\n') :
                        message.append(TextSendMessage(text=list))
                        num+=1
                    ol_num+=1
                    break
                ol_tmp_num+=1

            ul_tmp_num=0
            ul=discription.find_elements(By.TAG_NAME,'ul')
            for u in ul:
                if(ul_tmp_num==ul_num):
                    c=1
                    list=p.text+'\n\n'
                    for li in u.find_elements(By.TAG_NAME,'li'):
                        is_p=False
                        for test_p in li.find_elements(By.TAG_NAME,'p'):
                            is_p=True
                        if(is_p==False):
                            print(f'• {li.text}')
                            list+=f'• {li.text}\n'
                            islist=True
                            c+=1
                    if(num<4 and len(list)>0 and list!='\n\n') :
                        message.append(TextSendMessage(text=list))
                        num+=1
                    ul_num+=1
                    break
                ul_tmp_num+=1

        if(num==tmp_num and num<4 and len(p.text)>0 and p.text!=' '):
            message.append(TextSendMessage(text=p.text))
            num+=1

    if(islist==False):
        li=discription.find_elements(By.TAG_NAME,'li')
        c=1
        list=''
        for l in li:
            is_p=False
            for test_p in l.find_elements(By.TAG_NAME,'p'):
                is_p=True
            if(is_p==False):
                print(f'{c}. {l.text}')
                list+=f'{c}. {l.text}\n'
                c+=1
        if(num<4 and len(list)>0):
            message.append(TextSendMessage(text=list))
            num+=1

    img=discription.find_elements(By.TAG_NAME,'img')

    for i in img:
        src=i.get_attribute('src')
        print(src+"\n")
        if(num<4):
            message.append(ImageSendMessage(src,src))
            num+=1
    item=[]
    count=0        
    category = driver.find_element(By.ID,'article-nav-pills')
    for c in category.find_elements(By.TAG_NAME,'li'):
        print(c.text)
        if(count<13):
            item.append(
                QuickReplyButton(
                    action=MessageAction(label=f"{c.text}", text=f"{title}->{c.text}")
            ))
            count+=1

    driver.quit()
    return [message,item]


def search_paper(title,select_category,url):
    num=0
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=option)
    driver.get(url)
 
    item=[]
    count=0   
    i=0     
    index=0
    category = driver.find_element(By.ID,'article-nav-pills')
    for c in category.find_elements(By.TAG_NAME,'li'):
        i+=1
        print(c.text)
        if(select_category in c.text):
            print(c.text)
            index=i
        if(count<13):
            item.append(
                QuickReplyButton(
                    action=MessageAction(label=f"{c.text}", text=f"{title}->{c.text}")
            ))
            count+=1
    message=[]
    tmp_index=0
    pannels=driver.find_elements(By.CLASS_NAME,'panel-default')

    for pannel in pannels:
        ol_num=0
        ul_num=0
        tmp_index+=1
        islist=False
        # print(f"{tmp_index}/{index}")
        if(tmp_index==index):
            t=pannel.find_element(By.CLASS_NAME,'panel-title').text
            print(t)
            if(num<4 and len(t)>0  and t!='\n' and t!=' '):
                message.append(TextSendMessage(text=t))
                num+=1

            tmp=pannel.find_element(By.CLASS_NAME,'panel-body')
            ps=tmp.find_elements(By.TAG_NAME,'p')
            for p in ps:
                if p.text=="": continue
                print(p.text+'\n')
                tmp_num=num
                if '：' in p.text:
                    ol_tmp_num=0
                    ol=tmp.find_elements(By.TAG_NAME,'ol')
                    for o in ol:
                        if(ol_tmp_num==ol_num):
                            c=1
                            list=p.text+'\n\n'
                            for li in o.find_elements(By.TAG_NAME,'li'):
                                is_p=False
                                for test_p in li.find_elements(By.TAG_NAME,'p'):
                                    is_p=True
                                if(is_p==False):
                                    print(f'{c}. {li.text}')
                                    list+=f'{c}. {li.text}\n'
                                    islist=True
                                    c+=1
                            if(num<4 and len(list)>0 and list!='\n\n') :
                                message.append(TextSendMessage(text=list))
                                num+=1
                            ol_num+=1
                            break
                        ol_tmp_num+=1

                    ul_tmp_num=0
                    ul=tmp.find_elements(By.TAG_NAME,'ul')
                    for u in ul:
                        if(ul_tmp_num==ul_num):
                            c=1
                            list=p.text+'\n\n'
                            for li in u.find_elements(By.TAG_NAME,'li'):
                                is_p=False
                                for test_p in li.find_elements(By.TAG_NAME,'p'):
                                    is_p=True
                                if(is_p==False):
                                    print(f'• {li.text}')
                                    list+=f'• {li.text}\n'
                                    islist=True
                                    c+=1
                            if(num<4 and len(list)>0 and list!='\n\n') :
                                message.append(TextSendMessage(text=list))
                                num+=1
                            ul_num+=1
                            break
                        ul_tmp_num+=1

                if(num==tmp_num and num<4 and len(p.text)>0 and p.text!=' '):
                    message.append(TextSendMessage(text=p.text))
                    num+=1
            if(islist==False):
                li=tmp.find_elements(By.TAG_NAME,'li')
                c=1
                list=''
                for l in li:
                    is_p=False
                    for test_p in l.find_elements(By.TAG_NAME,'p'):
                        is_p=True
                    if(is_p==False):
                        print(f'{c}. {l.text}')
                        list+=f'{c}. {l.text}\n'
                        c+=1
                if(num<4 and len(list)>0):
                    message.append(TextSendMessage(text=list))
                    num+=1

            img=pannel.find_elements(By.TAG_NAME,'img')
            for i in img:
                src=i.get_attribute('src')
                print(src+"\n")
                if(num<4):
                    message.append(ImageSendMessage(src,src))
                    num+=1
    
    driver.quit()
    print(num)
    if(message==[]):
        message.append(TextSendMessage(text="很抱歉，這方面我不太清楚"))
    return [message,item]


if __name__ == "__main__":
    # i=search_discription("B型肝炎","https://kb.commonhealth.com.tw/library/1.html")
    i=search_paper("B型肝炎","就醫準備","https://kb.commonhealth.com.tw/library/1.html")
    # print(i[0])
    # print(i[1])