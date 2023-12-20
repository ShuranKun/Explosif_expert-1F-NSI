grid = [
    [' ', '*', ' ', ' ', ' '],
    [' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' '],
]

def positionne_request(game: list) -> tuple:
    """Demande à l'utilisateur un numéro de ligne et de colonne pour une case dans le jeu.
    Renvoie la ligne et la colonne choisies.
    """
    max_line = len(game) - 1
    max_column = len(game[0]) - 1

    while True:
        try:
            line = int(input("Entrez le numéro de ligne : "))
            if 0 <= line <= max_line:
                break
            else:
                print(f"Le nombre maximum de lignes est {max_line}")
        except ValueError:
            print("Veuillez entrer un nombre entier pour la ligne.")

    while True:
        try:
            column = int(input("Entrez le numéro de colonne : "))
            if 0 <= column <= max_column:
                break
            else:
                print(f"Le nombre maximum de colonnes est {max_column}")
        except ValueError:
            print("Veuillez entrer un nombre entier pour la colonne.")

    return line, column

# Testé par Sacha Girardeau