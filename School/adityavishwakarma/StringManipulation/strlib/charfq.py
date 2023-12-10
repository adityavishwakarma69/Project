def charFreq(st):
    dt = {}
    for c in st:
        if c not in dt:
            dt[c] = 1
        else:
            dt[c] += 1

    return dt

def wordFreq(st):
    dt = {}
    buffer = ''
    for i in range(len(st)):
        if not (st[i] == ' ' or st[i] == '.' or st[i] == ','):
            buffer += st[i]
        elif buffer != '':
            if not buffer in dt:
                dt[buffer] = 1
            else:
                dt[buffer]  += 1
            buffer = ''

    if not buffer in dt:
        dt[buffer] = 1
    else:
        dt[buffer]  += 1
        
    return dt

def isanagram(st1, st2):
    return charFreq(st1) == charFreq(st2)
