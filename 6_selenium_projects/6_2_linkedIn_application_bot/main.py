from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

webdriver_path = "/Users/wentungwen/Documents/chromedriver"
driver = webdriver.Chrome()

# get the job page
driver.get("https://www.linkedin.com/jobs/search")

# click the login button and login
login_btn = driver.find_element(By.LINK_TEXT, "Sign in")
login_btn.click()
user_name = driver.find_element(By.ID, "username")
user_password = driver.find_element(By.ID, "password")
user_name.send_keys("wentungwen@gmail.com")
user_password.send_keys()
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Sign in"]').click()


# set the keywords for titles and location
search_box = driver.find_element(By.CSS_SELECTOR, "input.jobs-search-box__keyboard-text-input")
search_box.send_keys("python developer")
search_location = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__input.jobs-search-box__input--location input")
search_location.clear()
search_location.send_keys("Taiwan")

# set remote job type
driver.find_element(By.CSS_SELECTOR, ".search-reusables__all-filters-pill-button").click()
time.sleep(3)

# easy apply
toggle = driver.find_element(By.CSS_SELECTOR, "input[data-artdeco-toggle-button='true']")
if toggle.get_attribute("aria-checked") == "false":
    driver.execute_script("arguments[0].scrollIntoView();", toggle)
    driver.execute_script("window.scrollBy(0, -100);")
    action = ActionChains(driver)
    action.move_to_element(toggle).click().perform()

time.sleep(3)
show_btn = driver.find_element(By.CSS_SELECTOR, "button.search-reusables__secondary-filters-show-results-button"
                                                ".artdeco-button")

show_btn.click()

time.sleep(3)


# job list
result_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

for item in result_list:
    time.sleep(3)
    item.click()
    try:
        # easy apply button
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button.jobs-apply-button").click()
        time.sleep(3)
        # submit/next button
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
        if submit_button:
            print("submit btn available")
            try:
                # select country code
                code_ele = driver.find_element(By.CSS_SELECTOR, 'select[data-test-text-entity-list-form-select]')
                select = Select(code_ele).select_by_value("Netherlands (+31)")
                # type in phone number
                driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--container input").send_keys("0123456789")
            except NoSuchElementException:
                print("country code/phone error")
                continue
            # click submit button
            submit_button.click()
        else:
            print("no submit btn")

    except NoSuchElementException:
        print("No application button, skipped.")
        driver.find_element(By.CSS_SELECTOR, "button.artdeco-modal__dismiss").click()
        driver.find_element(By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]').click()
        continue







