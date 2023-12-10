import strlib.case as sc
def stdFormat(st):
	formated = ''
	buff = ''
	w = 0
	for i in range(len(st)):
		if st[i] == ' ':
			w += 1
			formated += sc.upperCase(buff[0]) + '.'
			buff = ''
			continue
		buff = buff + st[i]
	formated += sc.titleCase(buff)
	return formated
print(stdFormat("Aditya Kumar Singh"))
