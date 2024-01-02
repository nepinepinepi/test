# Initialize the game board
board = [[' ' for _ in range(8)] for _ in range(8)]
board[3][3] = 'O'
board[3][4] = 'X'
board[4][3] = 'X'
board[4][4] = 'O'

# Function to print the board
def print_board(board):
    print('  0 1 2 3 4 5 6 7')
    for i in range(8):
        print(f'{i} ', end='')
        for j in range(8):
            print(f'{board[i][j]} ', end='')
        print()

# Function to check if a move is valid
def is_valid_move(board, row, col, player):
    if board[row][col] != ' ':
        return False
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for d in directions:
        r, c = row + d[0], col + d[1]
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] != ' ' and board[r][c] != player:
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] != ' ':
                r += d[0]
                c += d[1]
                if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                    return True
    return False

# Function to make a move
def make_move(board, row, col, player):
    if not is_valid_move(board, row, col, player):
        return False
    board[row][col] = player
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for d in directions:
        r, c = row + d[0], col + d[1]
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] != ' ' and board[r][c] != player:
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] != ' ':
                r += d[0]
                c += d[1]
                if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                    while (r, c) != (row, col):
                        r -= d[0]
                        c -= d[1]
                        board[r][c] = player
    return True

# Main game loop
current_player = 'X'
while True:
    print_board(board)
    print(f"Current player: {current_player}")
    move = input("Enter your move (row col): ")
    row, col = map(int, move.split())
    print(row, col)
    if make_move(board, row, col, current_player):
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print("Invalid move. Try again.")
