def iswordat(st, sub, i):
	if st[i:i + len(sub)] == sub:
		if (i + len(sub) == len(st) and st[i - 1] == ' ') or (i == 0 and st[i + len(sub)] == ' '):
			return True
		elif st[i - 1] == ' ' and st[i + len(sub)] == ' ':
			return True
		return False

def replacewords(st, old, new):
	i = 0
	while i < len(st):
		if iswordat(st, old, i):
			st = st[:i] + new + st[i + len(old) :]
		i+=1
	return st