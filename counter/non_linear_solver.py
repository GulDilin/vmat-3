import numpy as np
from numpy import sin, cos, tan, arccos, arcsin, arctan, abs

class SignError(Exception):
    pass


class FirstDiffSignError(Exception):
    pass


class SecondDiffSignError(Exception):
    pass


def diff_all_dots(y, x):
    return [(y[i] - y[i - 1]) / (x[i] - x[i - 1]) for i in range(1, len(y))], x[1:]


def count_root_hord(f, xx, yy, acc, ax=None):
    y1, x1 = diff_all_dots(yy, xx)
    if sum([0 if el * y1[0] > 0 else 1 for el in y1]) != 0:
        raise FirstDiffSignError('Fist diff should have one sign')
    y2, x2 = diff_all_dots(y1, x1)
    if sum([0 if el * y2[0] > 0 else 1 for el in y2]) != 0:
        raise SecondDiffSignError('Second diff should have one sign')
    if yy[0] * yy[-1] >= 0:
        raise SignError('Is not coverage. Function need to have different signs on ends.')

    a = xx[0]
    b = xx[-1]
    is_hord_from_a = (y2[-1] * y1[-1] < 0)
    old_x = b if is_hord_from_a else a
    while True:
        x = old_x
        y = eval(f)
        new_x = x - (b - x) / (yy[-1] - y) * y if not is_hord_from_a else x - (a - x) / (yy[0] - y) * y
        # if ax:
        #     if is_hord_from_a:
        #         ax.plot([xx[0], x], [yy[0], y])
        #     else:
        #         ax.plot([xx[-1], x], [yy[-1], y])
        if abs(new_x - old_x) <= acc:
            return new_x
        old_x = new_x


def count_root_tangent(f, xx, yy, acc, ax=None):
    y1, x1 = diff_all_dots(yy, xx)
    if sum([0 if el * y1[0] > 0 else 1 for el in y1]) != 0:
        raise FirstDiffSignError('Fist diff should have one sign')
    y2, x2 = diff_all_dots(y1, x1)
    if sum([0 if el * y2[0] > 0 else 1 for el in y2]) != 0:
        raise SecondDiffSignError('Second diff should have one sign')
    if yy[0] * yy[-1] >= 0:
        raise SignError('Is not coverage. Function need to have different signs on ends.')

    a = xx[0]
    b = xx[-1]
    old_x = b - yy[-1] / y1[-1]
    while True:
        x = old_x
        y = eval(f)
        d = (old_x - a) / 1000
        x = old_x - d
        y_l = eval(f)
        y1, x1 = diff_all_dots([y_l, y], [x, old_x])
        new_x = old_x - y / y1[-1]
        # if ax:
        #     ax.plot([new_x, old_x], [0, y])
        # print(f'error = {new}')
        if abs(new_x - old_x) <= acc:
            return new_x
        old_x = new_x

def solve_system_newton(f1, f2, yy1, yy2):
    pass