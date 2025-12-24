"""
Transaction model used to represent a single record
"""
from uuid import uuid4
class Transaction:
	"""
	Represents a single financial transactions
	
	Parameters
	----------
		transaction_type : str
			Either ``"income"`` or ``"expense"``
		amount : float
			The value of the transaction
		category : str
			Category describing where the money was spent/earned
		date : str
			Date of transaction in ``YYYY-MM-DD`` format
		description : str, optional 
			Text about transaction. Defaults to an empty string

	Attributes
	----------
	transaction_type : str
	amount : float
	category : str
	date : str
	description : str
	"""
	def __init__(self, transaction_type:str, amount:float, category:str, date:str, description:str= ""):
		self.transaction_type = transaction_type
		self.amount = amount
		self.category = category
		self.date = date
		self.description = description
		self.id = str(uuid4())

	def to_dict(self) -> dict:
		"""
		Convert the Transaction object to a dictionary
		
		Returns
		-------
			dict
				A dictionary representation of the transaction
		"""
		return {
			"transaction_type": self.transaction_type,
			"amount": self.amount,
			"category": self.category,
			"date": self.date,
			"description": self.description
		}
	def __str__(self) -> str:
		"""Returns a readable string of the transaction"""
		return f"{self.date} | {self.transaction_type} | £{self.amount} | {self.category} | {self.description}"
	
	def __eq__(self, other):
		if not isinstance(other, Transaction):
			return False
		return self.__dict__ == other.__dict__
