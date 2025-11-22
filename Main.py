from datetime import date
import json

from finance_tracker import FinanceTracker
from transaction import Transaction


	
def get_data_from_user() -> Transaction: # creates a dict of user input --- returns json formatted data
	user_inputs:dict = {}

	# type
	while True:
		input_type = input("type (expense/income): ").strip().lower()
		if input_type in ['expense','income']:
			user_inputs['type'] = input_type
			break
		print("Please enter 'expense' or 'income'.")

	#amount
	while True:
		try:
			amount = float(input("amount: ").strip())
			user_inputs['amount'] = amount
			break
		except ValueError:
			print("Please enter a valid amount.")

	
	# category
	user_inputs['category'] = input("category: ").strip() or "General"

	# date (defaults to current day)
	date_input = input(f"date (YYYY-MM-DD) [default {date.today()}]: ").strip()
	user_inputs['date'] = date_input if date_input else str(date.today().strftime("%Y-%m-%d"))
	
	# Description
	user_inputs['description'] = input("description: ").strip() or ""

	return Transaction(
    user_inputs["type"],
    user_inputs["amount"],
    user_inputs["category"],
    user_inputs["date"],
    user_inputs["description"]
)


def main():
	app_object = FinanceTracker()
	while True:
		print(
			"\n1- Check Balance\n"
			"2- Add Transaction\n"
			"3- Delete Transaction\n"
			"4- Edit Transaction\n"
			"5- Close\n"
		)
		try:
			answer = int(input())
		except ValueError:
			print("Invalid input.\n")
			continue

		match answer:
			case 1:
				print(f'£{app_object.balance}')
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