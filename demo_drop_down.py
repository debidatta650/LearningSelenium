from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

class drop_down_demo():
    def demo_drop_down(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.maximize_window()
        driver.find_element(By.NAME, "UserFirstName").send_keys("Debidatta")
        time.sleep(2)
        driver.find_element(By.NAME, "UserLastName").send_keys("Das")
        time.sleep(2)
        driver.find_element(By.NAME, "UserEmail").send_keys("debidatta.das@reverieinc.com")
        time.sleep(2)
        drop = driver.find_element(By.NAME, "UserTitle")
        d = Select(drop)
        d.select_by_index(5)
        time.sleep(2)
        driver.find_element(By.NAME, "CompanyName").send_keys("Reverie Language Technology")
        time.sleep(2)
        drop1 = driver.find_element(By.NAME, "CompanyEmployees")
        d1 = Select(drop1)
        d1.select_by_index(3)
        time.sleep(2)
        driver.find_element(By.NAME, "UserPhone").send_keys("7008545252")
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='msaCheckbox checkboxInput section']//div//div[@class='checkbox-ui']").click()
        time.sleep(2)

        driver.close()

a = drop_down_demo()
a.demo_drop_down()