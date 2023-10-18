import requests


AMOUNT = 10
BOOLEAN = "boolean"
parameters ={
    "amount": AMOUNT,
    "type": BOOLEAN
}

question_data = requests.get(url = "https://opentdb.com/api.php", params= parameters)
question_data.raise_for_status()
question_data = question_data.json()["results"]
