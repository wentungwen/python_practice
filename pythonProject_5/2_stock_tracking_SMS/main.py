import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
THRESHOLD = 0.05

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_APIKEY = "YOO4P8FZ515HX24L"
NEWS_APIKEY = "982b0d37196649079b8ec4a3005eb13f"

account_sid = "ACe6490eed28972d424c82ed31132d1755"
auth_token = "211a2952d250edcb9e832cd8b09d2884"

# # STEP 1: Use https://newsapi.org/docs/endpoints/everything When STOCK price increase/decreases by 5% between
# yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": STOCK_APIKEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_data = stock_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

delta = yesterday_closing_price - day_before_yesterday_closing_price
delta_per = (delta / yesterday_closing_price) * 100

# ------------------------------------- NEWS------------------------------------------#


news_params = {
    "serchIn": "title, description",
    "q": "tesla",
    "sortBy": "popularity",
    "apiKey": "982b0d37196649079b8ec4a3005eb13f",
    "pageSize": 5
}
res_news = requests.get(NEWS_ENDPOINT, params=news_params).json()
news_content = [(n["title"], n["description"], n["url"]) for n in res_news["articles"]]
print(res_news)

print(abs(delta_per))
if abs(delta_per) > 3:
    if delta > 0:
        delta_message = f"🔺{round(delta_per)}"
    else:
        delta_message = f"🔻{round(delta_per)}"
    content_template = f"\nTSLA: {delta_message}% \n\n\n"
    for n in range(0, 2):
        content_template += f"News{n + 1}\n" \
                            f"Headline: {news_content[n][0]}\n\n" \
                            f"Brief: {news_content[n][1]}\n\n" \
                            f"url: {news_content[n][2]}\n\n\n"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=content_template,
        # from_="+15073846093",
        # to="+31619013911",
        from_='whatsapp:+14155238886',
        # body = 'Your appointment is coming up on July 21 at 3PM',
        to='whatsapp:+886908383685'
    )
    print(message.status)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
