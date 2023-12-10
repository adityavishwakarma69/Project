import strlib
while True:
	print('''1. Check Palindrome
2. Standard name format
3. Character Frequency
4. find and replace word
5. case change
6. truncate space (remove extra spaces)
7. ASCII converion
8. Anagram
9. Word Frequency
10. ASCII to INT
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
			st = input("Enter name : ")
			print(strlib.stdFormat(st))
		case 3:
			st = input("Enter a string : ")
			freq = strlib.charFreq(st)
			for c in freq:
				print(f"{c} occured {freq[c]} times")
		case 4:
			choice = int(input("1. Replace first occurance\n2. Replace all occurance\nEnter option : "))
			st = input("Enter the string : ")
			old = input("Enter the word to replace : ")
			new = input("Enter the replacing word : ")
			match choice:
				case 1:
					print(strlib.replaceword(st, old, new))
				case 2:
					print(strlib.replacewords(st, old, new))
				case _:
					print("Invalid option")
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
			st = input("Enter a string : ")
			print(*strlib.toascii(st), sep = ' ')
		case 8:
			st1 = input("Enter a string : ")
			st2 = input("Enter another string : ")
			if strlib.isanagram(st1, st2):
				print("Yes, The strings are anagram")
			else:
				print("No, Strings are not anagram")

		case 9:
			st = input("Enter a string : ")
			freq = strlib.wordFreq(st)
			for k in freq:
				print(f"word \'{k}\' occured {freq[k]} times")
		case 10:
			st = input("Enter numeric string : ")
			print(type(n := strlib.toInt(st)))
			print(n)
		case 11:
			break

		case _:
			print("Invalid Option")
