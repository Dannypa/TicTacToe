from math import inf
from random import randint


def easy_move(field, sign):
    while True:
        x, y = randint(0, 2), randint(0, 2)
        if field[x][y] != '_':
            continue
        else:
            field[x][y] = sign
            break


def medium_move(field, sign):
    while True:
        _x, _y = randint(0, 2), randint(0, 2)
        if field[_x][_y] != '_':
            continue
        else:
            break
    # check all the columns
    for col_ind in range(3):
        col = field[col_ind]
        if (col.count('X') == 2 or col.count('O') == 2) and col.count('_') > 0:
            _x = col_ind
            _y = col.index('_')
            field[_x][_y] = sign
            return
    # check all the rows
    for row_ind in range(3):
        row = []
        for col in field:
            row.append(col[row_ind])
        if (row.count('X') == 2 or row.count('O') == 2) and row.count('_') > 0:
            _y = row_ind
            _x = row.index('_')
            field[_x][_y] = sign
            return
    # check all the diagonals
    l_r_d = []  # diag from left to right
    r_l_d = []  # diag from right to left
    for i in range(3):
        l_r_d.append(field[i][2 - i])
        r_l_d.append(field[i][i])
    if (l_r_d.count('X') == 2 or l_r_d.count('O') == 2) and l_r_d.count('_') > 0:
        _x = l_r_d.index('_')
        _y = 2 - _x
        field[_x][_y] = sign
        return
    if (r_l_d.count('X') == 2 or r_l_d.count('O') == 2) and r_l_d.count('_') > 0:
        _x = _y = r_l_d.index('_')
        field[_x][_y] = sign
        return
    field[_x][_y] = sign


def hard_move(field, sign):
    a = [all(i == '_' for i in j) for j in field]
    if all(a):
        return -1, 0, 0
    _max = -inf
    best_x, best_y = -1, -1
    for _x in range(3):
        for _y in range(3):
            if field[_x][_y] == '_':
                field[_x][_y] = sign
                s = minimax(field, sign)
                if s > _max:
                    _max = s
                    best_x, best_y = _x, _y
                field[_x][_y] = '_'
    return _max, best_x, best_y
    # field[best_x][best_y] = sign


def minimax(field, sign):
    op_sign = 'X' if sign == 'O' else 'O'
    res = get_state(field, sign)
    if res is not None:
        return res
    # opponent's move
    tmp, op_x, op_y = hard_move(field, op_sign)

    field[op_x][op_y] = op_sign

    res = get_state(field, sign)
    if res is not None:
        field[op_x][op_y] = '_'
        return res
    # AI move
    res, tmp_x, tmp_y = hard_move(field, sign)

    field[op_x][op_y] = '_'
    return res


# noinspection DuplicatedCode
def get_state(field, sign):
    for col in field:  # check columns
        x_s = [i == 'X' for i in col]
        o_s = [i == 'O' for i in col]
        if all(x_s):
            if sign == 'X':
                return 10
            else:
                return -10
        elif all(o_s):
            if sign == 'X':
                return -10
            else:
                return 10
    for i in range(3):  # check rows
        x_s = []
        o_s = []
        for col in field:
            x_s.append(col[i] == 'X')
            o_s.append(col[i] == 'O')
        if all(x_s):
            if sign == 'X':
                return 10
            else:
                return -10
        elif all(o_s):
            if sign == 'X':
                return -10
            else:
                return 10
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
        if sign == 'X':
            return 10
        else:
            return -10
    elif all(o_s_l) or all(o_s_r):
        if sign == 'X':
            return -10
        else:
            return 10
    for col in field:
        for i in col:
            if i == '_':
                return None
    return 0