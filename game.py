from grid import *
#from main import *

#fonction qui transforme A1 en coordonée 00
def cellNameTOIndex(coordonnee):
    while True:
        try:
            
            if len(coordonnee) >= 2:
                colonne = coordonnee[0]
                ligne = int(coordonnee[1:])
                
                if colonne.isalpha() and colonne.isupper() and 1 <= ligne <= 26:
                    poscolonne = ord(colonne) - ord('A')
                    posligne = ligne - 1
                    return posligne, poscolonne
                else:
                    print("Coordonnées invalides. Assurez-vous que la colonne est une lettre de A à Z et la ligne est un nombre de 1 à 26.")
            else:
                print("Coordonnées invalides.")
        except ValueError:
            print("Coordonnées invalides. Assurez-vous que la colonne est une lettre de A à Z et la ligne est un nombre de 1 à 26.")


# Fonction pour demander ou envoyer missile
def askSendMissile():
    print("debut fonction ask")
    coordonnee = input("Entrez les coordonnées (ex: A1): ").upper()
    return coordonnee


# Fonction pour envoyer un missile à une position donnée
def sendMissileAt(rowIndex, columnIndex):
    from grid import grid
    print("debut fonction senmis")
    if grid[rowIndex][columnIndex] == 'h' or grid[rowIndex][columnIndex] == 'm':
        print("Cette case a déjà été touchée. Veuillez tirer ailleurs.")
        return False
    elif grid[rowIndex][columnIndex] == 'b':
        grid[rowIndex][columnIndex] = 'h'  # Touché un bateau
        return True
    else:
        grid[rowIndex][columnIndex] = 'm'  # Touché de l'eau
        return False


# Fonction pour vérifier si le jeu est terminé
def game_over(compteurbateau, result):
    if result:
        compteurbateau -= 1
        
    if compteurbateau == 0:
        return True, compteurbateau
    else:
        return False, compteurbateau
