import requests, smtplib;

BITLY_ACCESS_TOKEN = '453dc5f80abb7f5a5d13c0a75976f1bd623c1e22'
BITLY_ENDPOINT = 'https://api-ssl.bitly.com/v4/shorten'
BITLY_HEADERS = {
        'Authorization': f"Bearer {BITLY_ACCESS_TOKEN}",
    }
BITLY_GROUP_ID = 'Bo2shMQfiqB'
BITLY_ORGANIZATION_ID = 'Oo2shBcgjHD'

ALERTZY_ENDPOINT = 'https://alertzy.app/send'

MY_EMAIL = 'jdcanada00@gmail.com'
EMAIL_APP_PASSWORD = 'mzmh iukj arwh uelh'


class Notify:
    def __init__(self):
        pass

    def send_emails_to_users_with_discounted_flight_details(self, best_flights, cities_to_search, users):
        for i, flight in enumerate(best_flights):
            # If any of the flights found today are at least 20% cheaper than the current lowest price
            if int(flight['price']) <= int(cities_to_search[i]['lowestPrice']) * 0.8:
                title = 'Flight Deal! Check it out!'

                bitly_body = {
                    "long_url": flight['deep_link']
                }  

                res_bitly = requests.post(url=BITLY_ENDPOINT, headers=BITLY_HEADERS, json=bitly_body)
                res_bitly.raise_for_status()
                bitly_data = res_bitly.json()

                pct_difference = round(((int(cities_to_search[i]['lowestPrice']) - int(flight['price'])) / int(cities_to_search[i]['lowestPrice']) * 100), 2)

                message = f'A flight from {flight['from']} to {flight["to"]} is available for {flight["price"]} dollars. This is a {pct_difference}% decrease from the regular price! It leaves on {flight["dTime"]} and you would stay for {flight["nightsInDest"]} nights. There are {flight['availability']['seats']} available seats on the flight as of this moment. If this sounds good to you, check it out :)'

                params = {
                    'accountKey': '74n56l3n00ppg4l',
                    'title': title,
                    'message': message,
                    'link': bitly_data['link']
                }

                self.send_emails(users, params)

                # res_alertzy = requests.get(ALERTZY_ENDPOINT, params=params)
                # res_alertzy.raise_for_status()
                # print(res_alertzy.content)
        
    def send_emails(self, users, params):
        for user in users:
            to_email = user['email']

            msg = f'Subject:{params['title']}\n\n{params["message"]}'


            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=EMAIL_APP_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=to_email,
                                    msg=msg)

            
                