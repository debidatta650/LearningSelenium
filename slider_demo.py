from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class sliderdemo():
    def demo_slider(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.snapdeal.com/products/electronics-home-audio-systems?sort=plrty")
        driver.maximize_window()
        ele1 = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        ele2 = driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
        achain = ActionChains(driver)
        # achain.drag_and_drop_by_offset(ele1, 30, 0).perform()
        achain.click_and_hold(ele1).pause(1).move_by_offset(40,0).release().perform()
        time.sleep(5)
        achain.drag_and_drop_by_offset(ele2,-20,0).perform()
        time.sleep(3)
        driver.close()

sd = sliderdemo()
sd.demo_slider()