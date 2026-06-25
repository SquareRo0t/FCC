# ---------------------------------------------------------

# Shopping cart program
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your cart -----")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"You total is: ${total}")

# ---------------------------------------------------------

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()


num_pad = (
    (1, 2, 3),
    (4, 5, 6,),
    (7, 8, 9),
    ("*", 0, "#"),
)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# ---------------------------------------------------------

# Quiz game
questions = (("Fråga 1"),
             ("Fråga 2"),
             ("Fråga 3"),
             ("Fråga 4"),
             ("Fråga 5"))

options = (("a", "b", "c", "d"),
           ("1", "1", "2", "3"),
           ("2", "1", "2", "3"),
           ("3", "1", "2", "3"),
           ("4", "1", "2", "3"))

answers = ("a", "1", "2", "3", "4")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (1, 2, 3, 4) ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("--------------------------")
print("         Result           ")
print("--------------------------")

print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

# ---------------------------------------------------------

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exist")
else:
    print()

capitals.update({"Germany": "Berlin"})
print(capitals)

# ---------------------------------------------------------