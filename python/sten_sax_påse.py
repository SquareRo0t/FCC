import random

computer = ["sten", "sax" , "påse"]

while True:
    x = input("Välj sten, sax eller påse ").lower()
    print(f"Du valde, {x}")

    computer_choice = random.choice(computer)
    print(f"Datorn valde: {computer_choice}")

    if x == computer_choice:
        print("Det blev oavgjort!")
    
    elif x == "sten" and computer_choice == "sax":
        print("Du vann! Sten krossar sax.")
    
    elif x == "sax" and computer_choice == "påse":
        print("Du vann! Sax klipper påse.")
    
    elif x == "påse" and computer_choice == "sten":
        print("Du vann! Påse fångar sten.")
    
    else:
        print("Datorn vann denna runda")
    