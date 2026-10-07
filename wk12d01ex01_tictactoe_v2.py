import random


def check_winner(board):
    result = "None"
    filled_count = 0

    # Rows
    if board[1] != " " and board[1] == board[2] and board[2] == board[3]:
        result = board[1]

    if board[4] != " " and board[4] == board[5] and board[5] == board[6]:
        result = board[4]

    if board[7] != " " and board[7] == board[8] and board[8] == board[9]:
        result = board[7]

    # Columns
    if board[1] != " " and board[1] == board[4] and board[4] == board[7]:
        result = board[1]

    if board[2] != " " and board[2] == board[5] and board[5] == board[8]:
        result = board[2]

    if board[3] != " " and board[3] == board[6] and board[6] == board[9]:
        result = board[3]

    # Diagonals
    if board[1] != " " and board[1] == board[5] and board[5] == board[9]:
        result = board[1]

    if board[3] != " " and board[3] == board[5] and board[5] == board[7]:
        result = board[3]

    # Count filled spaces
    for k in range(1, 10):
        if board[k] != " ":
            filled_count += 1

    # Check for draw
    if result == "None" and filled_count == 9:
        result = "Draw"

    return result


def display_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("-+-+-")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-+-+-")
    print(board[7] + " | " + board[8] + " | " + board[9])


def get_computer_move(board):
    valid = False

    while valid == False:
        comp_move = random.randint(1, 9)

        if board[comp_move] == " ":
            valid = True
        else:
            valid = False

    return comp_move


def main():
    # Create the board
    board = [" "] * 10

    game_over = False
    winner = "None"

    # Randomly choose who starts
    r = random.randint(0, 1)

    if r == 0:
        current_player = "O"
    else:
        current_player = "X"

    # Main game loop
    while game_over == False:

        display_board(board)

        # Human player's turn
        if current_player == "O":
            valid_move = False

            while valid_move == False:
                print("Enter your move (1-9):")
                human_move = int(input())

                if human_move >= 1 and human_move <= 9:

                    if board[human_move] == " ":
                        valid_move = True
                    else:
                        print("Space occupied! Try again.")

                else:
                    print("Invalid choice! Enter 1-9.")

            board[human_move] = "O"

        # Computer's turn
        else:
            print("Computer's turn...")

            comp_choice = get_computer_move(board)
            board[comp_choice] = "X"

        # Check winner
        winner = check_winner(board)

        if winner != "None":
            game_over = True

        else:
            # Change player
            if current_player == "O":
                current_player = "X"
            else:
                current_player = "O"

    # Display final board
    display_board(board)

    # Display result
    if winner == "O":
        print("You win!")

    elif winner == "X":
        print("Computer wins!")

    else:
        print("It's a draw!")


main()
