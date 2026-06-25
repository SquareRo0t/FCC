# ---------------------------------------------------------

# List comprehension

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
fruits_chars = [fruit[0] for fruit in fruits]

print(fruits_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]

print(odd_numbers)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)

# ---------------------------------------------------------