import copy
main_grid = [
    [' ', '*', ' ', '*', ' '],
    [' ', ' ', '*', '0', '0'],
    [' ', '*', '1', ' ', ' '],
    [' ', ' ', '6', '1', '*'],
    ['*', ' ', '*', ' ', ' '],
]

def hide_bomb(game: list) -> list:
    """Renvoie la grille de comparaison mais sans les bombe afin de l'afficher avec show_grid"""
    no_bomb_grid = copy.deepcopy(game)
    for x in range(len(no_bomb_grid)):
        for y in range(len(no_bomb_grid[x])):
            if no_bomb_grid[x][y] == '*':
                no_bomb_grid[x][y] = ' '
    return no_bomb_grid


grid_test = [ 
    [' ', ' ', ' ', ' ', ' '],
    [' ', '1', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]
    

grid_vide = [ 
    [' ', ' ', ' ', ' ', ' '],
    [' ', '1', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

assert hide_bomb(grid_test)== grid_vide, "Ca marche pas"
