# Create a tuple and print its first and last element
tup = (10, 20, 30, 40, 50)
print("First:", tup[0])
print("Last:", tup[-1])

#Count how many times an element appears in a tuple
tup = (1, 2, 3, 2, 4, 2)
print(tup.count(2))

#Find the index of a given element in a tuple
tup = (10, 20, 30, 40)
print(tup.index(30))

#Convert list into tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)

#Find max and min element in a tuple
tup = (4, 7, 1, 9, 2)
print("Max:", max(tup))
print("Min:", min(tup))

#Remove duplicate elements from a tuple
t = (1, 2, 2, 3, 4, 4)
unique = tuple(set(t))
print(unique)

#Create a set and print it
s = {1, 2, 3, 4}
print(s)

#Add an element to a set
s = {1, 2, 3}
s.add(4)
print(s)
#Remove an element from a set.
s = {1, 2, 3}
s.remove(2)
print(s)
#Find Union of two sets
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
print(set_1.union(set_2))
#Find interesection between two sets
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
print(set_1.intersection(set_2))

#Find elements in set A but not in B
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
print(set_1.difference(set_2))

#Find elements present in either set but not both
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
print(set_1.symmetric_difference(set_2))

#Check if one set is subset of another
set_1 = {1, 2}
set_2 = {1, 2, 3, 4}
print(set_1.issubset(set_2))

#Create a program that:

# Takes a paragraph as input
# Counts:
# total words
# unique words
# most frequent word
# vowels count
# Displays results

text = input("Enter paragraph:")
words = text.lower().split()
total_words = len(words)
unique_words = len(set(words))
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
most_freq = max(freq, key=freq.get)
vowels = sum(1 for ch in text.lower() if ch in "aeiou")

print("Total words:", total_words)
print("Unique words:", unique_words)
print("Most frequent word:", most_freq)
print("Vowel count:", vowels)

#Create a system where:
# Store student data as tuples: (name, marks)
# Find:
# highest scorer
# lowest scorer
# average marks
# unique marks

students = [
    ("Aman", 85),
    ("Riya", 90),
    ("Karan", 85),
    ("Neha", 95),
    ("Simran", 90)
]
highest = max(students, key=lambda x: x[1])
lowest = min(students, key=lambda x: x[1])
total = sum([s[1] for s in students])
avg = total / len(students)
unique_marks = set([s[1] for s in students])

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", avg)
print("Unique Marks:", unique_marks)

