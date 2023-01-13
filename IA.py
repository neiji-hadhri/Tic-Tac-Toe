import random
BOARD = 3
X = "X "
O = "O "
CELLULE_VIDE = "- "

def tableau_vide():
    return [[CELLULE_VIDE for _ in range(BOARD)] for _ in range(BOARD)]

def affichage(board):

    for row in board:
        print("| ",*row,"| ")
    print("\n")
    

def play_ia(player, board):

    cellules_vides = [index for index in range(BOARD * BOARD) if board[index // BOARD][index % BOARD] == CELLULE_VIDE]
    index = random.choice(cellules_vides)
    row = index // BOARD
    col = index % BOARD
    board[row][col] = player

def play(player, board):
    while True:
        try:

            index = int(input("{}, choisissez un indice (0 à 8) : ".format(player)))
            row = index // BOARD
            col = index % BOARD
            if board[row][col] == CELLULE_VIDE:
                board[row][col] = player
                return
            else:
                print("Ce coup n'est pas valide, veuillez réessayer.")
                continue
        except ValueError:
            print("Vous devez entrer un nombre entier, veuillez réessayer.")
            continue

def gagner(player, board):

    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(BOARD):
        if all(board[row][col] == player for row in range(BOARD)):
            return True
    if all(board[i][i] == player for i in range(BOARD)):
        return True
    if all(board[i][BOARD - i - 1] == player for i in range(BOARD)):
        return True
    return False
def plein(board):
    return all(i != CELLULE_VIDE for row in board for i in row)

def play_game():

        player_x_name = input("Entrez votre nom : ")
        player_o_name = "IA"
        board = tableau_vide()

        while True:
            affichage(board)
            play(X, board)
            if gagner(X, board):
                affichage(board)
                print("{} a gagné !".format(player_x_name))
                break

            if plein(board):
                affichage(board)
                print("Match nul !")
                break
            affichage(board)
            play_ia(O, board)

            if gagner(O, board):
                affichage(board)
                print("{} a gagné !".format(player_o_name))
                break

            if plein(board):
                affichage(board)
                print("Match nul !")
                break


play_game()