import random
#Positionne aléatoirement des bombes dans la grille du jeu 


def random_bomb(nbomb: int) -> list:
    """Place un nombre de bombe choisit dans une grille vide, chaque bombe a des coordonnées au hasard"""
    grid = [[' ' for i in range(5)] for i in range(5)]
    for i in range (nbomb):
        column = random.randint(0,4)
        line = random.randint(0,4)
        while grid[line][column] != ' ':
            column = random.randint(0,4)
            line = random.randint(0,4)
        grid[line][column] = '*'
    return grid

