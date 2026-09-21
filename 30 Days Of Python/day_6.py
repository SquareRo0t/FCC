# Exercises: Level 1
#1 Create an empty tuple
my_tuple = ()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers_tuple = ("Albert", "Ben", "Chris")
sisters_tuple = ("Anna", "Bea", "Christine")

#3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers_tuple + sisters_tuple

#4 How many siblings do you have?
print(len(siblings))

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Mit sätt
# siblings = list(siblings)
# siblings.append("Dork")
# siblings.append("Denise")
# family_members = tuple(siblings)
# print(family_members)

# Enklare sätt
family_members = siblings + ("Dork", "Denise")
# print(family_members)

# Exercises: Level 2
#1 Unpack siblings and parents from family_members
br1, br2, br3, sis1, sis2, sis3, fa, mo = family_members

#2 Create fruits, vegetables and animal products tuples. Join the three 
# tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "clementine")
vegetables = ("sallad", "carrot", "beetroot")
animal_product = ("milk", "egg", "butter")
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[3:6])

#5 Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[6:9])

#6 Delete the food_stuff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
# print(food_stuff_tp)


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)

# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)