import re  

name = ""
name2 = ""
email = ""
podekovani = "Děkuji za vaší pozornost"
max_pokusy = 3
pokusy = 0
is_registered = False 

email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"  # Regulární výraz

def ukonceni(vyzva):
    """ukočení programu pomocí 'exit'."""
    vstup = input(vyzva)
    if vstup.lower() == "exit":
        print("Program byl ukončen na žádost uživatele. Děkujeme.")
        exit()
    return vstup
