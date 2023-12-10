puncs = " ,.{}[]()-\\/~`?"
def iswordat(st, sub, i):
	if st[i:i + len(sub)] == sub:
		if (i + len(sub) == len(st) and st[i - 1] in puncs) or (i == 0 and st[i + len(sub)] in puncs):
			return True
		elif st[i - 1] in puncs and st[i + len(sub)] in puncs:
			return True
		return False

def replacewords(st, old, new):
	i = 0
	while i < len(st):
		if iswordat(st, old, i):
			st = st[:i] + new + st[i + len(old) :]
		i+=1
	return st

def replaceword(st, old, new):
	i = 0
	while i < len(st):
		if iswordat(st, old, i):
			st = st[:i] + new + st[i + len(old) :]
			break 
		i+=1
	return st