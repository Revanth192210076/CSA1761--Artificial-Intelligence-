import math

# Initialize the game board
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw():
    return " " not in board

# Alpha-Beta Pruning Algorithm
def alpha_beta_pruning(is_maximizing, alpha, beta):
    if check_win("O"):
        return 1  # AI wins
    elif check_win("X"):
        return -1  # Player wins
    elif check_draw():
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = alpha_beta_pruning(False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # Beta cut-off
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = alpha_beta_pruning(True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # Alpha cut-off
        return best_score

# Function to find the best move for the AI using Alpha-Beta Pruning
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = alpha_beta_pruning(False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Function to handle a player move
def player_move():
    while True:
        try:
            move = int(input("Enter a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Please try again.")
            else:
                board[move] = "X"
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Main game function
def play_game():
    while True:
        display_board()
        if check_win("O"):
            print("AI wins!")
            break
        elif check_win("X"):
            print("You win!")
            break
        elif check_draw():
            print("It's a draw!")
            break

        # Player's turn
        player_move()

        # Check for win or draw after player move
        if check_win("X") or check_draw():
            continue

        # AI's turn
        ai_move = best_move()
        board[ai_move] = "O"
        print(f"AI chooses position {ai_move + 1}")

# Run the game
play_game()
