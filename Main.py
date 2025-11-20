import json
from datetime import date

DATA_FILE = "finances.json"

def load_data() -> list[dict]: # opens the file and returns all of the saved data in file
	try:
		with open(DATA_FILE, "r") as file:
			return json.load(file)
	except FileNotFoundError:
		return []
	
def save_data(data:dict):
	data_list:list = load_data()
	data_list.append(data)
	with open(DATA_FILE, "w") as file:
		json.dump(data_list, file, indent=2)
	

def get_data_from_user() -> dict: # creates a dict of user input --- returns json formatted data
	user_inputs:dict = {}

	# type
	while True:
		entry_type = input("type (expense/income): ").strip().lower()
		if entry_type in ['expense','income']:
			user_inputs['type'] = entry_type
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
	date_input = input(f"date (YYYY-DD-MM) [default {date.today()}]: ").strip()
	user_inputs['date'] = date_input if date_input else str(date.today().strftime("%Y-%d-%m"))
	
	# Description
	user_inputs['description'] = input("description: ").strip() or ""

	return user_inputs


if __name__ == '__main__':
	inputs = get_data_from_user()
	save_data(inputs)