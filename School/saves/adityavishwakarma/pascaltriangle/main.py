n = 6
l = []
for i in range(n):
	l.append(list())
	for j in range(i + 1):
		if i == 0:
			l[i].append(j + 1)
		else:
			if j == 0 or j == i:
				l[i].append(1)
			else:
				l[i].append(sum(l[i - 1][j - 1:j + 1]))
	
for r in l:
	for e in r:
		print(e, end = ' ')
	print()