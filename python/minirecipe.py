def recipe(namn, ingredienser, portioner):
    print(f'{namn} för {portioner} portioner')

    for produkt, mangd in ingredienser.items():
        ny_mangd = (mangd / 4) * portioner

        print(f'{ny_mangd} {produkt}')
    print('-' * 30)

pannkakor = {
    'Ägg (st)': 3,
    'Mjölk (dl)': 6,
    'Vetemjöl (dl)': 3,
    'Smör (g)': 50
    }

antal = int(input('Hur många portioner vill du göra? ').lower())

recipe('Pannkakor', pannkakor, antal)