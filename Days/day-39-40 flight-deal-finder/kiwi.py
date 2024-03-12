import datetime as dt; import requests;

DEBUG = False

if DEBUG:
    import json;

KIWI_API_KEY = 'nLnBKIcoNZGQbnYhpJk-3x6Lkop7x5q3'
KIWI_ENDPOINT = 'https://api.tequila.kiwi.com'
KIWI_SEARCH_ENDPOINT = '/search'
KIWI_HEADERS = {
        'apikey': KIWI_API_KEY,
    }

DEPARTURE_CITIES = [{'IATA': 'YOW', 'City': 'Ottawa'}, {'IATA': 'YYZ', 'City': 'Toronto'}, {'IATA': 'YUL', 'City': 'Montreal'}]

TODAY = dt.datetime.now().strftime('%d/%m/%Y')
SIX_MONTHS_FROM_NOW = (dt.datetime.now() + dt.timedelta(days=180)).strftime('%d/%m/%Y')

TODAY_PLUS_ONE_WEEK = (dt.datetime.now() + dt.timedelta(days=7)).strftime('%d/%m/%Y')
SIX_MONTHS_FROM_NOW_PLUS_ONE_WEEK = (dt.datetime.now() + dt.timedelta(days=188)).strftime('%d/%m/%Y')


class Kiwi:
    def __init__(self):
        self.best_flights = []

    def search_for_cheapest_flight_in_each_city(self, cities_to_search):

        for city_to in cities_to_search:
            print(city_to['city'])
            lowest_price = 10000000000
            best_flight = {}
            
            for city_from in DEPARTURE_CITIES:
                params = {
                    'fly_from': city_from['IATA'],
                    'fly_to': city_to['iataCode(s)'],
                    'date_from': TODAY,
                    'date_to': SIX_MONTHS_FROM_NOW,
                    'return_from': TODAY_PLUS_ONE_WEEK,
                    'return_to': SIX_MONTHS_FROM_NOW_PLUS_ONE_WEEK,
                    'nights_in_dst_from': 1,
                    'nights_in_dst_to': 14,
                    'limit': 10,
                    }
                
                res = requests.get(url=KIWI_ENDPOINT + KIWI_SEARCH_ENDPOINT, headers=KIWI_HEADERS, params=params)
                res.raise_for_status()
                data = res.json()
                
                if DEBUG:
                    # comment out data = res.json()
                    with open('data_cities_to.json', 'r+') as f:
                        data = json.dump(res.json(), f)
                    
                    with open('data_cities_to.json', 'r') as f:
                        data = json.load(f)

                if len(data['data']) > 0:
                    for item in data['data']:

                        if DEBUG:
                            for key in item.keys():
                                print(key, end='\n\n')

                        if item['availability'] != {'seats': None} and int(item['price']) < lowest_price:
                            lowest_price = int(item['price'])
                            best_flight = {
                                'price': item['price'],
                                'deep_link': item['deep_link'],
                                'availability': item['availability'],
                                'fly_duration': item['fly_duration'],
                                'nightsInDest': item['nightsInDest'],
                                'flyFrom': item['flyFrom'],
                                'flyTo': item['flyTo'],
                                'dTime': dt.datetime.fromtimestamp(item['dTime']).strftime('%d/%m/%Y'),
                                'aTime': dt.datetime.fromtimestamp(item['aTime']).strftime('%d/%m/%Y'),
                                'from': f'{item['cityFrom']}, {item['countryFrom']['name']}',
                                'to': f'{item['cityTo']}, {item['countryTo']['name']}',
                            }

            if DEBUG:
                print('num entries', len(data['data']))
                print('best flight', best_flight, end='\n\n')

            self.best_flights.append(best_flight)
            print('done\n\n')
        
        return self.best_flights