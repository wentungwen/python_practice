from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time

webdriver_path = "/Users/wentungwen/Documents/chromedriver"
driver = webdriver.Chrome()

# cookie clicker project
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 10

while True:
    cookie.click()
    if time.time() >= timeout:
        # get current upgrades and make a dict {"grandma": 133, ...}
        try:
            upgrades = driver.find_elements(By.CSS_SELECTOR, "#store > div b")
            upgrade_elements = {}
            for upgrade in upgrades:
                element_text = upgrade.text
                if element_text != "":
                    cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    element_name = element_text.split("-")[0].strip()
                    upgrade_elements[element_name] = cost
            # check current money
            money = int(driver.find_element(By.ID, "money").text)

            # check the upgrade element and buy the most expensive one
            highest_upgrade_price = 0
            highest_upgrade_name = ""
            for n in upgrade_elements:
                upgrade_price = upgrade_elements[n]
                if money > upgrade_price > highest_upgrade_price:
                    highest_upgrade_price = upgrade_price
                    highest_upgrade_name = n
            upgrade_element = driver.find_element(By.ID, f"buy{highest_upgrade_name}")
            upgrade_element.click()

        except StaleElementReferenceException:
            continue
        except NoSuchElementException:
            continue

