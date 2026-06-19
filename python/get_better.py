# ---------------------------------------------------------

# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero")

# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be less than or equal to zero")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time can't be less than or equal to zero")

# total = principle * pow(1 + rate / 100, time)

# print(f"Balance after {time} year/s €{total:.2f}")

# ---------------------------------------------------------

# timer
# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("Time's up!")

# ---------------------------------------------------------

# Shopping cart program
# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- Your cart -----")

# for food in foods:
#     print(food)

# for price in prices:
#     total += price

# print()
# print(f"You total is: ${total}")

# ---------------------------------------------------------

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


# num_pad = (
#     (1, 2, 3),
#     (4, 5, 6,),
#     (7, 8, 9),
#     ("*", 0, "#"),
# )

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

# ---------------------------------------------------------

# Quiz game
# questions = (("Fråga 1"),
#              ("Fråga 2"),
#              ("Fråga 3"),
#              ("Fråga 4"),
#              ("Fråga 5"))

# options = (("a", "b", "c", "d"),
#            ("1", "1", "2", "3"),
#            ("2", "1", "2", "3"),
#            ("3", "1", "2", "3"),
#            ("4", "1", "2", "3"))

# answers = ("a", "1", "2", "3", "4")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("--------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter (1, 2, 3, 4) ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("Correct")
#     else:
#         print("incorrect")
#         print(f"{answers[question_num]} is the correct answer")

#     question_num += 1

# print("--------------------------")
# print("         Result           ")
# print("--------------------------")

# print("answers:", end=" ")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses:", end=" ")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")

# ---------------------------------------------------------

# capitals = {
#     "USA": "Washington D.C.",
#     "India": "New Delhi",
#     "China": "Beijing",
#     "Russia": "Moscow",
# }

# print(capitals.get("USA"))

# if capitals.get("Japan"):
#     print("That capital exist")
# else:
#     print()

# capitals.update({"Germany": "Berlin"})
# print(capitals)

# ---------------------------------------------------------

# Concession stand program
# menu = {
#     "pizza": 3.00,
#     "nachos": 4.50,
#     "popcorn": 6.00,
#     "fries": 2.50,
#     "chips": 1.00,
#     "pretzel": 3.50,
#     "soda": 3.00,
#     "lemonade": 4.25,
# }

# cart = []
# total = 0

# print("-------------MENY--------------")
# for key, value in menu.items():
#     print(f"{key:10}: €{value:.2f}")
# print("-------------------------------")

# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total is: €{total:2f}")

# ---------------------------------------------------------

# Python number guessing game
# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:
#     guess = input("Enter you guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again!")
#         else:
#             print(f"Correct! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")

# ---------------------------------------------------------
# import random

# options = ("rock", "paper", "scissors")
# running = True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")

#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False

# print("Thanks for playing!")
# ---------------------------------------------------------

# import random

# ● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),

#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
    
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),

#     4: ("┌─────────┐",
#         "│ ●     ● │",
#         "│         │",
#         "│ ●     ● │",
#         "└─────────┘"),
    
#     5: ("┌─────────┐",
#         "│ ●     ● │",
#         "│    ●    │",
#         "│ ●     ● │",
#         "└─────────┘"),
    
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice? "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end=" ")
#     print()

# for die in dice:
#     total += die
# print(f"Total: {total}")
# ---------------------------------------------------------

# def display_invoice(username, amount, due_data):
#     print(f"Hello {username}")
#     print(f"Your bill of €{amount:.2f} is due {due_data}")

# display_invoice("Chicken", 40, "02/03")

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)


# import time

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")

# count(30, 15)

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=46, area=123, first=456, last=789)
# print(phone_num)

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# def print_adress(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_adress(street="123 hahga", apt="1", city= "älv" , state= "ÄL", zip="123456")

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()

#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     else:
#          print(f"{kwargs.get('street')}")
#     print(f"{kwargs.get('city')} {kwargs.get('zip')}")

# shipping_label("Mr", "Sherlock", "Holmes", "Legend",
#                street="123 brit", apt="2", city="Lond", zip="2344" )