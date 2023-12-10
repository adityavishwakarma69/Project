def isLower(st):
	return ord(st[0]) >= 97 and ord(st[0]) <= 122

def isUpper(st):
	return ord(st[0]) >= 65 and ord(st[0]) <= 90

def upperCase(st):
	for i in range(len(st)):
		if ord(st[i]) <= 122 and ord(st[i]) >= 97:
				st = st[:i] + chr(ord(st[i]) - 32) + st[i + 1:]

	return st

def lowerCase(st):
	for i in range(len(st)):
		if ord(st[i]) <= 90 and ord(st[i]) >= 65:
				st = st[:i] + chr(ord(st[i]) + 32) + st[i + 1:]

	return st

def titleCase(st):
	for i in range(len(st)):
		if st[i - 1] == ' ' or i == 0:
			st = st[:i] + upperCase(st[i]) + st[i + 1:]
		else:
			st = st[:i] + lowerCase(st[i]) + st[i + 1:]

	return st

def toggleCase(st):
	for i in range(len(st)):
		if isLower(st[i]):
			st = st[:i] + upperCase(st[i]) + st[i + 1:]
		elif isUpper(st[i]):
			st = st[:i] + lowerCase(st[i]) + st[i + 1:]

	return st

