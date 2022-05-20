from selenium import webdriver 


chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);  
driver.maximize_window()
source='https://nationalinterest.org/topic/security'
category='https://nationalinterest.org/topic/security'
driver.get(category)

elements=driver.find_elements_by_xpath("//*[@class='article__title']")
