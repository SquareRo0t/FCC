# Exercises: Day 8
#1 Create an empty dictionary called dog
#2 Add name, color, breed, legs, age to the dog dictionary
dog = {"name" : "Bob",
       "color": "grey",
       "breed": "golden_retriever",
       "legs" : 4,
       "age"  : 1
       }
# print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name": "James",
           "last_name": "Bond",
           "gender": "Male",
           "age": 18,
           "marital_status": False,
           "skills":['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
           "country": "America",
           "city": "New York",
           "address":{"Street": "Space street", "zipcode": "11111"}
           }

#4 Get the length of the student dictionary 
print(len(student)) # 9

#5 Get the value of skills and check the data type, it should be a list
# print(type(student.get("skills")))

#6 Modify the skills values by adding one or two skills
student["skills"].append("C")
student["skills"].append("Html")
# print(student)

#7 Get the dictionary keys as a list
# print(student.keys())

#8 Get the dictionary values as a list
# print(student.values())

#9 Change the dictionary to a list of tuples using items() method
# print(student.items())

#10 Delete one of the items in the dictionary
del student["first_name"]

#11 Delete one of the dictionaries
del dog