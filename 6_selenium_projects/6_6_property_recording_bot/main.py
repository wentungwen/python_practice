from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

GOOGLE_FORM_URL = os.environ.get("GOOGLE_FORM_URL")
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
ZILLOW_URL = os.environ.get("ZILLOW_URL")

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(ZILLOW_URL)
time.sleep(9)

# sub_pages = [n.get_attribute("href") for n in driver.find_elements(
#     By.CSS_SELECTOR, "ul li.PaginationNumberItem-c11n-8-85-1__sc-bnmlxt-0.eKbbwc a")]
# print(sub_pages)

prices = [price.text.strip("$") for price in driver.find_elements(
    By.CSS_SELECTOR, '#grid-search-results ul li span[data-test="property-card-price"]')]
links = [link.get_attribute("href") for link in driver.find_elements(
    By.CSS_SELECTOR, '#grid-search-results ul li a.property-card-link')]
addresses = [addr.text for addr in driver.find_elements(
    By.CSS_SELECTOR, '#grid-search-results ul li address')]
print(len(prices), len(links), len(addresses))

time.sleep(2)

for idx, n in enumerate(range(0, len(prices))):
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get(GOOGLE_FORM_URL)
    time.sleep(3)
    input_box = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    input_box[0].send_keys(addresses[idx])
    input_box[1].send_keys(prices[idx])
    input_box[2].send_keys(links[idx])
    driver.find_element(By.CSS_SELECTOR, ".uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd").click()
    driver.close()



