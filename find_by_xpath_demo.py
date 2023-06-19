from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class demo_xpath():
    def xpath_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(6)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("chaleili")
        driver.close()

d = demo_xpath()
d.xpath_demo()