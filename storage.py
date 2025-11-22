import json
from pathlib import Path
from transaction import Transaction
DATA_FILE = Path("data/finances.json")

def load_data() -> dict:
	try:
		with open(DATA_FILE,'r') as file:
			try:
				return json.load(file)
			except ValueError:
				return {"balance": 0.0,"transactions": []}
	except FileNotFoundError:
		return {"balance": 0.0,"transactions": []}
		
def save_data(data:dict) -> None:
	with open(DATA_FILE,'w') as file:
		json.dump(data, file, indent=2)


help(save_data)