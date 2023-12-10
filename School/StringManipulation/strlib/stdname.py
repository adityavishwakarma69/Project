def stdFormat(st):
	split = []
	buff = ''
	w = 0
	for i in range(len(st)):
		if st[i] == ' ':
			w += 1
			split.append(buff)
			buff = ''
			continue
		buff = buff + st[i]
	split.append(buff)
	formated = ""
	for i in range(len(split)):
		if formul
	return split
print(stdFormat("Aditya Kumar Vishwakarma"))