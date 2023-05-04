board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
winner = None
gameRunning = True
gameOver = False


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



def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def interaction(player1, player2, board):
    possible_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    while True:
        if len(possible_positions) == 0:
            break
        print("Player1's turn")
        position = int(input("Choose a position between 0-8\n"))
        if position not in possible_positions:
            print("Invalid position, try again!")
        else:
            board[position] = player1
            possible_positions.remove(position)
        print_board(board)


        # elif player2_choice in possible_positions:
        #     board[player2_choice] = player2
        #     possible_positions.pop(player2_choice)
        #
print(interaction(player1,player2,board))








