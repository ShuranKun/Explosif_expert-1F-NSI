#Verifie si chaque case a une bombe

grid = [
    [' ', '*', ' ', ' ', ' '], 
    [' ', ' ', '*', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', '*'], 
    ['*', ' ', ' ', ' ', ' '], 
]




def bomb_checker(grid: list, line: int, column: int) -> bool:
    """Renvoie True ou False si la case indiqué par la ligne(line) et la colonne(column) contient une bombe ou non"""
    check = False
    if grid[line][column] == '*':
        check = True
    return check

print(bomb_checker(grid, 0, 1))
            



    







