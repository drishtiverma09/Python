# Q1. Exam Result System
# A school wants to display the result of a student.
# If marks ≥ 40 → Pass
# Else → Fail
# Question:
# Write a Python program to input marks and display the result.

marks=int(input("Enter marks:"))
if marks>=40:
    print("Pass")
else:
    print("Fail")

# Q2. Electricity Bill Discount
# If the total bill amount is more than ₹1000, a discount is given.
# Amount > 1000 → 10% discount
# Otherwise → No discount
# Question:
# Write a Python program to calculate the final bill amount.

amount=int(input("Enter the amount of bill:"))
if amount>1000:
    bill=amount*10/100
else:
    print("NO DISCOUNT")
Total_amount=amount-bill
print("The amount to be paid:",Total_amount)

# Q3. Largest of Three Numbers
# Three numbers are entered by the user.
# Question:
# Write a Python program to find the largest number using nested if.

a=int(input("N1:"))
b=int(input("N2:"))
c=int(input("N3:"))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

# Q4. Login System
# A system checks:
# If the username is correct
# Then checks if the password is correct
# Question:
# Write a Python program to display:
# “Login Successful”
# “Incorrect Password”
# # “Invalid Username”

username=input("Enter the username:")
password=input("Enter passcode :")

u=input("Enter username : ")
p=input("Enter passcode:")

if u==username:
    if p==password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid Username") 

# Q5. Scholarship Eligibility
# A student gets a scholarship if:
# Marks ≥ 85
# If family income < ₹3,00,000 → Eligible
# Else → Not Eligible
# Else → Not Eligible
# Question:
# Write a Python program to check scholarship eligibility using nested if

marks=int(input("Enter the marks:"))
family_income=int(input("Enter the income: "))
if marks>=85:
    if family_income<300000:
        print("Eligible")
    else:
        print("Not eligible")
else:
    print("Not eligible")

# Question6: Smart Login & Access Control System
# A company has a secure system with the following rules:
# The system first checks the username.
# Correct username is admin
# If incorrect → display Invalid Username
# If the username is correct, the system checks the password.
# Correct password is 1234
# If incorrect → display Incorrect Password
# If both username and password are correct, the system checks the role:
# If role is manager
# And experience ≥ 5 years → Full Access Granted
# Else → Limited Access Granted
# If role is employee
# And experience ≥ 2 years → Employee Access Granted
# Else → Trainee Access Granted
# Any other role → Role Not Recognized

username="ID"
password="1234"
u=input("Enter the username: ")
p=input("Enter the password: ")
if username==u:
    if p==password:
        print("Correct")
        role=input("Enter the role: ")
        exp=int(input("Enter the experience: "))
        if role=="manager":
            if exp>=5:
                print("Full access granted ")
            else:
                print("Limited access granted")
        elif role=="employee":
            if exp>=2:
                print("Employee access granted ")
            else:
                print("Limited access granted ")

        else: 
            print("Role not recognised")
    else:
        print("Incorrect passcode")
    
else:
    print("Invalid Username")

#Question 7.A movie is only for people above 18. Ask the user's age and decide if they can watch it.
age = int(input("Enter your age: "))

if age >= 18:
    print("You can watch the movie")
else:
    print("You are not allowed to watch this movie")

# Question9. If the purchase amount is more than ₹1000, give 10% discount.
amount = int(input("Enter shopping amount: "))

if amount > 1000:
    discount = amount * 0.10
    final_price = amount - discount
    print("Discount applied")
    print("Final price:", final_price)
else:
    print("No discount")

#Question10. Discount rules:
# Amount ≥ 5000 → 20% discount
# Amount ≥ 2000 → 10% discount
# Amount ≥ 1000 → 5% discount
# Otherwise → No discount
amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0
final_price = amount - discount
print("Final price:", final_price)

#Question11. Check if the year is leap year or not
year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")

#Question12. Given three sides of a triangle, determine whether it is:
# Equilateral (all sides equal)
# Isosceles (two sides equal)
# Scalene (all sides different)
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

