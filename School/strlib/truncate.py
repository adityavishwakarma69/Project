def truncate(st):

	new_str = ""

	flag = False

	for n in st:
		if n == ' ':
			if flag:
				new_str += ' '
				flag = False	
		else:
			new_str += n
			flag = True

	if new_str[-1] == ' ':
		new_str = new_str[:-1]

	return new_str
