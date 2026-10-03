#  Exercises: Day 13
# 1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_negative_and_zero = [i for i in numbers if i <= 0]
print(only_negative_and_zero)
print("---------------------------")

# 2 Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in list_of_lists for num in row]
print(flat_list)
print("---------------------------")

# 3 Using list comprehension create the following list of tuples:
tup_num = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(tup_num)
print("---------------------------")

# 4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_count = [[country.upper(), country[:3].upper(), capital.upper()] for i in countries for country, capital in i]
print(new_count)
print("---------------------------")

# 5 Change the following list to a list of dictionaries:
new_dic = [{"country": country.upper(), "city": city.upper()} for i in countries for country, city in i]
print(new_dic)

# 6 Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_list_name = [first + " " + last for i in names for first, last in i]
print(new_list_name)

# 7 Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda y1, slope, x1: y1 - (slope * x1)
print(slope(5, 1, 6, 3))
print(y_intercept(6, 0.75, 5))