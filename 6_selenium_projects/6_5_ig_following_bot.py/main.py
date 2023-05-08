from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

IG_EMAIL = os.environ.get("IG_EMAIL")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get("https://www.instagram.com/")
time.sleep(7)
driver.find_element(By.CSS_SELECTOR, "button._a9_0").click()

time.sleep(9)

driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input').send_keys(IG_EMAIL)
driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Password"]').send_keys(IG_PASSWORD)
driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button").click()
time.sleep(15)

driver.find_element(By.CSS_SELECTOR, 'div[role="button"]').click()
time.sleep(15)
driver.find_element(By.CSS_SELECTOR, 'button._a9_1').click()
time.sleep(3)
driver.get("https://www.instagram.com/helpmaths/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "section > main > div > header > section > ul > li:nth-child(2) > a").click()
time.sleep(5)
followers = driver.find_elements(By.CSS_SELECTOR, 'div[role="dialog"] button._acan')
time.sleep(4)
print(followers)
for n in followers:
    time.sleep(4)
    n.click()
    print("-")


driver.quit()


