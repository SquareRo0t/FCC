print("Welcome to the Adventure!")

x = input("Which way would you like to go? (left/right): ").lower()

if x == "left":
    print("Antoher path leading to two paths. Up and Down, which way do you take this time?")

    y = input("Type where you want to go (up/down): ").lower()

    if y == "up":
        print("There's nothing here")
    elif y == "down":
        print("Plenty of gold")
    else:
        print("Type up or down please")
    
elif x == "right":
    print("You see an animal")

else:
    print("Please choose the ways you can go")

