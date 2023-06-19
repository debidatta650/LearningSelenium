from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\browserDriver\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.facebook.com")
driver.maximize_window()
print(driver.title)
driver.close()