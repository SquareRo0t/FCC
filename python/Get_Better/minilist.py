print("Vad vill du titta på?  ")
print("Kött ")
print("Grönsaker ")
print("Snacks ")
print("Mejeri ")

mat_nyheter = ["Kött", "Grönsaker", "Snacks", "Mejeri"]

while True:
    x = input("").lower()

    if x == "kött":
        kött_lista = ["nötkött", "fläsk", "kycklig"]
        print("Du är i kött sektionen. Här finns: ")
        print(kött_lista)
