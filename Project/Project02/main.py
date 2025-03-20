"""
# Druhý projekt(2) do Engeto Online Python Akademie
# Projekt: (Tic Tac Toe)
# author: Slavomír Strnad
# email: Rimovals.s@seznam.cz
"""

def welcome():
    print("Welcome to Tic Tac Toe")
    print("========================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("\n*Horizontal \n*Vertical or \n*Diagonal row")
    print("========================================")
    print("Let's start the game")
    print("----------------------------------------")

def vytvor_pole():
    return list(range(9))

def empty(prazdny):
    return prazdny if prazdny in ["X", "O"] else " "

def vypis_pole(pole):
    print("+---+---+---+")
    print(f"| {empty(pole[0])} | {empty(pole[1])} | {empty(pole[2])} |")
    print("+---+---+---+")
    print(f"| {empty(pole[3])} | {empty(pole[4])} | {empty(pole[5])} |")
    print("+---+---+---+")
    print(f"| {empty(pole[6])} | {empty(pole[7])} | {empty(pole[8])} |")
    print("+---+---+---+")
    print("========================================")

def over_vstup(spatny_zadani, pole):

    # číslo 1-9
    if not spatny_zadani.isdigit():
        print("!---------------!--------------------!")
        print("Please enter a NUMBER from 1 to 9.")
        print("!---------------!--------------------!")
        return False
    
    # 1-9
    cislo = int(spatny_zadani)
    if cislo < 1 or cislo > 9:
        print("!---------------!--------------------!")
        print("Enter a number in the range 1-9.")
        print("!---------------!--------------------!")
        return False
    
    # obsazená pozice
    if pole[cislo - 1] in ["X", "O"]:
        print("!---------------!--------------------!")
        print("This position is already filled.")
        print("!---------------!--------------------!")
        return False
    
    return True

def vyhodnot_vyhru(pole):
    win_combo = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)            
    ]
    for (a, b, c) in win_combo:
        if pole[a] == pole[b] == pole[c]:
            return pole[a]  # vrátí X nebo O
    return None

def rematch(pole):

    if all(m in ["X", "O"] for m in pole):
        return True
    return False

def main():
    welcome()
    pole = vytvor_pole()
    vypis_pole(pole)
    
    aktualni_hrac = "X"  # začíná hráč s X
    
    while True:
        tah = input(f"Player {aktualni_hrac}, Please enter your turn number: (1-9): ")
        print("======================================")
        
        if not over_vstup(tah, pole):
            continue
        
        index = int(tah) - 1
        
        pole[index] = aktualni_hrac
        
        vypis_pole(pole)
        
        # vyhodnotit výherce
        vitez = vyhodnot_vyhru(pole)
        if vitez:
            print(f"Congratulations! Player: {vitez} win!")
            print("======================================")
            break
        
        # zkontrolujeme remízu
        if rematch(pole):
            print("Tie! nobody won. Try again...")
            print("======================================")
            break
        
        # střídání hráčů
        aktualni_hrac = "O" if aktualni_hrac == "X" else "X"

if __name__ == "__main__":
    main()
