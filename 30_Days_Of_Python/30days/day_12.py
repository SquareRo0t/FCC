# Exercises: Day 12
# Exercises: Level 1
# 1 Write a function which generates a six digit/character random_user_id.
import string
from random import choice, random , randint
import random

def random_user_int():
   random_ord = string.ascii_letters + string.digits
   ord = ""
   for i in range(1, 7):
      spara = choice(random_ord)
      ord += spara
   return ord

print("-------------------------------------")
# 2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
   user1 = int(input("Enter number of characters: "))
   user2 = int(input("Enter number of IDs: "))
   random_ord = string.ascii_letters + string.digits
   print("-------------------------------------")
   alla_id = ""

   for i in range(1, user2 + 1):
      u_ord = ""
      for j in range(1, user1 + 1):
        spara = choice(random_ord)
        u_ord += spara
      alla_id += u_ord +"\n"
   return alla_id.rstrip("\n")

# print(user_id_gen_by_user())

print("-------------------------------------")
# 3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
   slumptal1 = randint(0, 255)
   slumptal2 = randint(0, 255)
   slumptal3 = randint(0, 255)
   return f"rgb({slumptal1}, {slumptal2}, {slumptal3})"
print(rgb_color_gen())
print("-------------------------------------")

# Exercises: Level 2
# 1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(antal):
   tecken = "0123456789abcdef"
   hexa_lst = []
   
   for i in range(antal):
      sexahexa = ""
      for j in range(6):
         sexahexa += choice(tecken)
      sexahexa = "#" + sexahexa 
      hexa_lst.append(sexahexa)
         
   return hexa_lst
# print(list_of_hexa_colors(3))

print("-------------------------------------")
# 2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(rgb_any):
   rgb_lst = []

   for i in range(rgb_any):
      r = randint(0, 255)
      g = randint(0, 255)
      b = randint(0, 255)

      rgb_lst.append(f"rgb({r}, {g}, {b})")
      
   return rgb_lst
# print(list_of_rgb_colors(3))
print("-------------------------------------")

# 3 Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, number):
   if color_type == "rgb":
      print(list_of_rgb_colors(number))
   elif color_type == "hexa":
      print(list_of_hexa_colors(number))
   else:
      print("Please insert rgb or hexa")
(generate_colors('rgb', 3))

print("-------------------------------------")
# Exercises: Level 3
# 1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
   random.shuffle(lst)
   return lst
print(shuffle_list(["apple", "banana", "cherry", "pineapple"]))

print("-------------------------------------")
# 2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random_numbers():
   number = []
   i = 0
   while i < 7 :
      num = randint(0, 9)
      if num not in number:
         number.append(num)
         i += 1
   return number
print(seven_random_numbers())
