from random import randint


def randSortedList(length, low, maxdiff):
	randlist = []
	for i in range(length):

		randlist.append(randint(low, low + maxdiff))
		low = randlist[-1]

	return randlist


def binarySearch(arr, elm):
	low = 0
	high = len(arr)
	mid = high // 2

	while low <= high:
		if arr[mid] < elm:
			low = mid
		elif arr[mid] > elm:
			high = mid
		else : return mid

		mid = (high + low) // 2


	return False
arr = randSortedList(10, 0, 20)
elm = arr[randint(0, len(arr) - 1)]
print(binarySearch(arr, elm))
print(elm, arr)
