from datetime import date

from transaction import Transaction
from utils import is_hex

def input_transaction(isedit=False) -> Transaction:
	"""
	Collects user input for all fields to create a transaction
	
	Returns
	-------
	Transaction
		- transaction type ("income" or "expense")
		- amount (float)
		- category (string, defaults to "General" when empty)		
		- date (string in YYYY-MM-DD format, defaults to today)
		- description (optional string)

	"""
	
	user_inputs:dict[str, str|float] = {}
	if isedit:
		print("Enter the details of the transaction you are looking for: ")
	while True:
		input_type = input("type (expense/income): ").strip().lower()
		if input_type in ['expense','income']:
			user_inputs['transaction_type'] = input_type
			break
		print("Please enter 'expense' or 'income'.")

	while True:
		try:
			amount = float(input("amount: ").strip())
			user_inputs['amount'] = amount
			break
		except ValueError:
			print("Please enter a valid amount.")

	user_inputs['category'] = input("category: ").strip() or "General"

	date_input = input(f"date (YYYY-MM-DD) [default {date.today()}]: ").strip()
	user_inputs['date'] = date_input if date_input else str(date.today().strftime("%Y-%m-%d"))
	
	user_inputs['description'] = input("description: ").strip() or ""

	return Transaction(
    user_inputs["transaction_type"],
    user_inputs["amount"],
    user_inputs["category"],
    user_inputs["date"],
    user_inputs["description"]
)

def find_existing_transaction():
	print("Enter the ID of the transction you are looking for: ")
	while True:
		inputted_id = input()
		if len(inputted_id) != 36:
			print("Incorrect number of digits. Try again: ")
			continue
		if not is_hex(inputted_id):
			print("IDs only contain hexadecimal digits. Try again: ")
			continue
		break
		
	return inputted_id