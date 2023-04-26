from multiprocessing.connection import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"  #https://www.alphavantage.co/support/#api-key is the right one
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = 'YTKNWTFBFQHQO45G'
NEWS_API_KEY = 'gf56789654fghjgfdsyui54'




stock_parameters ={
    "function" : "TIME_SERIES_DAILY", 
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)



day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)



difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
if difference>0:
    updown = "🔺"
else:
    updown = "🔻"
#print(difference)


diff_percent = round((difference / float(yesterday_closing_price))*100)
print(diff_percent)


if abd(diff_percent) > 1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    print(articles)


    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {updown} {diff_percent}% \n Headline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles] 

    client = Client(TWILIO_STD, TWILIO_AUTH_TOKEN)

    for articles in formatted_articles:
        message = client.messages.create(
            body =articles,
            from_ = "+161572385037",
        )



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are 
required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, 
near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are 
required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, 
near the height of the coronavirus market crash.
"""

