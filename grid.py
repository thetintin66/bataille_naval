import random

# Variables globales pour la grille et ses dimensions
grid = [[' ' for _ in range(8)] for _ in range(8)]
ligne = 0
colonne = 0

# Définition des symboles pour chaque type de bateau
ship_symbols = {
    "porte_avions": 'b',
    "croiseur": 'b',
    "contre_torpilleur": 'b',
    "torpilleur": 'b'
}

# Fonction pour créer une grille si elle n'existe pas déjà
def create_grid():
    global grid
    global ligne
    global colonne
    while True:
        try:
            ligne = int(input("Entrez le nombre de lignes : "))
            colonne = int(input("Entrez le nombre de colonnes : "))
            if ligne > 26:
                ligne = 26
            if colonne > 26:
                colonne = 26
            grid = [[' ' for _ in range(colonne)] for _ in range(ligne)]
            place_ships()
            break
        except ValueError:
            print("Veuillez entrer des nombres entiers pour les dimensions de la grille.")


# Fonction pour placer tous les bateaux dans la grille
def place_ships():
    global grid
    pre_place_ships(grid, 5, ship_symbols["porte_avions"])
    pre_place_ships(grid, 4, ship_symbols["croiseur"])
    for _ in range(2):
        pre_place_ships(grid, 3, ship_symbols["contre_torpilleur"])
    pre_place_ships(grid, 2, ship_symbols["torpilleur"])

    printGrid(grid)  # Afficher la grille après le placement des bateaux


# Fonction pour placer aléatoirement les bateaux dans la grille
def pre_place_ships(grid, ship_size, symbol):
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
            return grid  # Retourne la grille mise à jour

# Fonction pour vérifier si l'emplacement pour placer un bateau est valide
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

# Fonction pour afficher la grille avec des symboles spécifiques
def printGrid(grid):
    print("Début de la fonction printGrid()")
    print("  ", end="")
    for i in range(len(grid[0])):
        print(chr(65 + i), end="  ")
    print()

    for i in range(len(grid)):
        print(f"{i + 1}", end=" ")
        for j in range(len(grid[i])):
            symbol = grid[i][j]
            if symbol == 'b':
                print('⛵', end=" ")
            elif symbol == ' ':
                print('🌊', end=" ")
            elif symbol == 'h':
                print('💥', end=" ")
            elif symbol == 'm':
                print('💦', end=" ")
            else:
                print(symbol, end=" ")
        print()

    print("Fin de la fonction printGrid()")

