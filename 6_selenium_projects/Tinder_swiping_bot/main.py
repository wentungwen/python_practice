from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

webdriver_path = "/Users/wentungwen/Documents/chromedriver"
driver = webdriver.Chrome()

driver.get("https://tinder.com/")
wait = WebDriverWait(driver, 10)
show_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.c1p6lbu0")))

login_button = driver.find_element(By.CSS_SELECTOR, "a.c1p6lbu0")
login_button.click()
time.sleep(5)

# click on FB-login button
login_fb_btn = driver.find_element(By.CSS_SELECTOR, "button.c1p6lbu0.W\(100\%\).Maw\(315px\)--s")
login_fb_btn.click()
time.sleep(3)

# switch to FB window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


# login and enter
driver.find_element(By.CSS_SELECTOR, "button._42ft._4jy0._9xo7.selected._51sy").click()
fb_email = driver.find_element(By.ID, "email")
fb_password = driver.find_element(By.ID, "pass")
fb_email.send_keys("wentungwen@gmail.com")
fb_password.send_keys("Bbc1121\\")
driver.find_element(By.CSS_SELECTOR, "#loginbutton input").click()
time.sleep(10)

driver.switch_to.window(base_window)
print(driver.title)
