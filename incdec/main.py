from random import randint

def newkey():
    exc = []
    key = ""
    for _ in range(128):
        temp = randint(0, 127)
        while temp in exc:
            temp = randint(0, 127)
        key = key + chr(temp)
        exc.append(temp)
    return key

def valueof(c, key):
    for i in range(len(key)):
        if key[i] == c:
            return chr(i)
        
def incrypt(filename, key):
    file = open(filename, 'r')
    data = file.read()
    file.close()

    file = open(f"inc_{filename}", 'w')
    coded = ""
    for c in data:
        coded = coded + key[ord(c)]
    
    file.write(coded)
    file.close()

def decrypt(filename, key):
    file = open(filename, 'r')
    data = file.read()
    file.close()

    decoded = ""
    for c in data:
        decoded = decoded + valueof(c, key)
    return decoded

def keyfromfile(filename):
    newkey = (file := open(filename, 'r')).read();file.close()
    return newkey

def keytofile(filename, key):
    (file := open(filename, 'w')).write(key);file.close()

key = keyfromfile("key.txt")
print(decrypt("inc_data.txt", key))