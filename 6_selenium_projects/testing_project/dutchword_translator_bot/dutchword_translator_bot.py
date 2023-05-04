from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with open("original_words.txt") as f:
    word_input = f.readlines()
marked_words = [n+",\n" for n in word_input]

with open("output.txt", "w") as f:
    f.writelines(marked_words)

webdriver_path = "/Users/wentungwen/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get("https://translate.google.com/")
driver.find_element(By.CSS_SELECTOR, "button").click()
driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Source text"]').send_keys(marked_words)
wait = WebDriverWait(driver, 10)
read = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Listen to source text"]')))
read.click()
time.sleep(100)
