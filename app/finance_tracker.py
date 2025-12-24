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
	
	def find_transaction(self,inputted_transaction:Transaction) -> Transaction | None:
		"""
		find an existing transaction from file
		
		Parameters
		----------
		inputted_details : Transaction
			all of the details given by the user to find the wanted transaction

		Returns
		-------
		
		"""
		
		all_transactions:list[Transaction] = self.transactions
		# Check that list is full of Transaction class
		all_transactions = [
			Transaction(**t) if isinstance(t, dict) else t
			for t in all_transactions
		]

		for t in all_transactions: # checks all the transactions from file
			if inputted_transaction == t:
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

	def edit_transaction(self,transaction_to_edit:Transaction):
		"""
		Edits an existing transaction

		Parameters
		----------
		transaction_to_edit : Transaction
			The transaction that is to be changed

		Notes
		-----
		Automatically saves changes to file using `save_data`

		Takes user input to change certain elements of the Transaction
		"""
		edit_options = { # all 5 edit options with how to format them
			1: ("transaction_type", lambda x: x if x in ['income','expense'] else None),
			2: ("amount", lambda x: float(x)),
			3: ("category", lambda x: x),
			4: ("date", lambda x: x),
			5: ("description", lambda x: x)
		}
		def get_valid_input(prompt: str, converter):
			while True:
				raw = input(prompt).strip()
				try:
					value = converter(raw)
					if value is None:
						raise ValueError
					return value
				except Exception:
					print(Exception)

		while True:
			print("\nEdit options (0 to exit):")
			for key, value in edit_options.items():
				print(f"{key} - {value[0]}")
			answer = int(input("Choice: ").strip())

			if answer == 0: # exit case
				break

			if answer not in edit_options:
				print("invalid option")
				continue

			field_name, converter = edit_options[answer]
			new_value = get_valid_input(f"Enter a new value for '{field_name}': ", converter) # user input to change
			setattr(transaction_to_edit, field_name, new_value) # chnaged the ransaction with the new input
			self.save()
			print(f"{field_name} edited succesfully!")

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