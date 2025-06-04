import math

board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
    print()

def is_winner(brd, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pos in win_positions:
        if brd[pos[0]] == brd[pos[1]] == brd[pos[2]] == player:
            return True
    return False

def is_draw(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i, cell in enumerate(brd) if cell == ' ']

def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    if is_winner(brd, 'X'):
        return -1
    if is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, depth + 1, False)
            brd[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, depth + 1, True)
            brd[move] = ' '
            best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

def play_game():
    print("Tic Tac Toe — You (X) vs AI (O)")
    print("Enter positions 1 to 9 as shown below:")
    print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    while True:
        print_board()

        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1
                if move < 0 or move >= 9 or board[move] != ' ':
                    print("Invalid move. Try again.")
                else:
                    board[move] = 'X'
                    break
            except ValueError:
                print("Please enter a number from 1 to 9.")

        if is_winner(board, 'X'):
            print_board()
            print("🎉 You win!")
            break
        if is_draw(board):
            print_board()
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()

        if is_winner(board, 'O'):
            print_board()
            print("😔 AI wins!")
            break
        if is_draw(board):
            print_board()
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()

