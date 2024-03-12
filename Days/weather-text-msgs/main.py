import requests, json # noqa E401
from pushover import init, Client

OPEN_WEATHER_MAP_API_KEY = '367ed1bb956495beb5d467b8b0d1da23'
OPEN_WEATHER_MAP_API_ENDPOINT = 'http://api.openweathermap.org'
geocoding_url = '/geo/1.0/direct'
five_day_url = '/data/2.5/forecast'

LAT = 45.421532
LONG = -75.697189

COIN_GECKO_API_KEY = '	CG-EnfErcnShapS384judwFGu4p'
COIN_GECKO_API_ENDPOINT = 'https://api.coingecko.com/api/v3'
coin_price_url = '/simple/price'
coin_list_url = '/coins/list'

PUSHOVER_APP_TOKEN = 'ajpdh5iz3zzaeuwsjtqtwudjd3yetw'
PUSHOVER_API_KEY = 'u4iupyizwgqz1vrj56t5ymftgdx6sh'

open_weather_params = {
    'lat': LAT,
    'lon': LONG,
    'cnt': 40,
    'appid': OPEN_WEATHER_MAP_API_KEY
}

coin_gecko_params = {
    'ids': 'bitcoin',
    'vs_currencies': 'usd'
}


def main():
    r = requests.get(OPEN_WEATHER_MAP_API_ENDPOINT + five_day_url, params=open_weather_params)
    r.raise_for_status()

    data = json.loads(r.text)

    send_rain_notification(will_it_rain_in_next_12_hours(data))


def will_it_rain_in_next_12_hours(data):
    for item in data['list'][:40]:
        # print(item['weather'][0]['main'])
        if item['weather'][0]['main'].lower() in ['rain', 'drizzle', 'thunderstorm']:
            print(item)
            return True
    return False


def send_rain_notification(will_rain):
    if will_rain:
        init(PUSHOVER_APP_TOKEN)
        Client(PUSHOVER_API_KEY).send_message("Bring an umbrella ☔️ :)", title="It's going to rain today")


if __name__ == '__main__':
    main()
