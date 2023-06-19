from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class is_enabled_demo():
    def demo_is_enabled(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        demo1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo1)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("username")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("password")
        demo2 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo2)
        
d = is_enabled_demo()
d.demo_is_enabled()