n = 6
for i in range(n):
    for j in range(n - i):
        print(chr(65 + j), end = "")
    print()
