# import thu vien 
from selenium import webdriver 

# khoi tao web 
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.csis.org/analysis/"
driver.get(url)
# lay thong tin tung link 
elements = driver.find_elements_by_xpath("//*[@class")

# lay thong tin trong tung link 


# ghi vao file dang json 