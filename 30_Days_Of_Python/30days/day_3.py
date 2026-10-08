age = 30
height = 175.0
is_complex = 4 - 4j

# base_triangle = int(input("Enter base: "))
# height_triangle = int(input("Enter height: "))
# area = 0.5 * base_triangle * height_triangle
# print("the area of the triangle is", area)

# side_a = int(input("Enter side a "))
# side_b = int(input("Enter side b "))
# side_c = int(input("Enter side c "))
# perimeter = side_a + side_b + side_c
# print("The perimeter of the triangle is", perimeter)

# length_rectangle = int(input("Enter lenght: "))
# width_rectangle = int(input("Enter width: "))
# area = length_rectangle * width_rectangle
# perimeter = 2 * (length_rectangle + width_rectangle)

# print("The area of the rectangle is", area)
# print("The perimeter of the rectangle is", perimeter)

# radius = float(input("Enter the radius: "))
# pi = 3.14
# circle_area = pi * radius * radius
# circumference = 2 * pi * radius
# print("The area of the circle is", circle_area)
# print("The circumference of the cirlce is", circumference)

# y = "2x - 2"  -> x = 0 ger y = -2 -> (0, -2)
#                  y = 0 ger x =  1 -> (1,  0) y = mx + b 

# m = y2-y2/x2-x1
import math
y2, y1, x2, x1 = 10, 2, 6, 2
y_tot = y2 - y1
x_tot = x2 - x1
m = (y2 - y1) / (x2 - x1)
euclidean_distance = math.sqrt(y_tot**2 + x_tot**2)
# print(m)
# print(euclidean_distance)

# y = x^2 + 6x + 9
x = -3
y = x ** 2 + 6 * x + 9
# print(y)

# print(len("python"))
# print(len("dragon"))
# print(len("python") > len("dragon"))

# print("on" in "python" and "on" in "dragon")
# print("on" not in "python" and "on" not in "dragon")

# print("jargon" in "I hope this course is not full of jargon")

# print(len("python"))
python_length = len("python")
python_float = float(python_length)
python_string = str(python_float)
# print(python_string)

# OM Tal % 2 == 0
tal = 4 % 2
# print(tal)

tal2 = 7 // 3
# print(tal2 == int(2.7))
# print("10" == 10)
# print(int("9.8") == 10)

# hours = int(input("Enter hours: "))
# rate_per_hour = int(input("Enter rate per hour: "))
# salay = hours * rate_per_hour
# print("Your weekly earning is", salay)

# years = int(input("Enter number of years you have lived: "))
# seconds_tot = years * 365 * 24 * 60 * 60
# print("You have lived for", seconds_tot, "seconds")

print("1", "1", "1", "1", "1")
print("2", "1", "2", "4", "8")
print("3", "1", "3", "9", "27")
print("4", "1", "4", "16", "64")
print("5", "1", "5", "25", "125")
