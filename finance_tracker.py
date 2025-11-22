"""
FinanceTracker manages the balances and transactions
"""

from pathlib import Path
from transaction import Transaction
from storage import load_data, save_data

DATA_FILE =Path("data/finances.json") 

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
	
	def add_transaction(self,transaction:Transaction):
		""" 
		Add a new transaction and update the balance.

		Parameters
		----------
		transaction : Transaction
			The transaction to be added. Must contaoning an amount and a type.

		Raises
		------
		ValueError
			If the transaction type is not "income" or "expense"
		Notes
		-----
		Automatically saves changes to file using `save_data`
		"""
		self.transactions.append(transaction)
		if transaction.transaction_type  == "income":
			self.balance = round(self.balance+transaction.amount,2)
		elif transaction.transaction_type == "expense":
			self.balance = round(self.balance-transaction.amount,2)
		else:
			print("Not expense or income error")
		data = {
			"balance": self.balance,
			"transactions": self.transactions
		}
		save_data(data)  
