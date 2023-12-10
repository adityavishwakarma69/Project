def factorize(num):
    facts = []
    for i in range(1, num//2 + 1):
        if num%i == 0:
            facts.append(i)
    return facts

def isperfect(num):
    if sum(factorize(num)) == num:
        return True
    return False

n = 1
c = 0
while c < 10:
    if isperfect(n):
        print(n)
        c+= 1
    n += 1
