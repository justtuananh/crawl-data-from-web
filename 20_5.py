from ast import expr_context
from logging import exception
from selenium import webdriver
import json
# khoi tao trinh duyet
#driver = webdriver.Firefox()
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);  
driver.maximize_window()
source='https://tass.com/politics'
category="https://tass.com/politics"
driver.get(category)
# xu ly cac doi tuong tren trinh duyet
elments=driver.find_elements_by_xpath("//*[@class='featured__title']")
articles=[]
url=[]
# lay danh sach cac link new
for elm in elments:
    href=elm.get_attribute('href')
    url.append(href)

# duyet tung link trong url,
# truy cap vao tung new de lay noi dung cua article
for href in url:
    driver.get(href)
    try: 
        content=driver.find_element_by_xpath("//*[@class='text-block']")
        article={}
        article['source']=source
        article['url']=href
        article['category']=category
        article['content']=content.text
        articles.append(article)
    except: 
        print(href)

# ghi du lieu ra file json
with open('politics_tass'+'.json','w',encoding='utf-8') as output:
    json.dump(articles,output,ensure_ascii=False)