from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class demo_partial_text():
    # def link_text_demo(self):
    #     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #     driver.get("https://www.yatra.com/")
    #     driver.maximize_window()
    #     driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
    #     time.sleep(5)

    def partial_link_text_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Yatra for").click()
        time.sleep(5)

a = demo_partial_text()
a.partial_link_text_demo()