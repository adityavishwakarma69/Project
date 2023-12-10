def bubblesort(lst):
    for i in range(len(lst) - 1):
        flag = False
        for j in range(len(lst) - 1 - i):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                
lst = [9, 2, 23, 76, 43]
bubblesort(lst)
print(lst)
