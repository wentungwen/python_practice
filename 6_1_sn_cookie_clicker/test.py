from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# webdriver_path = "/Users/wentungwen/Documents/chromedriver"
# driver = webdriver.Chrome()
#
# driver.get("http://orteil.dashnet.org/experiments/cookie/")

upgrade_elements = {'Cursor ': 15, 'Grandma ': 100, 'Factory ': 500, 'Mine ': 2000, 'Shipment ': 7000, 'Alchemy lab ': 50000, 'Portal ': 1000000, 'Time machine ': 123456789}
money = 102


highest_upgrade_price = 0
highest_upgrade_name = ""
for n in upgrade_elements:
    upgrade_price = upgrade_elements[n]
    if money > upgrade_price > highest_upgrade_price:
        highest_upgrade_price = upgrade_price
        highest_upgrade_name = n

print(highest_upgrade_price, highest_upgrade_name)



