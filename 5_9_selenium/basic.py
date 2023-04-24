from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

### Basic practices
webdriver_path = "/Users/wentungwen/Documents/chromedriver"
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# Practice 3: scratch and click wiki main page articles' numbers
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
article_count.click()

login = driver.find_element(By.LINK_TEXT, "Log in")
login.click()

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Taiwan")
search_box.send_keys(Keys.RETURN)



# Practice 2: python.org upcoming-event
driver.get("https://www.python.org/")
content = driver.find_elements(By.CSS_SELECTOR, "#content .medium-widget.event-widget.last .menu li")
content_texts = [data.text.split("\n") for data in content]

obj = {}
for idx, data in enumerate(content_texts):
    obj[idx] = {"time": data[0], "event": data[1]}
print(obj)


# Practice 1: Scratching the Amazon product title
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
price = driver.find_element(By.XPATH, '//*[@id="productTitle"]')
print(price.text)

