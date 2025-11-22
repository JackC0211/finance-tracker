from datetime import date

from finance_tracker import FinanceTracker
from input_handler import input_transaction_new

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
				print(f'\n£{app_object.balance} \n') #FIXME round balance
			case 2:
				myTransaction = input_transaction_new()
				app_object.add_transaction(myTransaction)
			case 3:
				pass #TODO add a way to delete a transaction - maybe withj a date, amount and description
			case 4:
				pass #TODO add a way to delete a transaction
			case 5:
				break
			case _:
				print("Invalid selection.")


if __name__ == '__main__':
	main()