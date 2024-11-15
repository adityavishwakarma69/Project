def replaceall(st, old, new):
    i = 0
    while i < len(st):
        if st[i:i + len(old)] == old:
            st = st[:i] + new + st[i + len(old):]
        i += 1

    return st


def replaceallwords(st, old, new):
    i = 0
    while i < len(st):
        if st[i:i + len(old)] == old:
            if (i == 0 and st[i + len(old)] == ' ') or (i + len(old) == len(st) and st[i - 1] == ' '):
                st = st[:i] + new + st[i + len(old):]
            elif st[i + len(old)] == ' ' and st[i - 1] == ' ':
                st = st[:i] + new + st[i + len(old):]
        i += 1

    return st


new = replaceallwords(
    old := "ram ramesh ramakant ramnath rameshwar ram ji", "ram", 'krishna')
print(old, new, sep="\n")
