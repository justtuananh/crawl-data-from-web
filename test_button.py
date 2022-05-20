from ast import expr_context
from logging import exception
from selenium import webdriver
import json


chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);  
driver.maximize_window()

source='https://nationalinterest.org/topic/security'
category="https://nationalinterest.org/topic/security"
driver.get(category)
while True:
    buttonNext = driver.find_element_by_class_name('pagination__next')

    linkPages=driver.find_element_by_xpath("//*[@class='pagination__next']")
    source1=linkPages.get_attribute('href')

    articles=[]
    url=[]
    driver.get(source1)
    elements=driver.find_elements_by_xpath("//*[@class='article__title']")
    for elm in elements: 
        link= elm.get_attribute('href')
        url.append(link)

    for lik in url: 
        driver.get(lik)
        try: 
            content=driver.find_element_by_xpath("//*[@class='detail__content']")
            article={}
            article["source"]= source 
            article["url"] = lik 
            article['category'] = category 
            article['content']= content.text
        except: 
            print(lik)

    with open("security_nationalinterest"+".json",'a', encoding='utf-8' )as output:
        json.dump(articles, output, ensure_ascii=False)
    
    if 'inactive' in buttonNext.get_attribute('class'):
        break;
    buttonNext.click()