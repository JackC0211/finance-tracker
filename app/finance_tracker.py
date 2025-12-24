"""
FinanceTracker manages the balances and transactions
"""

from pathlib import Path
from transaction import Transaction
from storage import load_data, save_data

DATA_FILE = Path("data/finances.json") 

class FinanceTracker:
	"""Main class responsible for managing transactions and balance
	
	The class loads existing transaction data from file,
	provides methods to update the balance and save changes
	
	Attributes
	----------
	balance : float
		The running total of all transactions (Balance in account)
	transactions : list of Transaction
		List of all recorded transactions
	"""
	balance:float
	transactions:list[Transaction]
	def __init__(self):
		""" 
		Initialise a FinanceTracer instance

		Loads stored balance and transaction history from file using `load_data`.
		"""
		data = load_data()
		self.balance = data["balance"]
		self.transactions = data["transactions"]
	
	def find_transaction(self,inputted_id:str) -> Transaction | None:
		for t in self.transactions:
			if inputted_id ==t.id:
				return t
		print("Unable to find transaction")
		return None


	def add_transaction(self,transaction:Transaction):
		""" 
		Add a new transaction and update the balance.

		Parameters
		----------
		transaction : Transaction
			The transaction to be added. Must contaoning an amount and a type.

		Notes
		-----
		Automatically saves changes to file using `save_data`
		"""
		self.transactions.append(transaction)
		self.save()  

	def update_transaction(self,transaction: Transaction, **changes) -> None:
		allowed = {"transaction_type", "amount", "category", "date", "description"}

		for field, value in changes.items():
			if field not in allowed:
				raise ValueError(f"Unknown field: {field}")
			setattr(transaction, field, value)
		self.save()


	def delete_transaction(self,transaction_to_remove:Transaction):
		self.transactions.remove(transaction_to_remove)
		self.save()
	
	def get_balance(self) -> float:

		"""Find the balance in the account
		
		Returns
		-------
		balance : float
			the running balance in the account
		"""
		self.balance =round(sum(
			-t.amount if t.transaction_type == "expense" else +t.amount 
			for t in self.transactions), 2)
		
		return self.balance
	
	def save(self):
		save_data({'balance': self.get_balance(), 'transactions': self.transactions})