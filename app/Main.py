from finance_tracker import FinanceTracker
from input_handler import input_transaction, find_existing_transaction
from plots import plot_expenses

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
				transaction_to_edit = app_object.find_transaction(find_existing_transaction()) 
				if transaction_to_edit :
					app_object.edit_transaction(transaction_to_edit)
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