# Exercises: Day 14
countries1 = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1 Explain the difference between map, filter, and reduce.

# 2 Explain the difference between higher order function, closure and decorator

# 3 Define a call function before map, filter or reduce, see examples.

# 4 Use for loop to print each country in the countries list.
for i in countries1:
    print(i)
print("--------------------------")

# 5 Use for to print each name in the names list.
for ii in names:
    print(ii)
print("--------------------------")

# 6 Use for to print each number in the numbers list.
for iii in numbers:
    print(iii)
print("--------------------------")

# Exercises: Level 2
# 1 Use map to create a new list by changing each country to uppercase in the countries list
def change_to_upper_case(countryy):
    return countryy.upper()
cy = map(change_to_upper_case, countries1)
print(list(cy))
print("--------------------------")

# 2 Use map to create a new list by changing each number to its square in the numbers list
def num_to_square(num):
    return num ** 2
num_square = map(num_to_square, numbers)
print(list(num_square))
print("--------------------------")

# 3 Use map to change each name to uppercase in the names list
def upper_name(name):
    return name.upper()
name_upper = map(upper_name, names)
print(list(name_upper))
print("--------------------------")

# 4 Use filter to filter out countries containing 'land'.
def is_land(land):
    if "land" in land:
        return True
country_land = filter(is_land, countries1)
print(list(country_land))
print("--------------------------")

# 5 Use filter to filter out countries having exactly six characters.
def country_six_char(six_char):
    if len(six_char) == 6:
        return True
six_country_char = filter(country_six_char, countries1)
print(list(six_country_char))
print("--------------------------")

# 6 Use filter to filter out countries containing six letters and more in the country list.
def six_or_more(more):
    if len(more) >= 6:
        return True
    else:
        return False
more_or_six = filter(six_or_more, countries1)
print(list(more_or_six))
print("--------------------------")

# 7 Use filter to filter out countries starting with an 'E'
def start_e(start):
    if "E" in start:
        return True
e_start = filter(start_e, countries1)
print(list(e_start))
print("--------------------------")

# 8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
def upper_name(name):
    return name.upper()
name_upper = map(upper_name, names)

def name_move(name):
    if len(name) >= 4:
        return True
    else:
        return False
move_name = filter(name_move, name_upper)
print(list(move_name))
print("--------------------------")

# 9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
rand_lst = [1, "äpple,", 1,3, "päron", "banan"]
def get_string_lists(parameter):
    if isinstance (parameter, str):
        return True
    else:
        return False
only_str = filter(get_string_lists, rand_lst)
print(list(only_str))
print("--------------------------")

# 10 Use reduce to sum all the numbers in the numbers list.3
from functools import reduce
def sumtot(x, y):
    return int(x) + int(y) 
total = reduce(sumtot, numbers)
print(total)
print("--------------------------")

# 11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def conca_country(x, y):
    return str(x) + ", " + str(y)
country_conc = reduce(conca_country, countries1)
countries2 = country_conc.replace("Norway, Iceland", "Norway, and Iceland")
print(countries2 + " are north European countries")
print("--------------------------")

# 12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from mymodule import countries, countries_data
def categorize_countries(pattern):
    if "land" in pattern or "ia" in pattern or "island" in pattern or "stan" in pattern:
        return True
    else:
        return False
common_pattern = filter(categorize_countries, countries)
print(list(common_pattern))
print("--------------------------")

# 13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def dic_return(country):
    f_letter = {}
    for i in country:
        if i[0] in f_letter:
            f_letter[i[0]] += 1
        else:
            f_letter[i[0]] = 1
    return f_letter
print("--------------------------")

# 14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(first_ten):
    return first_ten[:10]
result = get_string_lists(countries)
print("--------------------------")

# 15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(last_ten):
    return last_ten[-10:]
print("--------------------------")

# Exercises: Level 3
# the tasks below:
# Sort countries by name, by capital, by population

# print(sorted(countries_data, key=lambda x: x["name"]))
# print(sorted(countries_data, key=lambda x: x["capital"]))
# print(sorted(countries_data, key=lambda x: x["population"]))
print("--------------------------")
# Sort out the ten most spoken languages by location.
ten_most = {}

for i in countries_data:
    for j in i["languages"]:
        if j in ten_most:
            ten_most[j] += 1
        else:
            ten_most[j] = 1
sorte = sorted(ten_most.items(), key=lambda x: x[1], reverse=True)
print(sorte[:10])
print("--------------------------")

# Sort out the ten most populated countries.
popu = {}
for i in countries_data:
#   key = landets namn
#   value = landets population
    popu[i["name"]] = i["population"]
    sorted_pops = sorted(popu.items(), key=lambda item: item[1], reverse=True)
print(sorted_pops[:10])
print("--------------------------")