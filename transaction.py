
class Transaction:
	def __init__(self, transaction_type:str, amount:float, category:str, date:str, description:str= ""):
		self.transaction_type = transaction_type
		self.amount = amount
		self.category = category
		self.date = date
		self.description = description
	
	def to_dict(self) -> dict:
		return {
			"transaction_type": self.transaction_type,
			"amount": self.amount,
			"category": self.category,
			"date": self.date,
			"description": self.description
		}
	def __str__(self) -> str:
		return f"{self.date} | {self.transaction_type} | £{self.amount} | {self.category} | {self.description}"