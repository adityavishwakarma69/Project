def merge(arr, leftarr, rightarr):
    leftlen = len(leftarr)
    rightlen = len(rightarr)

    i, l, r = 0, 0, 0

    while (l < leftlen and r < rightlen):
        if leftarr[l] < rightarr[r]:
            arr[i] = leftarr[l]
            i += 1
            l += 1

        else:
            arr[i] = rightarr[r]
            i += 1
            r += 1

    while (l < leftlen):
        arr[i] = leftarr[l]
        i += 1
        l += 1

    while (r < rightlen):
        arr[i] = rightarr[r]
        i += 1
        r += 1

def mergesort(arr):

    length = len(arr)
    if length <= 1:
        return
    mid = length//2
    leftarr = arr[:mid]
    rightarr = arr[mid:] 

    mergesort(leftarr)
    mergesort(rightarr)

    merge(arr, leftarr, rightarr)

arr = [1, 4, 6, 3, 2, 9, 11, 18, 15]

mergesort(arr)

print(arr)
