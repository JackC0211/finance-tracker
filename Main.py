from datetime import date

from finance_tracker import FinanceTracker
from transaction import Transaction
	
def get_data_from_user() -> Transaction:
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


def main() -> None:
	app_object = FinanceTracker()
	while True:
		print("1- Check Balance")
		print("2- Add Transaction")
		print("3- Delete Transaction")
		print("4- Edit Transaction")
		print("5- Close")
		try:
			answer = int(input())
		except ValueError:
			print("Invalid input.\n")
			continue

		match answer:
			case 1:
				print(f'£{app_object.balance}') #FIXME round balance
			case 2:
				myTransaction = get_data_from_user()
				app_object.add_transaction(myTransaction)
			case 3:
				pass #TODO add a way to delete a transaction - maybe withj a date, amount and description
			case 4:
				pass #TODO add a way to edit a transaction
			case 5:
				break
			case _:
				print("Invalid selection.")


if __name__ == '__main__':
	main()