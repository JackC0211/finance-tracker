import json
from datetime import date

DATA_FILE = "finances.json"

def load_data():
	with open(DATA_FILE, "r") as file:
		return json.load(file)
	
def save_data(data):
	with open(DATA_FILE, "w") as file:
		data_json = json.dumps(data)
		file.write(data_json)

