import mysql.connector as mscn

con = mscn.connect(host = 'localhost', user = 'root', passwd = 'india', database = 'aditya')
cur = con.cursor()

if con.is_connected():
    print("connected ╰*°▽°*╯")
else:
    raise Exception("failed")

while True:
    print("1. Display Record")
    print("2. Insert Record")
    print("3. Delete Record")
    print("4. Search Record")
    print("5. Exit")
    opt = int(input(">>>"))

    match opt:
        case 1:
            cur.execute("select * from employee")
            for i in cur:
                print(i)
