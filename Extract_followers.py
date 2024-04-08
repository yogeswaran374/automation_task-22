from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# initialize the driver and URL

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/guviofficial/")
time.sleep(5)

# find elements by inspect followers

followers=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button')
print(followers.text) #print the followers