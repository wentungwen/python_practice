import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import os


# Set up the chatgpt API endpoint URL and API key
api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
prompt="give me some inspiration about Opinion/provocation part of our assignment:" \
       "How to design a cooking workshop for local restaurants and producers to promote and thus increase the acceptance of protein substitutes (eg, insect, whole vegetable protein) to the general public?" \
       "Opinion/provocation: Second part of the paper mainly focuses on students’ personal commentary on the topic. This is where you are expected to come up with nascent ideas, spark debate, challenge conventions or even come up with controversial perspectives around the subtheme. "

request_data = {
    "model": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 500,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open("./text.txt", "a") as f:
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



