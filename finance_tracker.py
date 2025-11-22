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

		while True:
			print(
'''
What would you like to edit?:
0 - exit editor
1 - transaction_type
2 - amount
3 - category
4 - date
5 - description
''')
			try: # value check
				answer = int(input("Choice: ").strip())
			except ValueError:
				print("Invald Number, try again: ")
				continue

			if answer == 0: # exit case
				print("exiting editor.")
				break

			if answer not in edit_options: # checks if valid value
				print("invalid option, try again.")
				continue

			field_name, converter = edit_options[answer]

			new_value_raw = input(f"Enter a new value for '{field_name}': ").strip() # user input to change

			try:
				new_value = converter(new_value_raw) # converts based on lambda function
				if new_value is None:
					raise ValueError
			except Exception:
				print("Invalid value.")
				continue
			
			setattr(transaction_to_edit, field_name, new_value) # chnaged the ransaction with the new input
			print(f"{field_name} edited succesfully!")

			data = {
				'balance': self.get_balance(),
				'transactions': self.transactions
			}
			save_data(data)

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