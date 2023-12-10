def checkprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def nextprime(num):
    np = num + 1
    while not checkprime(np):
        np += 1
    return np

p = 2
for i in range(20):
    print(2**(p-1)*(2**p - 1))
    p = nextprime(p)
    
