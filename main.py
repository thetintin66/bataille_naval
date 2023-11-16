
# Créer une grille vide
grid = [[' ' for _ in range(8)] for _ in range(8)]

# Placer les bateaux
grid[0][0] = 'b'
grid[0][1] = 'b'
'''
grid[2][5] = 'b'
grid[3][5] = 'b'
grid[4][5] = 'b'

grid[6][2] = 'b'
grid[6][3] = 'b'
grid[6][4] = 'b'
grid[6][5] = 'b'
'''

def printGrid(grid):
    # Lettres pour les colonnes
    print("  A  B  C  D  E  F  G  H")
    
    # Affichage de la grille avec les numéros de ligne et les symboles
    for i in range(len(grid)):
        print(f"{i + 1}", end=" ")
        for j in range(len(grid[i])):
            if grid[i][j] == 'b':
                print('⛵', end=" ")
            elif grid[i][j] == ' ':
                print('🌊', end=" ")
            elif grid[i][j] == 'h':
                print('💥', end=" ")

            elif grid[i][j] == 'm':
                print('💦', end=" ")
            else:
                print(grid[i][j], end=" ")
        print()  # Nouvelle ligne pour la prochaine rangée



def askSendMissile():
    coordonnee = input("Entrez les coordonnées (ex: A1): ").upper()
    colonne = coordonnee[0]
    ligne = coordonnee[1]
    #print(ligne, colonne)

    posligne = int(ligne) - 1

    if colonne.isalpha() and colonne.isupper():  # Vérifiez si la colonne est alphabétique et en majuscules
        poscolonne = ord(colonne) - ord('A')
        
        return posligne, poscolonne
    else:
        poscolonne = int(colonne) - 1  # Si ce n'est pas une lettre, essayez de le convertir en entier
        return posligne, poscolonne



def sendMissileAt(rowIndex, columnIndex):

    if grid[rowIndex][columnIndex] == 'h' or grid[rowIndex][columnIndex] == 'm':
        print("Cette case a déjà été touchée. Veuillez tirer ailleurs.")
        return False
    elif grid[rowIndex][columnIndex] == 'b':
        grid[rowIndex][columnIndex] = 'h'  # Touché un bateau
        return True
    else:
        grid[rowIndex][columnIndex] = 'm'  # Touché de l'eau
        return False
  
    
def game_over(compteurbateau,result):
    
    if (result == True) :
        compteurbateau = compteurbateau - 1 
       
    if (compteurbateau == 0) :
        return True,compteurbateau
    else :
        return False,compteurbateau


def main() :
    compteurbateau = 2
    # Afficher la grille initiale
    printGrid(grid)
    while(True) :
        print("ligne =",end =" ")

        ligne,colone = askSendMissile()

        result = sendMissileAt(ligne, colone)

        etat = game_over(compteurbateau,result) 
        compteurbateau = etat[1]
        #print("bateau restant" , compteurbateau)

        #print(game)
        printGrid(grid)
        if (etat[0] == True) :
            print("game_over")
            return 0

        



main()

