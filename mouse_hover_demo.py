from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
class mouse_over_demo():
    def demo_mouse(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # mousemov = driver.find_element(By.CLASS_NAME, "more-arr")
        # achain = ActionChains(driver)
        # achain.move_to_element(mousemov).perform()
        # time.sleep(2)
        # driver.find_element(By.XPATH, "//span[normalize-space()='Freight']").click()
        # time.sleep(2)
        mousemov = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        achain = ActionChains(driver)
        achain.move_to_element(mousemov).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='signInBtn']").click()
        time.sleep(3)

mdemo = mouse_over_demo()
mdemo.demo_mouse()