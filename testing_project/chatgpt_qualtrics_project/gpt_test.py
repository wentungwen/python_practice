import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import os


# Set up the chatgpt API endpoint URL and API key
api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.environ.get("GPT_APIKEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
with open("prompt.txt") as file:
    prompt = file.read()

request_data = {
    "model": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 1000,
    "temperature": 0.8
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open("./text.txt", "w") as f:
        f.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code), response.text}")

# separate the persona and import into list [pr1, pr2...]



"""
# read and questions from Qualtrics and generate the answer_list
webdriver_path = "/Users/wentungwen/Documents/chromedriver"
driver = webdriver.Chrome()
driver.get("https://tilburghumanities.eu.qualtrics.com/jfe/form/SV_6tXugLKNxmTdwQm")

try:
    driver.find_element(By.ID, "QR~QID19~1").is_selected()
except NoSuchElementException as e:
    print(e.msg)
"""


# post personas into chatGPT with each question



