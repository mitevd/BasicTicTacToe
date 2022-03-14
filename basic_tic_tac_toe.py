class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def read_player():
    first_player_name = input("First player name: ")
    second_player_name = input("Second player name: ")

    while True:
        first_player_sign = input(f"{first_player_name} would you like to play with 'X' or 'O'").upper()
        if first_player_sign == 'X' or first_player_sign == 'O':
            break
        else:
            continue
    second_player_sign = 'O' if first_player_sign == 'X' else 'X'
    return Player(first_player_name, first_player_sign), Player(second_player_name, second_player_sign)


def make_board():
    size = 3
    result = []
    for _ in range(size):
        result.append([None] * size)

    return result


def print_board_numeration():
    print("This is the numeration of the board: ")
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')
    print(f"{player_one.name} starts first! ")


def print_current_board(board):
    for row in board:
        for el in row:
            if el == None:
                el = ' '
            print(f'| {el} ', end=' ')
        print('|')


def check_current_position(position, board, free_positions, player):
    rol , col = free_positions[position]
    board[rol][col] = player.sign
    del free_positions[position]
    return print_current_board(board)


def check_for_win(board, player_sign, rol, col):
    check_horizontal = []
    check_vertical = []
    check_left_diagonal = []
    check_right_diagonal = []
    # check horizontal
    for el in board[rol]:
        if el != player_sign:
            check_horizontal.append(True)
        else:
            check_horizontal.append(False)
    # check vertical
    for current_row in range(len(board)):
        if board[current_row][col] != player_sign:
            check_vertical.append(True)
        else:
            check_vertical.append(False)
    # check left diagonal
    for i in range(len(board)):
        if board[i][i] != player_sign:
            check_left_diagonal.append(True)
        else:
            check_left_diagonal.append(False)
    # check right diagonal
    right_diagonal_col = len(board)-1
    for row in range(len(board)):
        if board[row][right_diagonal_col] != player_sign:
            check_right_diagonal.append(True)
        else:
            check_right_diagonal.append(False)
        right_diagonal_col -= 1

    if any(check_vertical) and any(check_horizontal) and any(check_right_diagonal) and any(check_left_diagonal):
        return False

    return True


player_one, player_two = read_player()

board = make_board()

print_board_numeration()

free_positions = {
    1: [0,0],
    2: [0,1],
    3: [0,2],
    4: [1,0],
    5: [1,1],
    6: [1,2],
    7: [2,0],
    8: [2,1],
    9: [2,2]
}

turn = 1

while True:

    current_player = player_one if turn % 2 != 0 else player_two
    try:
        current_position = int(input(f"{current_player.name} choose a free position [1-9]: "))
    except ValueError:
        print("You must to choose only a number in range [1-9]")
        continue
    if current_position not in free_positions:
        print("This position is not free!")
        continue
    current_rol, current_col = free_positions[current_position]
    check_current_position(current_position, board, free_positions, current_player)
    if check_for_win(board, current_player.sign, current_rol, current_col):
        print(f"{current_player.name} won!")
        break
    if not free_positions:
        print("Nobody won!")
        break
    turn += 1


