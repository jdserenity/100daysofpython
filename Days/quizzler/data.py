import requests
# num_questions = 10

params = {
    "amount": 10,
    'type': 'boolean'
}
r = requests.get(url='https://opentdb.com/api.php', params=params)
r.raise_for_status()
question_data = r.json()['results']
