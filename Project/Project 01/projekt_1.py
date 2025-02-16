"""
# První projekt do Engeto Online Python Akademie
# author: Slavomír Strnad
# email: Rimovals.s@seznam.cz
"""

# Texty
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# přístup do programu
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
    "slavek": "slavek" # Moje testovani
}

def prihlaseni():
    print("Přihlášení k programu")
    jmeno = input("username: ")
    heslo = input("password: ")

    if jmeno in uzivatele and uzivatele[jmeno] == heslo:
        print("-" * 40)
        print(f"Welcome to the app, *{jmeno}*")
        return True
    else:
        print("unregistered user, terminating the program..")
        exit()

# volba textu
def vyber_text():
    print("\nWe have 3 texts to be analyzed.")
    print("-" * 40)
    try:
        volba = int(input("Enter a number btw. 1 and 3 to select: "))
        print("-" * 40)
        if 1 <= volba <= len(TEXTS):
            return TEXTS[volba - 1]
        else:
            print("Invalid number, terminating the program..")
            exit()
    except ValueError:
        print("Invalid input, terminating the program..")
        exit()

# analýza textu
def analyzuj_text(text):
    slova = text.split()
    pocet_slov = len(slova)
    pocet_velky_pocatek = sum(1 for slova_v_textu in slova if slova_v_textu.istitle())
    pocet_velka_pismena = sum(1 for slova_v_textu in slova if slova_v_textu.isupper() and slova_v_textu.isalpha())
    pocet_mala_pismena = sum(1 for slova_v_textu in slova if slova_v_textu.islower())
    pocet_cisel = sum(1 for slova_v_textu in slova if slova_v_textu.isdigit())
    suma_cisel = sum(int(slova_v_textu) for slova_v_textu in slova if slova_v_textu.isdigit())
    
    # Vypíše proměnné 
    print(f"There are {pocet_slov} words in the selected text!")
    print(f"There are {pocet_velky_pocatek} titlecase words!")
    print(f"There are {pocet_velka_pismena} uppercase words!")
    print(f"There are {pocet_mala_pismena} lowercase words!")
    print(f"There are {pocet_cisel} numeric strings!")
    print(f"The sum of all the numbers {suma_cisel}")
    
    # Generování slov
    delky_slov = {}
    for slova_v_textu in slova:
        delka = len(slova_v_textu.strip(".,!?"))
        delky_slov[delka] = delky_slov.get(delka, 0) + 1
        
    print("-" * 40)
    print("LEN| OCCURENCES  |NR.")
    print("-" * 40)
    for delka, cetnost in sorted(delky_slov.items()):
        print(f"{delka:<3}| {'*' * cetnost:<11} |{cetnost}")

# Možnost opakování pro lepší testování
def hlavni_program():
    if prihlaseni():
        while True:
            text = vyber_text()
            analyzuj_text(text)

            # Ano / Ne pro ukončení 
            volba = input("\n Do you want to analyse another text? (yes/no): ").strip().lower()
            if volba.lower() not in ["y", "yes"]:
                print("Thank you for using the program. Goodbye!")
                break
    input("Press ENTER to exit...")  # Zabrání zavření okna a dává další možnost.

# Zavolám funkci
hlavni_program()        
