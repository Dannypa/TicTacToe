from TicTacToe import moves
from random import randint
from time import sleep


def draw_field():
    global field
    print("---------")
    for i in range(2, -1, -1):
        print('|', end=' ')
        for col in field:
            if col[i] != '_':
                print(col[i], end=' ')
            else:
                print(' ', end=' ')
        print('|')
    print("---------")


# noinspection DuplicatedCode
def check_state():
    global field
    # checks victory
    for col in field:  # check columns
        x_s = [i == 'X' for i in col]
        o_s = [i == 'O' for i in col]
        if all(x_s):
            print("X wins")
            return True
        elif all(o_s):
            print("O wins")
            return True
    for i in range(3):  # check rows
        x_s = []
        o_s = []
        for col in field:
            x_s.append(col[i] == 'X')
            o_s.append(col[i] == 'O')
        if all(x_s):
            print("X wins")
            return True
        elif all(o_s):
            print("O wins")
            return True
    # check diagonals
    x_s_r = []  # from right to left
    o_s_r = []
    x_s_l = []
    o_s_l = []  # from left to right
    for i in range(3):
        x_s_r.append(field[i][i] == 'X')
        o_s_r.append(field[i][i] == 'O')
        x_s_l.append(field[i][2 - i] == 'X')
        o_s_l.append(field[i][2 - i] == 'O')
    if all(x_s_l) or all(x_s_r):
        print("X wins")
        return True
    elif all(o_s_l) or all(o_s_r):
        print("O wins")
        return True
    for col in field:
        for i in col:
            if i == '_':
                return False
    print("Draw")
    return True


def get_coordinates():
    _x, _y = None, None
    while True:
        try:
            _x, _y = map(int, input('Enter the coordinates: ').split())
        except ValueError:
            print("You should enter numbers!")
            continue
        if (not 1 <= _x <= 3) or (not 1 <= _y <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        _x -= 1
        _y -= 1
        if field[_x][_y] != '_':
            print("This cell is occupied! Choose another one!")
            continue
        break
    return _x, _y


def machine_move(dif, sign):
    global field
    print(f"Making move level \"{dif}\"")
    sleep(1)
    if dif == 'easy':
        moves.easy_move(field, sign)
    elif dif == 'medium':
        moves.medium_move(field, sign)
    else:
        tmp, x, y = moves.hard_move(field, sign)
        field[x][y] = sign
    draw_field()


def user_move(sign):
    global field
    x, y = get_coordinates()
    field[x][y] = sign
    draw_field()


def game(param):
    signs = ['X', 'O']
    if param.count('user') == 1:
        _moves = ['user_move(user_sign)', 'machine_move(dif, machine_sign)']
        user_sign = signs[param.index('user')]
        # noinspection PyUnusedLocal
        machine_sign = signs[1 - param.index('user')]
        # noinspection PyUnusedLocal
        dif = param[1 - param.index('user')]
        if user_sign == 'O':
            _moves.reverse()
        draw_field()
        while True:
            eval(_moves[0])
            if check_state():
                return
            eval(_moves[1])
            if check_state():
                return
    elif param.count('user') == 2:
        draw_field()
        while True:
            user_move('X')
            if check_state():
                return
            user_move('O')
            if check_state():
                return
    else:
        draw_field()
        while True:
            machine_move(param[0], 'X')
            if check_state():
                return
            machine_move(param[1], 'O')
            if check_state():
                return


while True:
    field = [['_' for j in range(3)] for i in range(3)]
    command = input("Input command: ")
    com_list = command.split(' ')
    if com_list[0] == 'exit':
        exit(0)
    elif com_list[0] == 'start':
        if len(com_list) == 3 and all([com_list[i] in {'easy', 'user', 'medium', 'hard'} for i in range(1, 3)]):
            game(com_list[1:])
        else:
            print("Bad parameters!")
    else:
        print("Unknown command")