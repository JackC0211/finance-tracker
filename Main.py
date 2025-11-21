import json
from datetime import date

DATA_FILE = "finances.json"

def load_data() -> dict: # opens the file and returns all of the saved data in file
	try:
		with open(DATA_FILE, "r") as file:
			try:
				data = json.load(file)
				if "balance" not in data or "transactions" not in data:
					return {"balance": 0.0, "transactions": []}
				return data
			except ValueError:
				return {"balance": 0.0, "transactions": []}
	except FileNotFoundError:
		return {"balance": 0.0, "transactions": []}
	
def save_data(data:dict):
	with open(DATA_FILE, "w") as file:
		json.dump(data, file, indent=2)
	
def add_transaction(tx:dict):
	data = load_data()
	data["transactions"].append(tx)

	if tx["type"] == "income":
		data["balance"] += tx["amount"]
	else:
		data["balance"] -= tx["amount"]
	
	save_data(data)
	
def get_data_from_user() -> dict: # creates a dict of user input --- returns json formatted data
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

	return user_inputs

def find_balance() -> float: # TODO keep a balance saved in file somehwere to be called
	return round(load_data()["balance"],2)


def main():
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
				print(f'£{find_balance()}')
			case 2:
				add_transaction(get_data_from_user())
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