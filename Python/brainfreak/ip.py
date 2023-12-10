import sys

try:
	file = open(sys.argv[1], 'r')
except:
	raise Exception(f"NO SUCH THING NAMED {sys.argv[1]} EXISTS YOU DUMMY")

code = file.read() + '~'


eoc = '~'
i = 0


run = [0] 
p = 0

stack = []

while not code[i] == eoc:

	match code[i]:

		case '<':
			if p == 0:
				run.insert(0, 0)
			p -= 1

		case '>':
			if p + 1 == len(run):
				run.append(0)
			p += 1

		case '+':
			run[p] += 1

		case '-':
			run[p] -= 1

		case '.':
			print(chr(run[p]), end = "")

		case ',':
			run[p] = input()[0]

		case '[':
			if not run[p] == 0:
				stack.append(i)
		
		case ']':
			if not run[p] == 0:
				i = stack[-1]
			else : stack.pop()

	i += 1