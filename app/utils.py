
def is_hex(s: str) -> bool:
	"""Takes an input and checks if it could be hexadecimal"""
	try:
		int(s,16)
		return True
	except ValueError:
		return False