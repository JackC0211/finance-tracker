"""
Where all of the file handing occurs - saving and loading the data from the file
"""

import json
from pathlib import Path
from transaction import Transaction
DATA_FILE = Path("data/finances.json")

def load_data() -> dict:
	"""Load the finance data from JSON file
	
	Returns
	-------

		dict
		  a dictionary with keys:
			- "balance" : float
				The current account balance
			- "transactions" : list of Transaction objects
				List of all recorded transactions
		"""
	if not DATA_FILE.exists():
		return {"balance": 0.0,"transactions": []}
	
	with open(DATA_FILE,'r') as file:
		try:
			data = json.load(file)
		except ValueError:
			return {"balance": 0.0,"transactions": []}
		
	transactions = [
			Transaction(**t) if isinstance(t, dict) else t
			for t in data.get("transactions", [])
		]
	balance = data.get("balance", 0.0)
	return {"balance": balance, "transactions": transactions}

def save_data(data:dict) -> None:
	"""
	Save the finance data into the JSON file
	
	Parameters
	----------
		data : dict ('balance' , 'transactions')
			The full finance tracker data structure
	"""
	data_to_save = {
		"balance": data["balance"],
		"transactions": [t.to_dict() for t in data["transactions"]]
	}
	with open(DATA_FILE,'w') as file:
		json.dump(data_to_save, file, indent=2)

