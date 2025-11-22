from datetime import date

from finance_tracker import FinanceTracker
from input_handler import input_transaction

def main() -> None:
	app_object = FinanceTracker()
	while True:
		print("1- Check Balance")
		print("2- Add Transaction")
		print("3- Edit Transaction")
		print("4- Delete Transaction")
		print("5- Close \n ")
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
				transaction_to_edit = app_object.find_transaction(input_transaction(isedit=True)) #TODO add a way to edit a transaction - maybe withj a date, amount and description
				if transaction_to_edit :
					app_object.edit_transaction(transaction_to_edit)
			case 4:
				pass #TODO add a way to delete a transaction
			case 5:
				break
			case _:
				print("Invalid selection.")


if __name__ == '__main__':
	main()