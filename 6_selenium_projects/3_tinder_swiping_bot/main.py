from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
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
print("no such element")
time.sleep(3)

# switch to FB window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(5)

# click on accept cookie
try:
    # fb_cookie = driver.find_element(By.CSS_SELECTOR, "button._42ft._4jy0._al65._4jy3._4jy1.selected._51sy")
    fb_cookie = driver.find_element(By.CSS_SELECTOR, 'button[data-cookiebanner="accept_button"]')
    fb_cookie.click()
except NoSuchElementException:
    print("no fb cookie element")

# login fb
fb_email = driver.find_element(By.ID, "email")
fb_password = driver.find_element(By.ID, "pass")
fb_email.send_keys("wentungwen@gmail.com")
fb_password.send_keys("password")
driver.find_element(By.CSS_SELECTOR, "#loginbutton input").click()
time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(6)

# close notification btn
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Allow"]').click()

# set the location and switch back to the main window
try:
    time.sleep(6)
    alert = driver.switch_to.alert
    alert.accept()
    driver.switch_to.default_content()
except NoAlertPresentException:
    print("no alert error")

# click on not interest button
noti = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Not interested"]')))
noti.click()
print("not interest btn clicked!")

# click on accept cookie button
try:
    cookie = driver.find_element(By.XPATH, '//*[@id="s-407411262"]/div/div[2]/div/div/div[1]/div[1]/button')
    cookie.click()
except Exception as e:
    print(f"the cookie error: {e}")

# click love
count = 0
while count < 20:
    # like the guy
    time.sleep(1)
    like_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.Bgi\(\$g-ds-background-like\)\:a")))
    like_btn.click()

    # if he also likes you, click likes-you-too-button and send him message.
    try:
        time.sleep(1)
        textbox = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Say something nice!"]')
        textbox.send_keys("Hi, how's going:) ")
        driver.find_element(By.CSS_SELECTOR, 'button.button.Lts\(\$ls-s\).C\(\$c-ui-button-blue\)').click()

    except Exception as e:
        print(f"He likes you too error ====>{e}")

    time.sleep(3)
    count += 1
