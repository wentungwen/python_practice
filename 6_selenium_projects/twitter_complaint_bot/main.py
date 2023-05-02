import twitterbot
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bot = twitterbot.InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()





