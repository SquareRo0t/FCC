# ---------------------------------------------------------

def display_invoice(username, amount, due_data):
    print(f"Hello {username}")
    print(f"Your bill of €{amount:.2f} is due {due_data}")

display_invoice("Chicken", 40, "02/03")

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(30, 15)

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=46, area=123, first=456, last=789)
print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_adress(street="123 hahga", apt="1", city= "älv" , state= "ÄL", zip="123456")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
         print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('zip')}")

shipping_label("Mr", "Sherlock", "Holmes", "Legend",
               street="123 brit", apt="2", city="Lond", zip="2344" )

# ---------------------------------------------------------