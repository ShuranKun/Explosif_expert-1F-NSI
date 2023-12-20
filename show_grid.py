#Affiche la grille dans la console

grid = [
    ['i', 'l', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', '8', ' ', ' '], 
    [' ', '*', ' ', '@', ' '], 
    [' ', ' ', ' ', ' ', '1'], 
]

def show_grid(grid: list) -> str:
    """affiche une grille avec un tableau, des coordonees, qui separent chacunes des valeurs de grid"""
    grille_2 = ''
    print("   0 1 2 3 4")
    for i in range(5):
        grille = str(i) + " |" + grid[i][0] + "|"+ grid[i][1] + "|"+ grid[i][2]+ "|"+ grid[i][3]+ "|"+ grid[i][4]+ "|"
        grille_2 = grille_2 + grille + "\n"
    return grille_2


print(show_grid(grid))