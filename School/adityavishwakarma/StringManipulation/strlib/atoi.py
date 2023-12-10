def toInt(st):
	num = 0
	for c in st:
		ac = ord(c)
		if ac >= 48 and ac <= 57:
			num = num * 10 + ac - 48
		else:
			raise Exception(f"Unable to parse string, character \'{c}\' is not numeric")

	return num