from game import *
from main import *

def launch_game():
    print("Lancement du jeu de bataille navale...")
    main()

def modify_grid():
    print("Modification de la grille...")
    # Mettez ici le code permettant à l'utilisateur de modifier la grille

def quit_game():
    print("Quitter le jeu.")
    exit()

def main_menu():
    while True:
        print("=== MENU ===")
        print("1. Lancer le jeu")
        print("2. Modifier la grille")
        print("3. Quitter")
        choice = input("Entrez votre choix : ")

        if choice == '1':
            launch_game()
        elif choice == '2':
            modify_grid()
        elif choice == '3':
            quit_game()
        else:
            print("Choix invalide. Veuillez entrer un numéro correspondant à une option du menu.")


main_menu()
