from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class get_text_demo():
    def demo_get_text(self):
        driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        test = driver.find_element(By.XPATH, "//div[@class='yt-book why_bookyatra moduleArea']").text
        print(test)
        time.sleep(4)

d = get_text_demo()
d.demo_get_text()
