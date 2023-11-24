from game import *
from main import *

def launch_game():

    print("Lancement du jeu de bataille navale...")
    place_ships() #place les bateaux aletoirement (la grille et declarer a 8*8)
    main() #lancement du main

def modify_grid():

    print("Modification de la grille...")
    create_grid()  # creer la grille
    place_ship_manually() #lancela fonction qui permet de placer des bateau manuellement
    main()#lencement du main
   

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
