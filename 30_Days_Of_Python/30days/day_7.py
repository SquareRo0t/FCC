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
# allt från A + B
C_join = A.union(B)
print(C_join)

#2 Find A intersection B
# det som finns i båda
C_intersec = A.intersection(B)
print(C_intersec)

#3 Is A subset of B, Subset — delmängd
# Om alla element i A finns i B 
# A är en del av B → A är subset av B.
# är A helt inuti B?
C_subset = A.issubset(B)
print(C_subset)
 
#4 Are A and B disjoint sets, Superset — övermängd
# Disjoint betyder att A och B inte har några gemensamma element.
# har A och B inget gemensamt?
C_disjoint = A.isdisjoint(B)
print(C_disjoint)

#5 Join A with B and B with A
CAB = A.union(B)
CBA = B.union(A)
print(CAB)
print(CBA)

#6 What is the symmetric difference between A and B
#  27 och 28
C_symmetric = A.symmetric_difference(B)
print(C_symmetric)

#7 Delete the sets completely
del A
del B

# Exercises: Level 3
#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age)) # Denna är större dvs listan pga dubbletter
print(len(age_set))

#2 Explain the difference between the following data types: 
# string - är en text som består av en följd tecken, tex bokstäver, siffror eller symboler, omgiven av enkla eller dubbla citattecken
# list - en variabel som kan lagra flera värden samtidigt
# tuple - är en ordnad samling data som inte kan ändras efter att den har skapats
# set - är en inbyggd datatyp som lagrar en osorterad samling av unika element

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
# 10 unika ord
text = "I am a teacher and I love to inspire and teach people"
words = text.split()
print(words)

words_list = set(words)
print(words_list) 