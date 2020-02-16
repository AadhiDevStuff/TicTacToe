
game_still_running = True
winner = None
current_Player = "X"

# creating a board using array's
board =["_","_","_",
        "_","_","_",
        "_","_","_"]

# printing the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# input loop
def handle_turns(player):
    pos = input("Choose a position from 1-9: ")

    vaild_move = False
    while not vaild_move:
        
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos = input("Invalid position.Choose a position from 1-9: ")
        
        pos = int(pos)-1

        if board[pos] == "_":
            vaild_move = True
        else:
            print("Position is already occupied by " + "'"+board[pos]+"'")

    board[pos] = player
    display_board()

# checking rows for winner
def check_rows():
    global game_still_running
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        game_still_running = False


    # returning the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

# checking coloumns for winner
def check_columns():
    global game_still_running
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"

    if column_1 or column_2 or column_3:
        game_still_running = False


    # returning the winner's name
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

# checking diagonals for winner
def check_diagonals():
    global game_still_running
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[6] == board[4] == board[2] != "_"

    if diagonal_1 or diagonal_2:
        game_still_running = False


    # returning the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
   
# checking win
def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    # checking type of win 
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None   

# check if game Tied
def check_Tie():
    global game_still_running
    if "_" not in board:
        game_still_running = False


# checking if game Over
def checkGameOver():
    check_win()
    check_Tie()

# changing between "X" and "O"
def flip_Player():
    global current_Player
    if current_Player == "X":
        current_Player = "O"

    elif current_Player == "O":
        current_Player = "X"

    print(current_Player + "'s turn...")

# main game loop
def play_game():
    display_board()
    while game_still_running:
        handle_turns(current_Player)
        checkGameOver()
        flip_Player()
 
    # if game ended
    if winner == "X" or winner == "O":
        print(winner + " " + "Won")
    elif winner == None:
        print("Tied")    

        
# running the game loop
play_game()