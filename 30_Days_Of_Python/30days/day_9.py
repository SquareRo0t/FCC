#  Exercises: Day 9
#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# user = int(input("Enter your age: "))
# if user >= 18:
#     print("You are old enough to drive") 
# else:
#     print(f"You need {18 - user} more years to learn to drive")

#2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# my_age = 30
# your_age = int(input("Enter your age: "))

# age_diff = abs(my_age - your_age)

# if your_age > my_age:
#     if age_diff == 1:
#         print("You are one year older than me")
#     else:
#         print(f"You are {age_diff} years older than me.")

# elif your_age < my_age:
#     if age_diff == 1:
#         print("You are one year younger than me")
#     else:
#         print(f"You are {age_diff} years younger than me.")

# else:
#     print("We're the same age!")

#3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# if a > b:
#     print("a is greater than b")
# elif a < b:
#     print("a is smaller than b")
# else:
#     print("a is equal to b")

# Exercises: Level 2
#1 Write a code which gives grade to students according to theirs scores:
# grade = int(input("Enter score to grade: "))

# if grade > 100 or grade < 0:
#     print("Invalid score! Please enter a value between 0 and 100")

# elif grade >= 90:
#     print("A")

# elif grade >= 80:
#     print("B")

# elif grade >= 70:
#     print("C")

# elif grade >= 60:
#     print("D")

# else:
#     print("F")

#2 Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# month = input("Enter the month: ")
# if month.lower() in ["september", "october", "november"]:
#     print("Autumn")

# elif month.lower() in ["december", "january", "february"]:
#     print("Winter")

# elif month.lower() in ["march", "april", "may"]:
#     print("Spring")

# elif month.lower() in ["june", "july", "august"]:
#     print("Summer")

# else:
#     print("Please enter a valid month!")

#3 The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# fruit = input("Enter a fruit to add: ").lower()
# if fruit not in fruits:
#     fruits.append(fruit)
#     print(fruits)
# else:
#     print("That fruit already exist in the list")

# Exercises: Level 3
#1 Here we have a person dictionary. Feel free to modify it! 
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    print("Node")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    if "Python" in person['skills']:
        print("The person has the 'python' skills!")
    else:
        print("The person does not have the 'python' skill")
else:
    print("The person dictionary does not even have a 'skills' key")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if "skills" in person:

    if person['skills'] == ["JavaScript", "React"]:
        print("He is a front end developer")

    elif person['skills'] == ["Node", "Python", "MongoDB"]:
        print("He is a backend developer")

    elif person['skills'] == ["React", "Node", "MongoDB"]:
        print("He is a fullstack developer")

    else:
        print("unknown title")

#  * If the person is married and if he lives in Finland, print the information in the following format:¨
if "is_married" in person and "country" in person:

    if person['is_married'] and person['country'] == "Finland":

        first = person['first_name']
        last = person['last_name']
        country = person['country']

        print(f"{first} {last} live in {country}. He is married")

