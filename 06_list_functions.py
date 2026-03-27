#1. List Comprehension
#2. map()
#3. filter()
#4. reduce()

# 1. LIST COMPREHENSION
# Q1: Create a list of squares from 1 to 10
squares = [x ** 2 for x in range(1, 11)]
print("Q1 - Squares from 1 to 10:", squares)

# Q2: Extract even numbers from a given list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Q2 - Even numbers:", even_numbers)

# Q3: Convert a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print("Q3 - Uppercase words:", uppercase_words)

# Q4: Flatten a 2D list into a 1D list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened_list = [num for row in matrix for num in row]
print("Q4 - Flattened list:", flattened_list)

# 2. MAP FUNCTION

# Q5: Square all elements in a list using map()
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Q5 - Squared using map:", squared_numbers)

# Q6: Convert a list of strings to integers
string_numbers = ["1", "2", "3"]
integer_numbers = list(map(int, string_numbers))
print("Q6 - Converted to integers:", integer_numbers)

# Q7: Add corresponding elements of two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = list(map(lambda x, y: x + y, list1, list2))
print("Q7 - Element-wise addition:", sum_list)
# 3. FILTER FUNCTION
# Q8: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
filtered_evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Q8 - Filtered even numbers:", filtered_evens)

# Q9: Filter names starting with 'A'
names = ["Alice", "Bob", "Ankit", "John"]
names_starting_with_a = list(filter(lambda name: name.startswith('A'), names))
print("Q9 - Names starting with 'A':", names_starting_with_a)
#4. REDUCE FUNCTION
# Q10: Find the product of all elements in a list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Q10 - Product of elements:", product)
# Q11: Find the maximum element in a list
numbers = [10, 25, 7, 99, 3]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Q11 - Maximum value:", maximum)


# Q12: Get squares of even numbers only
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print("Q12 - Squares of even numbers:", even_squares)


# Q13: Find sum of even numbers using filter() and reduce()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
sum_of_evens = reduce(lambda x, y: x + y, even_numbers)
print("Q13 - Sum of even numbers:", sum_of_evens)


# Q14: Count words with length greater than 3
words = ["hi", "hello", "cat", "python"]
long_words_count = len(list(filter(lambda word: len(word) > 3, words)))
print("Q14 - Count of words with length > 3:", long_words_count)


# Q15: Multiply all odd numbers in a list
numbers = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
product_of_odds = reduce(lambda x, y: x * y, odd_numbers)
print("Q15 - Product of odd numbers:", product_of_odds)
