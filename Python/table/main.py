def bubbleSort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if int(l[j][1]) > int(l[j + 1][1]):
                l[j], l[j+ 1] = l[j + 1], l[j]



import csv

fileobject = open("test.csv", 'r')

reader = csv.reader(fileobject)

data = []

for line in reader:
    data.append(line)

fileobject.close()
bubbleSort(data)

fileobject = open("ranking.csv", 'w')
writer = csv.writer(fileobject)
print(*data, sep = '\n')

for i in range(len(data)):
    row = data[len(data) - 1 - i]
    row.insert(0, i + 1)
    writer.writerow(row)
fileobject.close()

