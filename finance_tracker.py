from pathlib import Path
import json
from transaction import Transaction


DATA_FILE =Path("data/finances.json") 



class FinanceTracker:

	def __init__(self):
		self.balance = 0.0
		self.transactions = []
		self.load_file()

	def load_file(self):
		if DATA_FILE.exists():
			with open(DATA_FILE,'r') as file:
				data:dict = json.load(file)
				self.balance = data.get("balance", 0.0)
				self.transactions = [Transaction(**t) for t in data.get("transactions", [])]