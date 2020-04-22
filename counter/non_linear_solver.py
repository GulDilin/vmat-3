import numpy as np
from numpy import sin, cos, tan, arccos, arcsin, arctan, abs, sqrt, exp
import gauss


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
        d = 1.0e-5
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


def jacobian(f, x):
    if len(f) != len(x):
        raise ValueError('f and x need be same length')
    h = 1.0e-5
    n = len(x)
    return [[(f[i](x) - f[i](x[:k] + [x[k] - h] + x[k + 1:])) / h for k in range(n)] for i in range(n)]
    # Jac = np.array([[0 for _ in range(n)] for _ in range(n)])


def newton(f, x, acc):
    if len(f) != len(x):
        raise ValueError('f and x need be same length')
    max_iterations = 100
    old_x = x
    for i in range(max_iterations):
        Jac = jacobian(f, x)
        for i in range(len(Jac)):
            print(Jac[i])
        matrix = [Jac[i] + [f[i](x)] for i in range(len(x))]
        print()
        for i in range(len(matrix)):
            print(matrix[i])
        sys = gauss.SLAU(matrix)
        sys.make_triangle()
        sys.solve()
        dx = sys.solution
        # dx = linalg.solve(Jac, fO)
        x = [x[i] - dx[i] for i in range(len(x))]
        print([abs(x[i] - old_x[i]) for i in range(len(x))])
        print([abs(x[i] - old_x[i]) <= acc for i in range(len(x))])
        if sum([1 if abs(x[i] - old_x[i]) <= acc else 0 for i in range(len(x))]) == len(x):
            return x, i + 1
        old_x = x
    return old_x, max_iterations
