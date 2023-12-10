filename = input("Enter the name of file : ")

try:
	file = open(filename, 'r')
except:
	print(f"Unable to open File {filename}")
	exit()

data = file.read()

file.close()

file = open("copyof" + filename, 'w')
file.write(data)
file.close()