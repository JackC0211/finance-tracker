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

	def save(self):
		with open(DATA_FILE,'w') as file:
			data = {
				"balance": self.balance,
				"transactions": [t.to_dict() for t in self.transactions]
				}
			json.dump(data, file, indent=2)

	def add_transaction(self,transaction:Transaction):
		self.transactions.append(transaction)
		if transaction.transaction_type  == "income":
			self.balance = round(self.balance+transaction.amount,2)
		elif transaction.transaction_type == "expense":
			self.balance = round(self.balance-transaction.amount,2)
		else:
			print("Not expense or income error")
		self.save()

