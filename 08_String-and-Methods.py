# Reverse a given string 
string = input("Enter string: ")
print(string[::-1])

#Write a program to count number of vowels in a string
string = input("Enter string: ")
count = 0
for ch in string.lower():
    if ch in "aeiou":
        count += 1
print(count)

# Check if the string is a pallindrome or not
string = input("Enter string: ")
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
  #Count number of words in a string
string = input("Enter sentence: ")
print(len(string.split()))

#Replace a with e in the string
string = input()
print(string.replace("a", "e"))

#Check if the string ends with the input given by user
x = input()
print(x.endswith("ing"))

#Write a program to count uppercase letters, lowercase letters, and digits in a string
string = input("Enter string: ")
upper = 0
lower = 0 
digit = 0
for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)

#Check whether a string contains only alphabets
string = input("Enter string: ")
if string.isalpha():
    print("Only alphabets")
else:
    print("Contains other characters")
  #Remove duplicate words from a sentence
sentence = input("Enter sentence: ")
words = sentence.split()
result = []
for word in words:
    if word not in result:
        result.append(word)
print(" ".join(result))

#Reverse each word in sentence
sentence = input("Enter sentence: ")
words = sentence.split()
result = []
for word in words:
    result.append(word[::-1])
print(" ".join(result))


