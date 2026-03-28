# Q1. Write a Python program to create a 3×3 2D list with values from 1 to 9 and print it in matrix form.
x=int(input("Enter the number of rows:"))
y=int(input("Enter number of columns :"))
matrix=[]
for i in range(x):
    row=[]
    for j in range(y):
        elements=int(input(f"Enter value of elements: [{i}{j}]" ))
        row.append(elements)
    matrix.append(row)
print(matrix)


# Q2. Write a Python program to print the element at row 2, column 3 of a 2D list.
x=int(input("Enter the number of rows:"))
y=int(input("Enter number of columns:"))
matrix=[]
for i in range(x):
    row=[]
    for j in range(y):
        value=int(input(f"Enter the value : [{i}{j}]"))
        row.append(value)
    matrix.append(row)
result=matrix[1][2]
print("Element at [2][3]:", result)


# Q3. Write a Python program to find and print the transpose of a given 2D list.
rows=int(input("Enter number of rows:"))
column=int(input("enter no. columns:"))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(column):
        value=int(input("Enter value of elements:"))
        row.append(value)
    matrix.append(row)
print(matrix)
transpose = []
for i in range(y):
    row = []
    for j in range(x):
        row.append(matrix[j][i])
    transpose.append(row)
print("Transpose:", transpose)


# Q4. Write a Python program to create a jagged array and print the length of each row.
[1]
[2, 3]
[4, 5, 6]
x=int(input("Enter number of rows:"))
matrix=[]
for i in range(x):
    y=int(input("Enter number of columns:"))
    row=[]
    for j in range(y):
        value=int(input("Enter values: "))
        row.append(value)
    matrix.append(row)
print(matrix)
list=[]
for row in matrix:
    item=len(row)
    list.append(item)
print(list)


# Q5. Write a Python program to add two 2D lists (matrices) of the same size.
x=int(input("Enter number of rows :"))
y=int(input("Enter number of columns:"))

m1=[]
for i in range(x):
    row=[]
    for j in range(y):
        value=int(input(f"Enter the value :[{i}{j}]"))
        row.append(value)
    m1.append(row)

m2=[]
for i in range(x):
    row=[]
    for j in range(y):
        val=int(input(f"Enter the value: [{i}{j}]"))
        row.append(val)
    m2.append(row)

result=[]
for i in range(x):
    row=[]
    for j in range(y):
        value=m1[i][j]+m2[i][j]
        row.append(value)
    result.append(row)
print(result)


# Q6. Write a Python program to create an identity matrix of size n × n.
x=int(input("Enter number of rows :"))
y=int(input("Enter number of columns:"))
identity=[]
for i in range(x):
    row=[]
    for j in range(y):
        if i==j:
            row.append(1)
        else:
            row.append(0)
    identity.append(row)
print(identity)


# Q7. Write a Python program to rotate a matrix by 90 degrees clockwise.
x=int(input("Enter number of rows :"))
y=int(input("Enter number of columns:"))
matrix=[]
for i in range(x):
    row=[]
    for j in range(y):
        val=int(input("Enter the value:"))
        row.append(val)
    matrix.append(row)

list1=[]
for i in range(y):
    row=[]
    for j in range(x):
        row.append(matrix[j][i])
    list1.append(row)

l2=[]
for row in list1:
    l2.append(row[::-1])
print(l2)


# Q8. Write a Python program to find the inverse of a 2×2 matrix.
# matrix=[]
for i in range(2):
    row=[]
    for j in range(2):
        val=float(input(f"Enter the value [{i+1}{j+1}]:"))
        row.append(val)
    matrix.append(row)

a=matrix[0][0]
b=matrix[0][1]
c=matrix[1][0]
d=matrix[1][1]

det=a*d-b*c
if det==0:
    print("Determinant does not exist.")
else:
    inv=[
        [round(d/det, 2), round(-b/det, 2)],
        [round(-c/det, 2), round(a/det, 2)]
    ]
    print("inverse of matrix :")
    print(inv)


# Q9. Write a Python program to find the maximum value in a 2D list.
x=int(input("Enter no. of rows:"))
y=int(input("Enter no. of columns:"))
matrix=[]
for i in range(x):
    row=[]
    for j in range(y):
        val=int(input(f"Enter value of elements - [{i}{j}] :"))
        row.append(val)
    matrix.append(row)
max_val=max(max(row) for row in matrix)
print("Maximum value:",max_val)


# Q10. Write a Python program to extract all even numbers from a 2D list.
x=int(input("Enter no. of rows:"))
y=int(input("Enter no. of columns:"))
matrix=[]
for i in range(x):
    row=[]
    for j in range(y):
        val=int(input(f"Enter value of elements - [{i}{j}] :"))
        row.append(val)
    matrix.append(row)
even_num= [num for row in matrix for num in row if num%2==0]
print(even_num)


# Q11. Write a Python program to create a 2D list and print the element at row 2 and column 3.
n=int(input("Enter number of rows :"))
c=int(input(("Enter number of columns:")))
mat=[]
for i in range(n):
    rows=[]
    for j in range(c):
        value=int(input(f"Enter value of elements[:{i}{j}]"))
        rows.append(value)
    mat.append(rows)
print(mat[1][2])
