# Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["X", "Tesla", "Chatgpt"])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("X")
print(it_companies)

# What is the difference between remove and discard
# Skillnaden är att remove() kommer visa ett felmeddelande i terminalen medan discard() inte kommer att göra det

# Exercises: Level 2
#1 Join A and B
#2 Find A intersection B
#3 Is A subset of B
#4 Are A and B disjoint sets
#5 Join A with B and B with A
#6 What is the symmetric difference between A and B
#7 Delete the sets completely