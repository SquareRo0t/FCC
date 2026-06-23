# object = A "bundle" of related attributes (variables) and methods (functions)
# Ex. phone, cup, book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

from car import Car

car1 = Car("Mustang", 2026, "blue", False)
car2 = Car("BWM", 2025, "SILVER", True)
car3 = Car("Volo", 2020, "Red", True)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)
# print()
# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)

car1.drive()
car2.stop()
car1.describe()