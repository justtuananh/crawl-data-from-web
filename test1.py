from selenium import webdriver
import json
# khoi tao trinh duyet
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
source='www.globaltimes.cn'
category="https://www.globaltimes.cn/world/index.html"
driver.get(category)
# xu ly cac doi tuong tren trinh duyet
elments=driver.find_elements_by_xpath("//*[@class='new_title_ms']")
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
    content=driver.find_element_by_xpath("//*[@class='article_right']")
    article={}
    article['source']=source
    article['url']=href
    article['category']=category
    article['content']=content.text
    articles.append(article)

# ghi du lieu ra file json
with open('tuananh'+'.json','w',encoding='utf-8') as output:
    json.dump(articles,output,ensure_ascii=False)