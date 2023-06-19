import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class find_elements_demo():
    def find_tag_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        list1 = driver.find_elements(By.TAG_NAME, "a")
        print(len(list1))
        for i in list1:
            print(i.text)
        time.sleep(4)

a= find_elements_demo()
a.find_tag_demo()