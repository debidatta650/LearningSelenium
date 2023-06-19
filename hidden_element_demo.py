import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class hidden_demo():
    # def hidden_element_demo(self):
    #     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #     driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
    #     dis1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
    #     print(dis1)
    #     driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
    #     dis2 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
    #     print(dis2)

    def hidden_element_demo_yatra(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element(By.XPATH, "//span[normalize-space()='Hotels']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//i[@class='icon icon-angle-right arrowpassengerBox']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="BE_Hotel_pax_box"]/div[1]/div[2]/div[3]/div/div/span[2]').click()
        time.sleep(4)
        ele = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(ele)

d = hidden_demo()
# d.hidden_element_demo()
d.hidden_element_demo_yatra()