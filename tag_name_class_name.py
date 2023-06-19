from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class tag_class_name_demo():
    # def tag_name_demo(self):
    #     driver= webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #     driver.get("https://www.yatra.com/")
    #     driver.maximize_window()
    #     driver.find_element(By.TAG_NAME,"a").click()
    #     time.sleep(5)

    def class_name_demo(self):
        driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "list-dropdownNull").click()
        time.sleep(5)

a = tag_class_name_demo()
a.class_name_demo()