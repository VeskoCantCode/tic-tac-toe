import sys


# Main while loop responsible for the player selection
def player_selection():
    while True:
        player1 = input("Choose your mark, Player1.\nOptions: press X or O\n")
        player2 = ""
        if player1.capitalize() == "X":
            player2 += "O"
            print(f"Player1: {player1}\n"
                  f"Player2: {player2}")
            return player1, player2
        elif player1.capitalize() == "O":
            player2 += "X"
            print(f"Player1: {player1}\n"
                  f"Player2: {player2}")
            break
        elif player1.capitalize() != "X" and "O":
            print("Invalid choice!\nTry again!")
            continue


# Function responsible for  printing the board
def print_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])


# Functions defining the winner
def check_if_player_wins(player, players_list):
    winning_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                          [1, 4, 7], [2, 5, 8], [3, 6, 9],
                          [1, 5, 9], [3, 5, 7]
                          ]
    for condition in winning_conditions:
        if set(condition).issubset(set(players_list)):
            print(f"'{player}' player wins!")
            return True


# The main loop of the game
def main(player1, player2):
    board = ["-" for i in range(0, 10)]
    player1_list_of_moves = []
    player2_list_of_moves = []
    possible_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        switch_turn = False
        if not switch_turn:
            print("Player1's turn")
            try:
                position1 = int(input("Choose a position between 1-9\n"))
                if position1 not in possible_positions:
                    print("Invalid position, try again!")
                else:
                    board[position1] = player1
                    player1_list_of_moves.append(position1)
                    switch_turn = True
                    possible_positions.remove(position1)
                    print_board(board)
                    if check_if_player_wins(player1, player1_list_of_moves):
                        break
            except Exception as e:
                print("Error! Try again!")
                print(e)

        if switch_turn:
            print("Player2's turn")
            try:
                position2 = int(input("Choose a position between 1-9\n"))

                if position2 not in possible_positions:
                    print("Invalid position, try again!")
                else:
                    board[position2] = player2
                    player2_list_of_moves.append(position2)
                    possible_positions.remove(position2)
                    print_board(board)
                    if check_if_player_wins(player1, player1_list_of_moves):
                        break
            except Exception as e:
                print("Error! Try again!")
                print(e)
    play_again = input(
        "Do you want to play again?\n'y' for yes and 'n' for no.\n")
    if play_again == "n":
        sys.exit()
    elif play_again == "y":
        main(player1, player2)
    else:
        print(
            "That is not what you were supposed to write in but i will take it as a yes :>")


if __name__ == "__main__":
    player1, player2 = player_selection()
    main(player1, player2)
