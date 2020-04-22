import numpy as np
from numpy import sin, cos, tan, arccos, arcsin, arctan, abs, sqrt, exp
import counter.gauss as gauss


class SignError(Exception):
    pass


class FirstDiffSignError(Exception):
    pass


class SecondDiffSignError(Exception):
    pass


def diff_all_dots(y, x):
    return [(y[i] - y[i - 1]) / (x[i] - x[i - 1]) for i in range(1, len(y))], x[1:]


def count_root_hord(f, xx, yy, acc):
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
    from_right = (y2[-1] * y1[-1] < 0)
    iter_count = 0
    old_x = b if from_right else a
    while True:
        iter_count += 1
        x = old_x
        y = eval(f)
        new_x = x - (b - x) / (yy[-1] - y) * y if not from_right else x - (a - x) / (yy[0] - y) * y
        if abs(new_x - old_x) <= acc:
            return new_x, iter_count
        old_x = new_x


def count_root_tangent(f, xx, yy, acc):
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
    iter_count = 0
    while True:
        iter_count += 1
        x = old_x
        y = eval(f)
        d = 1.0e-5
        x = old_x - d
        y_l = eval(f)
        y1, x1 = diff_all_dots([y_l, y], [x, old_x])
        new_x = old_x - y / y1[-1]
        if abs(new_x - old_x) <= acc:
            return new_x, iter_count
        old_x = new_x


def jacobian(f, x):
    if len(f) != len(x):
        raise ValueError('f and x need be same length')
    h = 1.0e-5
    n = len(x)
    return [[(f[i](x) - f[i](x[:k] + [x[k] - h] + x[k + 1:])) / h for k in range(n)] for i in range(n)]


def newton(f, x, acc):
    if len(f) != len(x):
        raise ValueError('f and x need be same length')
    max_iterations = 100
    old_x = x
    for i in range(max_iterations):
        Jac = jacobian(f, x)
        matrix = [Jac[i] + [f[i](x)] for i in range(len(x))]

        sys = gauss.SLAU(matrix)
        sys.make_triangle()
        sys.solve()
        dx = sys.solution
        x = [x[i] - dx[i] for i in range(len(x))]

        if sum([1 if abs(x[i] - old_x[i]) <= acc else 0 for i in range(len(x))]) == len(x):
            return x, i + 1
        old_x = x
    return old_x, max_iterations
