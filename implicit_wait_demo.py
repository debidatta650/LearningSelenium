from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

class demo_implicit():
    def demo_imp_wait(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(6)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID, "usersdname").send_keys("debidatta@dell.com")

d = demo_implicit()
d.demo_imp_wait()