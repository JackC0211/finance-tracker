from pathlib import Path
import json
from transaction import Transaction
from storage import load_data, save_data

DATA_FILE =Path("data/finances.json") 

class FinanceTracker:
	balance:float
	transactions:list[Transaction]
	def __init__(self):
		self.balance, self.transactions = load_data().values()
	
	def add_transaction(self,transaction:Transaction):
		self.transactions.append(transaction)
		if transaction.transaction_type  == "income":
			self.balance = round(self.balance+transaction.amount,2)
		elif transaction.transaction_type == "expense":
			self.balance = round(self.balance-transaction.amount,2)
		else:
			print("Not expense or income error")
		data = {
			"balance": self.balance,
			"transactions": [transaction.to_dict() for transaction in self.transactions]
		}
		save_data(data)
