with open("test.txt", 'r') as file:
    line = file.readline()
    while line != '':
        print(line.replace(' ', '#'), end = '')
        line = file.readline()
