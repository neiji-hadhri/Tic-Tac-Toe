board =["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]
Joueuractuel= "X"
winner = None
Exécution_de_jeu = True

def printtableau(board) :
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | ")

def entréeJoueur(board) :
    inp = int(input("Entrez un numéro 1-9: "))  
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = Joueuractuel
    else :
        print("Oups,Un joueur est déjà à cet endroit!")
        changer_de_Joueur() ==False

  
def vérifierHorizental(board):
    global winner
    if board[0]  == board[1] == board[2] and board[0] != "-":
        winner=board[0]
        return True
    elif board[3]  == board[4] == board[5] and board[3] != "-":
        winner=board[3]
        return True
    elif board[6]  == board[7] == board[8] and board[6] != "-":
        winner=board[6]
        return True
    

def vérifierVertical(board) :
    global winner
    if board[0]  == board[3] == board[6] and board[0] != "-":
        winner=board[0]
        return True
    elif board[1]  == board[4] == board[7] and board[1] != "-":
        winner=board[1]
        return True
    elif board[2]  == board[5] == board[8] and board[2] != "-":
        winner=board[2]
        return True
def vérifierDiagonale(board) :
    global winner
    if board[0]  == board[4] == board[8] and board[0] != "-":
        winner=board[0]
        return True
    elif board[2]  == board[4] == board[6] and board[2] != "-":
        winner=board[2]
        return True

def vérifierEgaliter(board) :
    global Exécution_de_jeu
    if "-" not in board :
        printtableau(board)
        print("C'est un match Nul!")
        Exécution_de_jeu = False

def VérifierVictoire() :
    if vérifierDiagonale(board) or vérifierHorizental(board) or vérifierVertical(board):
        print(f"the winner is {winner}")

        


def changer_de_Joueur() :

    global Joueuractuel
    if Joueuractuel == "X" :
        Joueuractuel= "O"
    else: 
        Joueuractuel = "X"
       






while Exécution_de_jeu:
    printtableau(board)
    entréeJoueur(board)
    VérifierVictoire()
    vérifierEgaliter(board)
    changer_de_Joueur()
    
