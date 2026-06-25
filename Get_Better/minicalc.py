def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    return x / y


def mul(x, y):
    return x * y


def percent(x, y):
    return x * (1 - y / 100)


print("Welcome, what kind of calculations do you want to do today?")
print("1. Addition + ")
print("2. Subtraction - ")
print("3. Division / ")
print("4. Mulitplication * ")
print("5. Percent %")
print("6. Quit")

while True:
    x = input("Please insert number 1-6 depending on operator you want to use ")

    if x == "1":
        print("Enter the numbers you want to add together ")
        num1 = float(input("Enter first number "))
        num2 = float(input("Enter second number "))

        res = add(num1, num2)
        print("The anser is: ", res)

    elif x == "2":
        print("Enter the numbers you want to subtract ")
        num1 = float(input("Enter first number "))
        num2 = float(input("Enter second number "))

        res = sub(num1, num2)
        print("The anser is: ", res)

    elif x == "3":
        print("Enter the numbers you want to divide ")
        num1 = float(input("Enter first number "))
        num2 = float(input("Enter second number "))

        res = div(num1, num2)
        print("The answer is: ", res)

    elif x == "4":
        print("Enter the numbers you want to multiplie ")
        num1 = float(input("Enter first number "))
        num2 = float(input("Enter second number "))

        res = mul(num1, num2)
        print("The answer is: ", res)

    elif x == "5":
        print("Enter the price and the percent")
        num1 = float(input("Enter the total price  "))
        num2 = float(input("Enter the percent number "))

        res = percent(num1, num2)
        print("Total price after the percent:", res)

    elif x == "6":
        print("Good bye!")
        break

    else:
        print("Please pick a number between 1 - 6")
