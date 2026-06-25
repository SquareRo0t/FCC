# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from class

class Student:

    class_year = 2020
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("John", 1)
student2 = Student("Doe", 2)
student3 = Student("Hill", 3)

print(student1.name)
print(student1.age)
print(Student.class_year)

print()

print(student2.name)
print(student2.age)
print(Student.class_year)

print()

print(Student.num_students)

print()

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)

