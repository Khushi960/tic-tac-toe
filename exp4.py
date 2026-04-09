board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-"*5)

def check_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[i] == player for i in pos) for pos in win_positions)

def is_full(b):
    return ' ' not in b

def minimax(b, is_max):
    if check_winner(b, 'X'):
        return 1
    if check_winner(b, 'O'):
        return -1
    if is_full(b):
        return 0

    if is_max:
        best = -1000
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, False)
                b[i] = ' '
                best = max(best, score)
        return best
    else:
        best = 1000
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, True)
                b[i] = ' '
                best = min(best, score)
        return best

def best_move():
    best_val = -1000
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def play():
    print("Positions:")
    print("1|2|3\n-----\n4|5|6\n-----\n7|8|9")

    while True:
        print("\ncurrent board:")
        print_board()

        user = int(input("Enter position (1-9): ")) - 1

        if user < 0 or user > 8 or board[user] != ' ':
            print("Invalid move try again.")
            continue

        board[user] = 'O'

        if check_winner(board, 'O'):
            print_board()
            print("You Win")
            break

        if is_full(board):
            print_board()
            print("draw")
            break

        comp = best_move()
        board[comp] = 'X'

        print("\nComputer played:")

        if check_winner(board, 'X'):
            print_board()
            print("Computer Wins")
            break

        if is_full(board):
            print_board()
            print("draw")
            break

play()