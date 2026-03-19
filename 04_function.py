# Q1.print 'Hello World!'
def greeting():
    print("Hello world!")
greeting()

#Q2.Greet a user by his/her name
def greeting(name):
    print(f"Greetings,{name}!")
greeting('dhvani')

#Q3. Add two numbers 
def add(a,b):
    print('Sum of two numbers: ',a+b)
add(4,6)

#Q4.Square of number 
def square(a):
    print('Square of number : ',a*a)
square(5)

#Q5.Check if number is odd or even
def check_number(a):
    if a%2==0:
        print("Number is even!")
    else:
        print("Number is odd!")
check_number(8)
check_number(1)

#Q6.Print numbers from 1 to 20
def list():
    for i in range (1,21):
        print(i)
list()
        
#Q7.Multiplication table for a number
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
multiplication_table(2)
#Q8. Factorial of a number 

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

# #Q9.Reverse a string
def reverse_string(n):
    print(n[::-1])
reverse_string('Hello')

#Q10.Average of 3 numbers
def average(a,b,c):
    avg=a+b+c/3
    print(avg)
average(3,6,9)

#Q11. Function to check if a number is positive, negative, or zero
def check_number(n):
    if n>0:
        print("Number is positive")
    elif n<0:
        print("Number is negative")
    else:
        print("Number is zero")
check_number(-1)
check_number(8)

#Q12. Sum of a list
def sum_list(lst):
    print("Sum of Numbers in the list: ",sum(lst))
sum_list([1,2,3])

#Q13.Maximum number in a list
def max_number(lst):
    print("Maximum number in the list is :" ,max(lst))
max_number([3,5,6,7])

#Q14. Count number of vowels in string
def count_vowels(string):
    vowels='aeiouAEIOU'
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
print(count_vowels('Hello World'))

#Q15. Check if string is palindrome
def check_palindrome(string):
    return(string==string[::-1])
print(check_palindrome("wow"))
print(check_palindrome("hello"))   

#Q16. Count the  length of a list without using len()
def length_string(string):
    count=0
    for char in string:
        count+=1
    return count
print(length_string("HELLO WORLD"))

#Q17.Remove duplicates from a list
def remove_duplicate(lst):
    return(list(set(lst)))
print(remove_duplicate([1,3,5,3,1,4,7]))

#Q18.Count words in a sentence
def count_words(string):
    words=string.split()
    return len(words)
print(count_words("Python is easy language"))
    
    

        
