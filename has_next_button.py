from unicodedata import category
from weakref import WeakValueDictionary
from webbrowser import Chrome
from selenium import webdriver 
import json 



chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);  
driver.maximize_window(); 

source = ""
category = ""
driver.get(category)

while True:
    buttonNext = driver.find_element_by_class_name('pagination__next')
    if 'inactive' in buttonNext.get_attribute('class'):
        break;
    buttonNext.click()
    source1 = ""
    category1 = ""
    driver.get(category1)
    


