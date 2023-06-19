import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class demo_find_element():
    # def locate_by_id(self):
    #     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #     driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
    #     driver.find_element(By.ID,value="login-input").send_keys("test@test.com")
    #     time.sleep(5)

    # def locate_by_name(self):
    #     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #     driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
    #     driver.maximize_window()
    #     # driver.name.css:"#login-input".send_keys("debidatta@debidatta.com")
    #     driver.find_element(By.NAME, value="login-input").send_keys("test@test.com")
    #     time.sleep(6)

    # def locate_by_xpath(self):
    #     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #     driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
    #     driver.maximize_window()
    #     driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("debidatta@debidatta.com")
    #     time.sleep(5)
    def locate_by_scc_selector(self):
        driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys("sharvi@sharvi.com")
        time.sleep(5)

find_by_id = demo_find_element()
find_by_id.locate_by_scc_selector()

# browser = webdriver.Chrome(executable_path="D:\\browserDriver\\chromedriver_win32\\chromedriver.exe")