#Take a list of names and print each name in uppercase.
names=["french","english","spanish","hindi"]
for name in names:
    print(name.upper())
#Create a list and print only elements greater than 10.
number=[1,34,5,6,11,23,55]
for num in number:
    if num>10:
        print(num)
#Add an element to a list and then remove one element
lst=[1,2,3,4,5,6]
lst.append(0)
lst.remove(3)
print(lst)
#Print the first and last element of a list
lst=[1,2,3,4,5]
print(lst[0])
print(lst[-1])
#Sort a list in ascending order
num=[2,5,1,9,7]
num.sort()
print(num)
#Create a new list containing squares of another list
lst=[1,4,5,2]
squares=[]
for num in lst:
    print(num)
    num=num*num
    squares.append(num)
print(squares)
#Reverse a list without using .reverse().
lst=[1,2,3,4]
print(lst[::-1])
#Sort a list in descending order
lst=[1,4,7,2,9]
lst.sort(reverse=True)
print(lst)
#Check if a given element exists in a list
nums=[1,2,3,4,5]
print(3 in nums)
print(9 in nums)

#Given a list, print only elements at even indices.
lst=[1,2,3,4,5,6]
for i in range (len(lst)):
    if i%2==0:
        print(lst[i])
