import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
from numpy import sin, cos, tan, arccos, arcsin, arctan, abs
import pylab

left = -2
right = 2
accuracy = 0.01
RED = "#E35656"


def diff_all_dots(y, x):
    return [(y[i] - y[i - 1]) / (x[i] - x[i - 1]) for i in range(1, len(y))], x[1:]


class SignError(Exception):
    pass


class FirstDiffSignError(Exception):
    pass


class SecondDiffSignError(Exception):
    pass


def count_root_hord(f, xx, yy, acc, ax=None):
    if yy[0] * yy[-1] >= 0:
        raise SignError('Is not coverage. Function need to have different signs on ends.')
    y1, x1 = diff_all_dots(yy, xx)
    if sum([0 if el * y1[0] > 0 else 1 for el in y1]) != 0:
        raise FirstDiffSignError('Fist diff should have one sign')
    y2, x2 = diff_all_dots(y1, x1)
    if sum([0 if el * y2[0] > 0 else 1 for el in y2]) != 0:
        raise SecondDiffSignError('Second diff should have one sign')

    a = xx[0]
    b = xx[-1]
    is_hord_from_a = (y2[-1]*y1[-1] < 0)
    print(f'from a = {is_hord_from_a}')
    old_x = b if is_hord_from_a else a
    # old_x = a - (b - a) / (yy[-1] - yy[0]) * yy[0] if not is_hord_from_a else b - (a - b) / (yy[0] - yy[-1]) * yy[-1]
    while True:
        x = old_x
        y = eval(f)
        new_x = x - (b - x) / (yy[-1] - y) * y if not is_hord_from_a else x - (a - x) / (yy[0] - y) * y
        # if ax:
        #     if is_hord_from_a:
        #         ax.plot([xx[0], x], [yy[0], y])
        #     else:
        #         ax.plot([xx[-1], x], [yy[-1], y])
        if new_x - old_x <= acc:
            return new_x
        old_x = new_x


if __name__ == '__main__':
    f = lambda x: - x ** 2 + 1

    delta = (right - left) / 10000
    x = np.arange(left, right + delta, delta, dtype=float)
    y = [f(i) for i in x]
    func_str = "-x ** 2 + 1"
    # plt.ion()

    main_axes = [0.1, 0.05, 0.6, 0.6]
    fig = plt.figure()
    ax = fig.add_axes(main_axes)
    plot, *a = plt.plot(x, y, x, 0 * x)

    plt.grid(True)

    axis1 = (plt.axes([0.85, 0.75, 0.14, 0.05]))
    axis2 = (plt.axes([0.85, 0.65, 0.14, 0.05]))
    axis3 = (plt.axes([0.85, 0.55, 0.14, 0.05]))
    axis4 = (plt.axes([0.15, 0.85, 0.30, 0.05]))
    axis5 = (plt.axes([0.15, 0.75, 0.30, 0.05]))
    axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])

    left_text = TextBox(axis1, 'Left limit', label_pad=0.01)
    right_text = TextBox(axis2, 'Right limit', label_pad=0.01)
    acc_text = TextBox(axis3, 'Accuracy')
    function = TextBox(axis4, 'Function')
    answer = TextBox(axis5, 'Answer x = ')

    answer.color = 'white'
    catulate_btn = Button(axes_button_calculate, "Calculate")
    left_text.set_val("-2")
    right_text.set_val("2")
    function.set_val(func_str)
    acc_text.set_val(accuracy)

    ax.text(0.5, 2.8, "You can use +, -, *, /, **, cos, sin, tan, arc*", fontsize=10)


    def submit_func(text):
        global func_str, x
        try:
            b = eval(text)
            func_str = text
            function.color = "white"
        except RuntimeWarning:
            function.color = RED
            pass
        except Exception:
            function.color = RED
            pass


    def submit_left(text):
        global left, func_str
        try:
            x = float(text)
            b = eval(func_str)
            left = x
            left_text.color = "white"
            update(None)
        except Exception:
            left_text.color = RED
            pass


    def submit_right(text):
        global right, func_str
        try:
            x = float(text)
            b = eval(func_str)
            right = x
            right_text.color = "white"
            update(None)
        except Exception:
            right_text.color = RED
            pass


    def submit_accuracy(text):
        global accuracy, func_str
        try:
            x = float(text)
            if x <= 0:
                raise ValueError("accuracy need to be positive")
            accuracy = x
            acc_text.color = "white"
            update(None)
        except Exception:
            acc_text.color = RED
            pass


    def update(event):
        global plot
        global ax, x, y
        delta = (right - left) / 1000
        x = np.arange(left, right + delta, delta, dtype=float)
        y = eval(func_str)
        plot.remove()
        plt.delaxes(ax)
        ax = fig.add_axes(main_axes)
        plot, *a = ax.plot(x, y)
        ax.plot(x, 0 * x)
        plt.grid(True)
        plt.draw()


    def calculate_root(event):
        global func_str, y, x, ax, accuracy
        update(None)
        try:
            root = count_root_hord(func_str, yy=y, xx=x, acc=accuracy, ax=ax)
            answer.set_val(root)
            ax.scatter(root, 0, color="black")
        except Exception:
            ax.text(0, 0, 'Does not coverage', style='italic',
                bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})



    left_text.on_text_change(submit_left)
    right_text.on_text_change(submit_right)
    function.on_text_change(submit_func)
    acc_text.on_text_change(submit_accuracy)
    catulate_btn.on_clicked(calculate_root)
    plt.show()
