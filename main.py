from game import *
from grid import *


def main():
    global grid
    compteurbateau = 17

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
            break  



