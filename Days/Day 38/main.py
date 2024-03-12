import requests, os
import datetime as dt

# Nutritionix API
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
exercise_endpoint = os.environ["exercise_endpoint"]

# Sheety API
SHEETY_BASIC_AUTH = os.environ["SHEETY_BASIC_AUTH"]
google_sheet_endpoint = os.environ["google_sheet_endpoint"]


def main():
    exercise_text = input("Enter your exercise text: ")

    entries = create_entry(exercise_text)

    if entries:
        add_entries_to_sheet(entries)


def create_entry(exercise_text):
    headers = {
        'Content-Type': 'application/json',
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    parameters = {
        "query": exercise_text,
        "gender": "male",
        "age": "23",
        "weight_kg": "68",
        "height_cm": "180",
    }
    
    res = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
    res.raise_for_status()
    data = res.json()

    if data['exercises']:
        date = dt.datetime.now().strftime('%d/%m/%Y')
        time = dt.datetime.now().strftime('%H:%M:%S')

        entries = []

        for exercise in data['exercises']:
            entries.append({
                'sheet1': {
                    'date': date,
                    'time': time,
                    'exercise': exercise['name'].title(),
                    'duration': int(exercise['duration_min']),
                    'calories': int(exercise['nf_calories'])
                }
            })
        return entries


def add_entries_to_sheet(entries):
    headers = {
        'Authorization': SHEETY_BASIC_AUTH,
        'Content-Type': 'application/json',
    }

    for entry in entries:
        res = requests.post(url=google_sheet_endpoint, json=entry, headers=headers)
        res.raise_for_status()
        print(res.status_code)


if __name__ == '__main__':
    main()  
