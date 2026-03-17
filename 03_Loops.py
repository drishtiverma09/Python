#Write a program to print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print(i)
#Write a program to print all even numbers between 1 and 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
#Write a program to print the multiplication table of a number entered by the user.
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#Write a program to reverse a number using a while loop.
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)
#Write a program to print the following pattern.
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)
#Write a program to check if number is prime or not
num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
#Write a program to find factorial of a number
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i
print("Factorial =", factorial)
#Write a program to print the Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
#Write a program to calculate the sum of digits of a number entered by the user.
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits:", sum_digits)
#Write a program to check whether a number is an Armstrong number.
num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
#Write a program to count the number of vowels in a string
text = input("Enter a string: ")
count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)
#Create a number guessing game where the user keeps guessing until they find the correct number.
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct guess!")
    else:
        print("Try again")
#Write a program to print the following pattern.

#     *
#    ***
#   *****
#  *******
# *********

rows = 5

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
#Write a program to reverse a string using a loop.
string = input("Enter a string: ")
reverse = ""

for char in string:
    reverse = char + reverse

print("Reversed string:", reverse)
#Write a program to print all prime numbers between 1 and 50.
for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
    
