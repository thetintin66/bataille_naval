from game import *
from grid import *


def main():
    global grid
    compteurbateau = 17

    create_grid()  # Initialise la grille

    # place_ships()  # Place les bateaux dans la grille

    while True:
        from grid import grid
        coordonnee = askSendMissile()
        ligne, colonne = cellNameTOIndex(coordonnee)
        result = sendMissileAt(ligne, colonne)

        etat = game_over(compteurbateau, result)
        compteurbateau = etat[1]
        printGrid(grid)

        if etat[0]:
            print("Game over")
            break  # Sortir de la boucle si la condition de fin de partie est remplie


# Lancement du jeu
#main()
