import requests
import yfinance as yf

STOCK = "TSLA"
COMPANY_NAME = "Strive Asset Management"


def main():
    # using yfinance instead
    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    ticker = yf.Ticker(STOCK)

    hist = ticker.history(period='2d')

    closes = []
    for close in hist['Close'].iloc:
        closes.insert(0, float(format(close, '.2f')))

    last_close = closes[0]
    penultimate_close = closes[1]

    close_delta = last_close / penultimate_close
    pct_close_delta = round((1.0 - close_delta) * 100, 2)
    print(pct_close_delta)

    if pct_close_delta >= 5 or pct_close_delta <= -5:
        news = ticker.news[:3]
        # print(news)
        headlines = [item['title'] for item in news]
        links = [item['link'] for item in news]
        inc_or_dec = 'increased' if pct_close_delta < 0 else 'decreased'
        title = f"{STOCK} {inc_or_dec} by {pct_close_delta}% since last close"
        message = (f"News headlines possibly responsible for this change are:\n\n"
                   f"{headlines[0]}\n{links[0]}\n\n"
                   f"{headlines[1]}\n{links[1]}\n\n"
                   f"{headlines[2]}\n{links[2]}\n\n")

        params = {
            'accountKey': '74n56l3n00ppg4l',
            'title': title,
            'message': message,
        }

        res = requests.get('https://alertzy.app/send', params=params)
        res.raise_for_status()
        print(res.content)


# not using this, using yfinance instead
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# news_res = requests.get('')

# Not using Twilio, will use alertzy instead
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == '__main__':
    main()
