# 5x5 grid
# number marked on all boards


def mark_board(board, number):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == number:
                board[i][j] = 'X'



def display_board(board):
    for row in board:
        print(' '.join(str(x) for x in row))
    print()


def check_win(board):
    for row in board:
        if all(x == 'X' for x in row):
            return True

    # check each column
    for i in range(len(board[0])):
        cells = [row[i] for row in board]
        if all(x == 'X' for x in cells):
            return True



def copy_board(board):
    return [[cell for cell in row] for row in board]

def sum_unmarked(board):
    return sum([sum([cell for cell in row if cell != 'X']) for row in board])

with open('i') as f:
    random_input = [int(v) for v in f.readline().split(',')]

    boards = []
    board = None
    for l in f:
        l = l.strip()
        if len(l) == 0:
            if board is not None:
                boards.append(board)
            board = []
            continue
        else:
            board.append([int(x) for x in l.split()])

    print(boards)

    og_boards = [copy_board(board) for board in boards]


    for chosen in random_input:
        for board in boards:
            mark_board(board, chosen)

        print("Chosen", chosen, "\n\n\n")

        for i, board in enumerate(boards):
            if check_win(board):
                display_board(board)
                display_board(og_boards[i])
                print(sum_unmarked(board))
                print(sum_unmarked(board) * chosen)
                print("Win!")
                exit()



