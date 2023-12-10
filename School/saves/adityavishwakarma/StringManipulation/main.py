import strlib
while True:
	print('''1. Check Palindrome
2. Standard name format
3. character frequency
4. find and replace word
5. case change
6. truncate space (remove extra spaces)
7. ASCII converion
8. Anagram
11. Exit''')
	opt = int(input("Enter Option : "))

	match opt:
		case 1:
			st = input("Enter a String : ")
			if strlib.isPalindrome(st):
				print("The given string is palindrome")
			else:
				print("The given string is not palindrome")
		case 2:
			pass
		case 3:
			pass
		case 4:
			pass
		case 5:
			st = input("Enter a string")
			print('''1. Title Case
2. Upper Case
3. Lower Case
4. Toggle Case''')
			choice = int(input("Enter Option : "))
			match choice:
				case 1:
					print(strlib.titleCase(st))
				case 2:
					print(strlib.upperCase(st))
				case 3:
					print(strlib.lowerCase(st))
				case 4:
					print(strlib.toggleCase(st))
		case 6:
			st = input("Enter a string : ")
			print(strlib.truncate(st))
		case 7:
			pass

		case 11:
			break

		case _:
			print("Invalid Option")