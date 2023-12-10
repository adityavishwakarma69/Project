def find(st, sub):
    finds = []
    for i in range(len(st) - len(sub) + 1):
        if st[i : i + len(sub)] == sub:
            finds.append(i)

    return finds

def findfirst(st, sub):
    for i in range(len(st) - len(sub) + 1):
        if st[i : i + len(sub)] == sub:
            return i

    return -1

def replace(st, old, new):
    n = findfirst(st, old)
    n = n if n != -1 else None
    if n != None:
        st = st[:n] + new + st[n+len(old) :]
    return st

def replaceall(st, old, new):
    i = 0
    while i < len(st):
        st = replace(st, old, new)
        i += 1

    return st
    


print(replaceall("hello this is a hello to you please accept my hello", "hello", "namaste"))

