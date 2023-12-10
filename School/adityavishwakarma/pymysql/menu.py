import mysql.connector as con
import csv

connection = con.connect(host = 'localhost', user = 'root', passwd = 'india', database = 'aditya')

cursor = connection.cursor()

if connection.is_connected():
	print("Connected successfully")
else:
	exit()

while 1:
	print('''
_____________________
| 1. Display Record |
| 2. Insert Record  |
| 3. Delete Record  |
| 4. Search Record  |
| 5. Update Record  |
| 6. Flush Contents |
| 7. Export to csv  |
| 8. Exit           |
|___________________|''')       
	opt = int(input("Enter Option >> "))

	match opt:
		case 1:
			cursor.execute("select * from student")
			data = cursor.fetchall()
			print("__________________________________________\n")
			for r in data:
				for j in r:
					print(j, end = "  ")
				print()
			print("___________________________________________")

		case 2:
			print("Enter record to insert ")
			print("__________________________________________\n")
			sid = int(input("Enter Student ID >> "))
			sname = input("Enter Student Name >> ")
			sdob = input("Enter Student Dob(YYYY-MM-DD) >> ")
			spn = int(input("Enter Student phone >> "))
			sh = input("Enter Student House >> ")[0]
			cursor.execute(f"insert into student values({sid}, \'{sname}\', \"{sdob}\", {spn}, \'{sh}\')")

		case 3:
			sid = int(input("Enter the sid of the record >> "))
			cursor.execute(f"delete from student where std_id = {sid}")
			if cursor.rowcount == 0:
				print("Row not found")
			else:
				print("Row successfully Deleted")

		case 4:
			op = int(input('''1. Search by name
2. Search by id
option >> '''))
			match op:
				case 1:
					sname = input("Enter name >> ").strip()
					cursor.execute(f"select * from student where std_name = \'{sname}\'")
					data = cursor.fetchall()
					print("___________________________________________\n")
					for r in data:
						for j in r:
							print(j, end = "  ")
						print()
					print("___________________________________________")
				case 2:
					sid = int(input("Enter id >> "))
					cursor.execute(f"select * from student where std_id = {sid}")
					data = cursor.fetchall()
					print("___________________________________________\n")
					for r in data:
						for j in r:
							print(j, end = "  ")
						print()
					print("___________________________________________")

		case 5:
			sid = int(input("Enter Student ID >> "))
			sname = input("Enter Student Name >> ")
			sdob = input("Enter Student Dob(YYYY-MM-DD) >> ")
			spn = int(input("Enter Student phone >> "))
			sh = input("Enter Student House >> ")[0]
			cursor.execute(f"update student set std_name = \'{sname}\', std_dob = \'{sdob}\', std_phone = {spn}, std_house = \'{sh}\' where std_id = {sid}")

		case 6:
			cursor.execute("flush table student")
		case 7:
			filename = input("enter name of file")
			with open(filename, 'w') as fileobj:
				reader = fileobj.reader()
				cursor.execute("select * from student")
				data = cursor.fetchall()

		case 8:
			exit()

		case _:
			print("Option not found")
cursor.close()