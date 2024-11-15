# Tic Tac Toe game

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
    # All winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    # Check if any winning combination is satisfied by the player
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw():
    return " " not in board

# Function to handle a player move
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Please try again.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Main game function
def play_game():
    current_player = "X"
    
    while True:
        display_board()
        player_move(current_player)
        
        # Check for a win
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        # Check for a draw
        elif check_draw():
            display_board()
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
