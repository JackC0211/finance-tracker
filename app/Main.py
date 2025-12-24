from finance_tracker import FinanceTracker
from input_handler import input_transaction, find_existing_transaction
from plots import plot_expenses

def handle_edit_transaction(app_object: FinanceTracker) -> None:
	transaction_to_edit = app_object.find_transaction(find_existing_transaction())
	if transaction_to_edit:
		print("1 - type (expense/income)")
		print("2 - amount")
		print("3 - category")
		print("4 - date (YYYY-MM-DD)")
		print("5 - description")
		choice = input("Choice: ").strip()

		if choice == "1":
			new_type = input("New type (expense/income): ").strip().lower()
			if new_type in ("expense", "income"):
				app_object.update_transaction(transaction_to_edit, transaction_type=new_type)
			else:
				print("Invalid type.")
		elif choice == "2":
			try:
				new_amount = float(input("New amount: ").strip())
				app_object.update_transaction(transaction_to_edit, amount=new_amount)
			except ValueError:
				print("Invalid amount.")
		elif choice == "3":
			new_cat = input("New category: ").strip() or "General"
			app_object.update_transaction(transaction_to_edit, category=new_cat)
		elif choice == "4":
			new_date = input("New date (YYYY-MM-DD): ").strip()
			app_object.update_transaction(transaction_to_edit, date=new_date)
		elif choice == "5":
			new_desc = input("New description: ").strip()
			app_object.update_transaction(transaction_to_edit, description=new_desc)			

def user_selection():
	app_object = FinanceTracker()
	while True:
		print("1- Check Balance")
		print("2- Add Transaction")
		print("3- Edit Transaction")
		print("4- Delete Transaction")
		print("5- Plot Expenses")
		print("6- Close \n ")
		try:
			answer = int(input())
		except ValueError:
			print("Invalid input.\n")
			continue
		match answer:
			case 1:
				print(f'\n£{app_object.get_balance()} \n') #FIXME round balance
			case 2:
				myTransaction = input_transaction()
				app_object.add_transaction(myTransaction)
			case 3:
				handle_edit_transaction(app_object)
			case 4:
				transaction_to_remove = app_object.find_transaction(find_existing_transaction()) 
				if transaction_to_remove :
					app_object.delete_transaction(transaction_to_remove)
			case 5:
				plot_expenses(app_object.transactions)
			case 6:
				break
			case _:
				print("Invalid selection.")


def main() -> None:
	user_selection()


if __name__ == '__main__':
	main()