import os
import requests
from bs4 import BeautifulSoup
import smtplib

TARGET_PRICE = 100

header = {
    "Accept_Language": "en-NL,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,en-US;q=0.6,nl;q=0.5",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36"
}


def get_amazon_price():
    res = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                       headers=header)
    content = res.text
    soup = BeautifulSoup(content, "lxml")
    price_list = soup.select(
        selector="#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > "
                 "span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > "
                 "span:nth-child(2)")

    price_txt = [price.get_text() for price in price_list][0]
    price = float(price_txt.strip("$"))

    return price


def email_message(user, password):
    msg = f"Subject: Big discount!! \nThe price right now is {current_price}, which is lower than {TARGET_PRICE}!"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(
            from_addr=user,
            to_addrs="wentungwen@gmail.com",
            msg=msg,
        )


current_price = get_amazon_price()
my_email = "wen.for.programming@gmail.com"
my_password = os.environ.get("EMAIL_PASSWORD")

if current_price < TARGET_PRICE:
    email_message(my_email, my_password)
