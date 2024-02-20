import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api = "P5OO1Q8X18A44BZK"

r_params ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api,
}


response = requests.get(STOCK_ENDPOINT, params=r_params)
data = response.json()["Time Series (Daily)"]
print(data)
data_list = [value for (key, value) in data.items()]


yesterday_data = data_list[0]
print(yesterday_data)
yesterday_close_price = yesterday_data["4. close"]
print(yesterday_close_price)
today_data = data_list[1]
today_price = today_data["4. close"]
print(today_price)
pos_diffrence = abs(float(yesterday_close_price) - float(today_price))

print(pos_diffrence)
percentage_difference = (pos_diffrence/float(yesterday_close_price)) * 100
print(percentage_difference)
api_2 = "f4981bd7ad1c4b8f8e44fdcce537a732"
n_params ={
    "qInTitle":COMPANY_NAME,
    "apikey": api_2,
}

if percentage_difference > 5:
    n_response= requests.get(NEWS_ENDPOINT,params=n_params)
    articles=n_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)




