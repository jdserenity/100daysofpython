import requests
import datetime as dt

ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'jdjimenez77'
TOKEN = 'Rg2fWkM$RWjtqBDCDBlROL0Bvyu7wmW2PCRBzzNXR$15hsjCrlgHVtiXak0ZXF$7wsJcmfxNdf^7cAf*Iv3atukerOpaMf5JCJ^'
GRAPH_ID = 'graph-project'

# user_create_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",

headers = {
    'X-USER-TOKEN': TOKEN
}

# params = {
#     "id": GRAPH_ID,
#     "name": "Graph Project",
#     "unit": "kilometer",
#     "type": "int",
#     "color": "ajisai",
# }

# res = requests.post(url=f"{ENDPOINT}/{USERNAME}/graphs", headers=header, json=params)

today = dt.datetime.now()

params = {
    "quantity": '100',
}

res = requests.delete(url=f"{ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}", headers=headers)
# res.raise_for_status()
print(res.text)
