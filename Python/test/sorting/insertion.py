from random import randint

def randlist(length, low, high):
	lst = []
	for i in range(length):
		lst.append(randint(low, high))

	return lst

def insort(arr):
	n = len(arr)
	for i in range(1, n):
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1



arr = randlist(10, 20, 100)
print(arr)
insort(arr)
print(arr)