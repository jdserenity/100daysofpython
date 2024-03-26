import bs4, requests, smtplib; import confidential; from email.message import EmailMessage

DEBUG = False

AMAZON_URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

HEADERS = confidential.HEADERS

data = {}


def main():
    global data

    data = get_data()

    if is_price_below_threshold(): send_email()


def get_data():
    r = requests.get(AMAZON_URL)
    r.raise_for_status()
    
    soup = bs4.BeautifulSoup(r.text, 'lxml')

    print(str(soup.title.text.split(':')[1].strip()))

    data = {'title': soup.title.text.split(':')[1].strip()}

    prices = [price.text for price in soup.find_all(class_='a-price-whole')]
    fractions = [price.text for price in soup.find_all(class_='a-price-fraction')]

    data['price'] = prices[1] + fractions[1]

    return data


def is_price_below_threshold():
    if DEBUG:
        return True
    return True if float(data['price']) < 100 else False


def send_email():
    my_email = confidential.MY_EMAIL
    my_app_password = confidential.APP_PASSWORD

    msg = EmailMessage()
    msg.set_content(f"\"{data['title']}\" is now ${data['price']}\n\n{AMAZON_URL}")

    msg['Subject'] = "Amazon product price went down below threshold sir"
    msg['From'] = my_email
    msg['To'] = confidential.YAHOO_TEST_EMAIL

    with smtplib.SMTP("smtp.gmail.com") as smtp:    
        smtp.starttls()
        smtp.login(user=my_email, password=my_app_password)
        smtp.send_message(msg)


if __name__ == '__main__':
    main()