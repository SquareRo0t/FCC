# Nivå 1
# print("J och 29")

# namn = "J"
# stad = "stockholm"
# print(f"Mitt namn är {namn} och bor i {stad}")

# print("Var vänlig och skriv ditt namn ")
# x = input()
# print("Hej, " + x)

# def area_rektangel(bas, höjd):
#     area = bas * höjd
#     print(area)

# area_rektangel(3,5)

# x_tal = input("Skriv ett tal: ")
# tal = int(x_tal)

# if tal % 2 == 0:
#     print("Talet är jämnt")
# else:
#     print("Talet är udda")

# age = input("How old are you? ")
# age_int = int(age)

# if 4 <= age_int <=12:
#     print("You're a child")
# elif age_int == 13 and age_int <= 17:
#     print("You're a teen")
# elif age_int >= 18:
#     print("You're an adult")
# else:
#     print("a baby")


# filmer = ["film1", "film2", "film3", "film4", "film5"]

# for x in filmer:
#     print(x)


# toala_summa = 0
# for alla_tal in range(1, 101): # Range för siffor 1 och uppåt
#     toala_summa += alla_tal
# print(toala_summa)

# def take_name(name):
#     return f"Hej, {name}!"

# print(take_name("Anna"))

# Skriv en funktion som tar två tal och returnerar det större av dem
# def tva_tal(tal1, tal2):
#     if tal1 > tal2:
#         print(f"{tal1} är störst")
#     else:
#         print(f"{tal2} är störst")
# (tva_tal(1,2))

# Skriv en funktion som räknar hur många vokaler det finns i ett ord
# def antal_vokaler(ord):
#     vokaler ="aeiouyåäö"
#     antal = 0

#     for tecken in ord.lower():
#         if tecken in vokaler:
#             antal += 1

#     return antal

# print(antal_vokaler("människa"))


# Bygg ett enkelt gissningsspel – datorn väljer ett tal 1–10, användaren gissar tills de har rätt
import random
dator_slump = random.randint(1, 10)

while True:
    x = input("Gissa på en siffra mellan 1-10: ")
    
    gissning = int(x)
    print(f"Du gissde på {gissning}")

    if gissning == dator_slump:
        print("Grattis du gissade rätt nummer")
        break
    elif gissning > dator_slump:
        print("Du gissade för högt! Försök igen.")
    else:
        print("Du gissade för låg! Försök igen.")

