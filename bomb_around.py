grille = [
    [' ', '*', ' ', ' ', ' '],
    [' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' '],
]


def bomb_around(game: list, line: int, column: int) -> str:
    """Renvoie le nombre de bombes autour d'une case donnée par le numéro de ligne et de colonne dans une grille"""
    nb_bomb = 0
    for i in range(-1,2):
        for j in range(-1,2):
            l = line+i
            c = column+j
            if c >=0 and l >=0  and l<len(game) and c<len(game[l]) and game[l][c] == '*':
                nb_bomb +=1
    return str(nb_bomb)


assert bomb_around(grille, 0, 2) == 2, 'Problème dans la fonction bombe_autour'
assert bomb_around(grille, 1, 3) == 1, 'Problème dans la fonction bombe_autour'


