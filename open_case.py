grille = [
    [' ', '*', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

grille_bool = [[True for i in range(5)] for i in range(5)]

def bomb_around(game, line, column):
    """Renvoie le nombre de bombes autour d'une case donnée par le numéro de ligne et de colonne dans une grille"""
    nb_bomb = 0
    for i in range(-1,2):
        for j in range(-1,2):
            l = line+i
            c = column+j
            if c >=0 and l >=0  and l<len(game) and c<len(game[l]) and game[l][c] == '*':
                nb_bomb +=1
    return str(nb_bomb)


def open_case(game: list, line: int, column: int) -> None:
    """Modifie la grille pour y faire appaitre les indicateurs de bombes et révéler les cases"""
    game[line][column] = bomb_around(game, line, column)
    if game[line][column] == str(0):
        for i in range(-1,2):
            for j in range(-1,2):
                l = line+i
                c = column+j
                if c >=0 and l >=0  and l<len(game) and c<len(game[l]) and game[l][c] == ' ':
                    if grille_bool[l][c]:
                        grille_bool[l][c] = False
                        open_case(game, l, c)
                    else:
                        grille_bool[l][c] = False

def show_grid(grid):
    """affiche une grille avec un tableau, des coordonees, qui separent chacunes des valeurs de grid"""
    grille_2 = ''
    print("   1 2 3 4 5")
    for i in range(5):
        grille = str(i+1) + " |" + grid[i][0] + "|"+ grid[i][1] + "|"+ grid[i][2]+ "|"+ grid[i][3]+ "|"+ grid[i][4]+ "|"
        grille_2 = grille_2 + grille + "\n"
    return grille_2

open_case(grille, 1, 4)
print(show_grid(grille))

