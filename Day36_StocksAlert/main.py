import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "DIS"
COMPANY_NAME = "WaltDisneyCo"

twilio_account_sid = "ACa3c015cc5e6c0bfd001db9f617d88b1b"
twilio_auth_token = "00f095ba6e39ef5fb3a84bba66e053b4"
client = Client(twilio_account_sid, twilio_auth_token)


def stock_change():
    url_stocks = 'https://www.alphavantage.co/query?'

    parameters_stocks = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "interval": "60min",
        "apikey": "EG8QPINFXKGCICPS",

    }

    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    response_stocks = requests.get(url_stocks, params=parameters_stocks)
    response_stocks.raise_for_status()
    data_stocks = response_stocks.json()

    # get the day data in list form so we can get value 0 (yesterday), and value 15 (day before yesterday)
    last_day = list(data_stocks["Time Series (Daily)"].keys())[0]
    previous_day = list(data_stocks["Time Series (Daily)"].keys())[1]

    # get prices for yesterday and day before
    last_day_price = float(data_stocks["Time Series (Daily)"][last_day]["4. close"])
    previous_day_price = float(data_stocks["Time Series (Daily)"][previous_day]["4. close"])
    print(previous_day_price, last_day_price)

    # work out percentage change
    percentage_change = round(((last_day_price - previous_day_price) / last_day_price * 100), 2)
    print(percentage_change)

    if percentage_change > 5:
        return f"{STOCK}: 🔺{percentage_change}%"
    elif percentage_change < -1:
        return f"{STOCK}: 🔻{percentage_change}%"


stock_alert = stock_change()

if stock_alert:
    # Get NEWS and send messages
    url = 'https://newsapi.org/v2/everything'

    # get today's date
    today = datetime.now()
    # subtract one day to get day before yesterdays date
    yesterday = today - timedelta(days=2)
    # format the date as a string in the desired format (YYYY-MM-DD)
    yesterday_str = yesterday.strftime('%Y-%m-%d')

    parameters = {
        "q": COMPANY_NAME,
        "from": yesterday_str,
        "apiKey": "7ef7ea9c8db74ae9941196f5c3e6401f",
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()

    # pull 3 articles and send message for each
    for item in range(3):
        # extract the title and description of the news article
        article = data["articles"][item]
        title = article["title"]
        description = article["description"]

        # format date string
        date_string = article["publishedAt"]
        date = datetime.fromisoformat(date_string[:-1])
        formatted_date = date.strftime("%Y-%m-%d %H:%M")

        # write message
        message = f"Stock Alert!\n{stock_alert}\n{formatted_date}\nHeadline: {title}\nBrief: {description}"
        print(message)

        # send message
        # message = client.messages.create(
        #     from_='whatsapp:+14155238886',
        #     body=f"Stock Alert!\n{message}",
        #     to='whatsapp:+34652678183'
        # )

        # message = client.messages \
        #     .create(
        #     body=message,
        #     from_='+12708125618',
        #     to='+34652678183'
        # )
        # print(message.status)
