import requests, json;

DEBUG = False

SHEETY_ENDPOINT = 'https://api.sheety.co/1721e5d903e2b8b90a3a0e8a158e9c59/flightDealFinderDay3940'
PRICES_ENDPOINT = '/prices'
USERS_ENDPOINT = '/users'
SHEETY_BASIC_AUTH = 'Basic amRhdWdpbnRlbDpSNVczRWJmM3hLUnQyJkgmWGJyeFNFekIza0xEYXZ2YzNIdHdGeFUqXjVmRjMwcmFJb2FUJlA0Qk9zZlFqJW8lU3Z6NXF1cipteTNYNjNhYWZHdXBMbE80RzFLRSZYQFcxV1U='
SHEETY_HEADERS = {
        'Authorization': SHEETY_BASIC_AUTH,
        'Content-Type': 'application/json',
    }


# the code is supposed to get the data from a google sheet but I'm not paying for the api so I'm just using a local file


class Sheety:
    def __init__(self):
        pass

    def get_entries_from_sheet(self):
        # res = requests.get(url=f'{SHEETY_ENDPOINT}{PRICES_ENDPOINT}')
        # res.raise_for_status()

        # with open('sheety_data.json', 'w') as f:
        #     json.dump(res.json(), f)

        with open('sheety_data.json', 'r') as f:
            data = json.load(f)

        if DEBUG:
            for item in data['prices']:
                print(item['iataCode(s)'], end='\n\n')

        return data['prices']
    
    # def add_lowest_flight_price_to_sheet(self, best_flight, num_row):
    #     body ={
    #         'sheet1': {
    #             "lowestPrice": best_flight['price'],
    #         }
    #     }

    #     res = requests.put(url=f'{SHEETY_ENDPOINT}/{num_row}', json=body)
    #     # res.raise_for_status()
    #     print(res.status_code)

    # if best_flight:
            #     add_lowest_flight_price_to_sheet(best_flight, (cities_to_search.index(city_to)) + 2)
    
    def add_user_to_sheet(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ").lower()
        confirm_email = input("Confirm your email (for your security): ").lower()

        if email == confirm_email:
            body = {
                'user': {
                    'firstName': first_name,
                    'lastName': last_name,
                    'email': email,
                }
            }

            res = requests.post(url=f'{SHEETY_ENDPOINT}{USERS_ENDPOINT}', json=body)
            res.raise_for_status()

            if DEBUG:
                print(res.text)
                print(res.status_code)

            if res.status_code == 200:
                print("You're in the club!")

    def return_list_of_users(self):
        res = requests.get(url=f'{SHEETY_ENDPOINT}{USERS_ENDPOINT}')
        res.raise_for_status()
        data = res.json()

        print(res.json())

        return data['users']
