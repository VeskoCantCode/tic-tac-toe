board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = None
gameOver = False

# Two-player gameplay
player1 = input("Choose your mark,Player1. Options: press X or O\n")
player2 = ""
if player1.upper() == "X":
    player2 += "O"
    print(f"Player1: {player1}\n"
          f"Player2: {player2}")
elif player1.upper() == "O":
    player2 += "X"
    print(f"Player1: {player1}\n"
          f"Player2: {player2}")


# Function responsible for  printing the board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Functions defining the winner
def check_if_player_wins(player,board):
    winning_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],
                          [0, 4, 8], [2, 4, 6]
                          ]
    for condition in winning_conditions:
        if board[condition] == player:
              pass







# The main loop of the game
def interaction(player1, player2, board):
    possible_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    while True:
        switch_turn = False
        # if gameOver-> call the winner function and break
        if len(possible_positions) == 0:
            break
        if switch_turn == False:
            print("Player1's turn")
            position1 = int(input("Choose a position between 0-8\n"))
            if position1 not in possible_positions:
                print("Invalid position, try again!")
            else:
                board[position1] = player1
                switch_turn = True
                possible_positions.remove(position1)
                print_board(board)

        if switch_turn:
            print("Player2's turn")
            position2 = int(input("Choose a position between 0-8\n"))
            if position2 not in possible_positions:
                print("Invalid position, try again!")
            else:
                board[position2] = player2
                possible_positions.remove(position2)
                print_board(board)

print(interaction(player1,player2,board))








