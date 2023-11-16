import random

grid = [[' ' for _ in range(8)] for _ in range(8)]

# Définition des symboles pour chaque type de bateau
ship_symbols = {
    "porte_avions": 'b',#p
    "croiseur": 'b',#c
    "contre_torpilleur": 'b',#t
    "torpilleur": 'b'#s
}


def displayGrid(grid):
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


def createGrid():
    placeShips(grid)
    displayGrid(grid)
    return grid


def is_valid_location(grid, x, y, ship_size, direction):
    positions = []
    for i in range(ship_size):
        new_x = x + direction[0] * i
        new_y = y + direction[1] * i
        if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == ' '):
            return False
        positions.append((new_x, new_y))
    
    for pos in positions:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= pos[0] + i < len(grid) and 0 <= pos[1] + j < len(grid[0]):
                    if grid[pos[0] + i][pos[1] + j] != ' ':
                        return False
    return True


def placeShip(grid, ship_size, symbol):
    directions = [(0, 1), (1, 0)]  # Droite, Bas
    while True:
        x = random.randint(0, len(grid) - 1)
        y = random.randint(0, len(grid[0]) - 1)
        direction = random.choice(directions)
        
        if is_valid_location(grid, x, y, ship_size, direction):
            for i in range(ship_size):
                new_x = x + direction[0] * i
                new_y = y + direction[1] * i
                grid[new_x][new_y] = symbol
            break


def placeShips(grid):
    # Placez chaque type de bateau dans la grille
    placeShip(grid, 5, ship_symbols["porte_avions"])
    placeShip(grid, 4, ship_symbols["croiseur"])
    for _ in range(2):
        placeShip(grid, 3, ship_symbols["contre_torpilleur"])
    placeShip(grid, 2, ship_symbols["torpilleur"])


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


def main():
    compteurbateau = 17
    grid = createGrid()

    while True:
        print("ligne =", end=" ")
        ligne, colone = askSendMissile()
        result = sendMissileAt(ligne, colone)

        etat = game_over(compteurbateau, result)
        compteurbateau = etat[1]
        displayGrid(grid)
        if etat[0] == True:
            print("game_over")
            break  # Sortir de la boucle si la condition de fin de partie est remplie


main()






