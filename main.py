import re
import module

# Menu
def menu():
    while True:
        print("\n--- MENU ---")
        if module.is_registered:
            print("1. Změnit údaje")
            print("2. Zobrazit údaje")
            print("3. Ukončit Program")
            volba = module.ukonceni("Vyberte možnost (1-3): ")
            
            if volba == "1":
                volba2()
            elif volba == "2":
                volba3()
            elif volba == "3":
                print("Program byl ukončen. Děkujeme.")
                exit()
            else:
                print("Neplatná volba. Zkuste to znovu.")
        else:
            print("1. Registrace")
            print("2. Ukončit Program")
            volba = module.ukonceni("Vyberte možnost (1-2): ")
            
            if volba == "1":
                volba1()
            elif volba == "2":
                print("Program byl ukončen. Děkujeme.")
                exit()
            else:
                print("Neplatná volba. Zkuste to znovu.")

# Funkce registrace
def volba1():
    """Registrace uživatele."""
    print("\n--- Registrace ---")
    module.name = module.ukonceni("Zadejte Vaše jméno: ")
    module.name2 = module.ukonceni("Zadejte Vaše příjmení: ")
    
    while True:
        email_input = module.ukonceni("Zadejte váš Email: ")
        if re.match(module.email_pattern, email_input):
            module.email = email_input
            module.is_registered = True
            print("Registrace úspěšná!")
            break
        else:
            print("Neplatný email. Zkuste to znovu.")

# Funkce pro změnu údajů
def volba2():
    """Změna údajů uživatele."""
    print("\n--- Změna údajů ---")
    module.name = module.ukonceni("Zadejte nové jméno: ")
    module.name2 = module.ukonceni("Zadejte nové příjmení: ")
    while True:
        email_input = module.ukonceni("Zadejte nový Email: ")
        if re.match(module.email_pattern, email_input):
            module.email = email_input
            print("Údaje byly úspěšně změněny.")
            break
        else:
            print("Neplatný email. Zkuste to znovu.")

# Funkce pro zobrazení údajů
def volba3():
    """Zobrazení údajů uživatele."""
    if not module.is_registered:
        print("Nejprve se prosím zaregistrujte.")
        volba1()
        return

    print("\n--- Zadané údaje ---")
    print(f"Jméno: {module.name}")
    print(f"Příjmení: {module.name2}")
    print(f"Email: {module.email}")

# Spuštění programu
menu()