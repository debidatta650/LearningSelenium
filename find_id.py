import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class demoid:
    def demoid1(self):
        dr = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        dr.get("https://login.salesforce.com/?locale=in")
        dr.find_element(By.ID,value="username").send_keys("achive@achive.com")
        time.sleep(4)

d = demoid()
d.demoid1()