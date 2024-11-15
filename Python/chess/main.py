board = [
    ['br', 'bk', 'bb', 'bq', 'bc', 'bb', 'bk', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['na', 'na', 'na', 'na', 'na', 'na', 'na', 'na'],
    ['na', 'na', 'na', 'na', 'na', 'na', 'na', 'na'],
    ['na', 'na', 'na', 'na', 'na', 'na', 'na', 'na'],
    ['na', 'na', 'na', 'na', 'na', 'na', 'na', 'na'],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wr', 'wk', 'wb', 'wq', 'wc', 'wb', 'wk', 'wr']]


n = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6 , "h" : 7}

while True:
    fr = input("enter move")
    to = input("enter move")
    try :
        fr = (8 - int(fr[1]), n[fr[0]])
        to = (8 - int(to[1]), n[to[0]])
    except :
        print("invalid move")
        continue
    board[to[0]][to[1]] = board[fr[0]][fr[1]]
    board[fr[0]][fr[1]] = 'na'
    print(to, fr)
    for r in board:
        print (r)
