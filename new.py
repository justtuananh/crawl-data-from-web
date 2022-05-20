from selenium import webdriver 
import json


# driver = webdriver.Chrome()


chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);  
driver.maximize_window()

source = "https://breakingdefense.com/"
category  = "https://breakingdefense.com/"
driver.get(category)

# xu li cac doi tuong tren trinh duyet 
elements=driver.find_elements_by_xpath("//*[@class='postTitle']")
articles =[]
url = [] # kieu du lieu list 
# lay danh sach cac link new 
for elm in elements: 
    href = elm.get_attribute('href')
    url.append(href)

# duyet tung link trong url 
# truy cap vao tung link de lay thong tin 

for href in url:
    
    driver.get(href)
    content=driver.find_element_by_xpath("//*[@class='entry']")
    article={}
    article['source']=source
    article['url']=href
    article['category']=category
    article['content']=content.text
    articles.append(article)


# ghi vao file 
with open(source+".json", 'w', encoding = 'utf-8') as output: 
    json.dump(articles, output, ensure_ascii = False)
