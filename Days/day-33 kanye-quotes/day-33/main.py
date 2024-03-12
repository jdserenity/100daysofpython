import smtplib
import requests
import datetime as dt

MY_LAT = 45.496360
MY_LONG = -77.754610

my_email = 'jdangelorg@gmail.com'
app_password = 'fgky kaxl sdjh ahsj'


def main():
    iss_r = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_r.raise_for_status()

    iss_lat = float(iss_r.json()['iss_position']['latitude'])
    iss_long = float(iss_r.json()['iss_position']['longitude'])

    params = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }
    sun_r = requests.get(url='https://api.sunrise-sunset.org/json', params=params)
    sun_r.raise_for_status()

    sunrise = [int(val) for val in sun_r.json()['results']['sunrise'].split('T')[1].split('+')[0].split(':')]
    sunset = [int(val) for val in sun_r.json()['results']['sunset'].split('T')[1].split('+')[0].split(':')]

    time_now = dt.datetime.now().time().replace(microsecond=0)
    sunrise_time = dt.datetime.today().replace(hour=sunrise[0], minute=sunrise[1], second=sunrise[2],
                                               microsecond=0).time()
    sunset_time = dt.datetime.today().replace(hour=sunset[0], minute=sunset[1], second=sunset[2],
                                              microsecond=0).time()

    # if it is dark outside where I am
    if not sunset_time < time_now < sunrise_time:
        # and the iss is above where I am
        if near_iss(iss_lat, iss_long):
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=app_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=my_email,
                                    msg=f"Subject:You can see the ISS outside right now\n\nLook up 👍")


def near_iss(iss_lat, iss_long):
    if MY_LAT + 5 >= iss_lat >= MY_LAT - 5:
        if MY_LONG + 5 >= iss_long >= MY_LONG - 5:
            return True
    return False


if __name__ == '__main__':
    main()
