from collections import defaultdict

import matplotlib.pyplot as plt

def plot_expenses(transactionsToPlot):
	expenses = defaultdict(float)
	for t in transactionsToPlot:
		if t.transaction_type == "expense":
			expenses[t.category] += t.amount 

	if not expenses:
		print("No expenses")
		return
	
	categories = list(expenses.keys())
	amounts = list(expenses.values())

	plt.figure(figsize=(6,6))
	plt.pie(amounts, labels=categories, autopct="%1.1f%%")
	plt.title("expenses by category")
	plt.show()