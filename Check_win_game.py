# grid = [
# [' ', ' ', ' ', ' ', ' '], 
# [' ', ' ', ' ', ' ', ' '], 
# [' ', ' ', '*', '*', ' '], 
# [' ', ' ', ' ', ' ', ' '], 
# [' ', ' ', ' ', ' ', ' ']
# ]

grid = [['*' for i in range(5)] for i in range(5)]

def check_win_game(grid: list) -> bool: 
    """Verifie s'il reste des cases vides dans la grille afin de savoir si le joueur à gagner"""
    fin_de_partie = True
    for i in grid:
        for j in i:
            if j == ' ':
                fin_de_partie=False 
    return fin_de_partie

print(check_win_game(grid))


# for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if not ' ' in grid[i][j]:
#                 fin_de_partie = True