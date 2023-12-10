def matInput():
	rows = int(input("Enter the number of rows : "))
	cols = int(input("Enter the number of columns : "))
	mat = []
	for r in range(rows):
		mat.append(list())
		for c in range(cols):
			mat[r].append(float(input(f"Enter the Value of A{r + 1}{c + 1} : ")))

	return mat

def matMul(mat1, mat2):
	if len(mat1[0]) != len(mat2):
		print("can't multiply : ")
		return
	mat = []
	for i in range(len(mat1)):
		mat.append(list())
		for j in range(len(mat2[0])):
			elm = 0
			for k in range(len(mat1[0])):
				elm += mat1[i][k] * mat2[k][j]
			mat[i].append(elm)

	return mat

def printMat(mat):
	for r in mat:
		for e in r:
			print(e, end = ' ')
		print()

print("Enter Values in MATRIX 1")
mat1 = matInput()
print("Enter Values in MATRIX 1")
mat2 = matInput()
printMat(matMul(mat1, mat2))
