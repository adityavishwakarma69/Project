import pickle

file = open("hello", 'wb')
t1 = "hello"
t2 = 1231
t3 = ["1", 2, {"h" : 10}]

pickle.dump(t1, file)
pickle.dump(t2, file)
pickle.dump(t3, file)

file.close()

file = open("hello", 'rb')

for i in range(4):
    print(pickle.load(file))

file.close()
