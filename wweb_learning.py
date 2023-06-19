import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class learning_demo():
    def learning(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        time.sleep(3)
        driver.fullscreen_window()
        time.sleep(3)
        # driver.refresh()
        # time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Yatra for Business").click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.minimize_window()
        time.sleep(4)

a= learning_demo()
a.learning()