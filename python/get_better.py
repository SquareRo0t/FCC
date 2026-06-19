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


# Quiz game
# questions = (("1"), 
#              ("2"), 
#              ("3"), 
#              ("4"), 
#              ("5"))

# options = (("1", "2", "3", "4", "5"), 
#            ("2", "2", "3", "4", "5"), 
#            ("3", "2", "3", "4", "5"), 
#            ("4", "2", "3", "4", "5"), 
#            ("5", "2", "3", "4", "5"))

# answers = ("1", "2", "3", "4", "5")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("--------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter (1, 2, 3, 4, 5) ").upper()
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