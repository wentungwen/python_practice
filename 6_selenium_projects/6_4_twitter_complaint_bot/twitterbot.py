from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

PROMISED_DOWN = os.environ.get("PROMISED_DOWN")
PROMISED_UP = os.environ.get("PROMISED_UP")
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = CHROME_DRIVER_PATH
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.twitter_email = TWITTER_EMAIL
        self.twitter_password = TWITTER_PASSWORD

    def get_internet_speed(self):
        driver = webdriver.Chrome()
        driver.get("https://www.speedtest.net/")
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        driver.find_element(By.CSS_SELECTOR, "a.js-start-test.test-mode-multi").click()

        time.sleep(60)
        driver.find_element(By.CSS_SELECTOR, "a.notification-dismiss.close-btn").click()
        download_speed = driver.find_element(By.CSS_SELECTOR,
                                             ".result-data-large.number.result-data-value.download-speed").text
        upload_speed = driver.find_element(By.CSS_SELECTOR,
                                           ".result-data-large.number.result-data-value.upload-speed").text
        print(download_speed, upload_speed)

    def tweet_at_provider(self):
        driver = webdriver.Chrome()
        driver.get("https://twitter.com/")
        time.sleep(12)

        # switch to twitter's iframe
        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".S9gUrf-YoZ4jf iframe"))
        driver.find_element(By.XPATH, '//*[@id="container"]/div').click()

        # switch google windows
        time.sleep(2)
        if len(driver.window_handles) > 1:
            base_window = driver.window_handles[0]
            tw_login_window = driver.window_handles[1]
            driver.switch_to.window(tw_login_window)
            # login with google window
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "input#identifierId").send_keys(self.twitter_email)
            driver.find_element(By.CSS_SELECTOR, "button").click()
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR, 'input').send_keys(self.twitter_password)
            driver.find_elements(By.CSS_SELECTOR, "button")[1].click()
            # switch back twitter windows
            time.sleep(5)
            driver.switch_to.window(base_window)
        else:
            print("No login window found.")










