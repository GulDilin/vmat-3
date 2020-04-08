import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
from numpy import sin, cos, log, log2, log10, tan, arccos, arcsin, arctan
import pylab

left = -2
right = 2
accuracy = 0.01
RED = "#E35656"


def diff_all_dots(x, y):
    return [(y[i]-y[i-1])/(x[i]-x[i-1]) for i in range(1, len(y))], x[1:]


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
    axes_button_calculate = plt.axes([0.7, 0.05, 0.25, 0.075])

    left_text = TextBox(axis1, 'Left limit', label_pad=0.01)
    right_text = TextBox(axis2, 'Right limit', label_pad=0.01)
    acc_text = TextBox(axis3, 'Accuracy')
    function = TextBox(axis4, 'Function')
    catulate_btn = Button(axes_button_calculate, "Calculate")
    left_text.set_val("-2")
    right_text.set_val("2")
    function.set_val(func_str)
    acc_text.set_val(accuracy)


    def submit_func(text):
        global func_str, x
        try:
            eval(text)
            func_str = text
            function.color = "white"
        except Exception:
            function.color = RED
            pass


    def submit_left(text):
        global left, func_str
        try:
            x = float(text)
            eval(func_str)
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
            eval(func_str)
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
        global ax
        delta = (right - left) / 1000
        x = np.arange(left, right + delta, delta, dtype=float)
        # y = [f(i) for i in x]
        y = eval(func_str)
        plot.remove()
        plt.delaxes(ax)
        ax = fig.add_axes(main_axes)
        plot, *a = ax.plot(x, y)
        ax.plot(x, 0 * x)
        plt.grid(True)
        # ax.plot(x, y, x, 0 * x)
        # plot.set_xdata(x)
        # plot.set_ydata(y)
        plt.draw()


    left_text.on_text_change(submit_left)
    right_text.on_text_change(submit_right)
    function.on_text_change(submit_func)
    acc_text.on_text_change(submit_accuracy)
    catulate_btn.on_clicked(update)
    plt.show()
