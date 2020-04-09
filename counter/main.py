import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, RadioButtons
import numpy as np
from numpy import sin, cos, tan, arccos, arcsin, arctan, abs
from non_linear_solver import count_root_tangent, count_root_hord, SignError, FirstDiffSignError, SecondDiffSignError
import argparse

left = -2
right = 2
accuracy = 0.01
RED = "#E35656"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--system', default=False, help='System of equations')

    is_hord = True
    f = lambda x: - x ** 2 + 1

    delta = (right - left) / 10000
    x = np.arange(left, right + delta, delta, dtype=float)
    y = [f(i) for i in x]
    func_str = "-x ** 2 + 1"

    main_axes = [0.1, 0.05, 0.6, 0.6]
    fig = plt.figure()
    ax = fig.add_axes(main_axes)
    plot, *a = plt.plot(x, y, x, 0 * x, 0 * x, y)

    plt.grid(True)

    axis1 = (plt.axes([0.85, 0.75, 0.14, 0.05]))
    axis2 = (plt.axes([0.85, 0.65, 0.14, 0.05]))
    axis3 = (plt.axes([0.85, 0.55, 0.14, 0.05]))
    axes_f1 = (plt.axes([0.15, 0.9, 0.30, 0.05]))
    axes_f2 = (plt.axes([0.15, 0.85, 0.30, 0.05]))
    axes_answer = (plt.axes([0.15, 0.75, 0.30, 0.05]))
    axis6 = (plt.axes([0.75, 0.25, 0.30, 0.15]))
    # axis7 = (plt.axes([0.85, 0.35, 0.30, 0.05]))
    axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])

    left_text = TextBox(axis1, 'Left limit', label_pad=0.01)
    right_text = TextBox(axis2, 'Right limit', label_pad=0.01)
    acc_text = TextBox(axis3, 'Accuracy')
    function = TextBox(axes_f1, 'Function')
    answer = TextBox(axes_answer, 'Answer x = ')
    hord_radio = RadioButtons(axis6, ["Hord", "Tangent"], active=0)

    answer.color = 'white'
    catulate_btn = Button(axes_button_calculate, "Calculate")
    left_text.set_val("-2")
    right_text.set_val("2")
    function.set_val(func_str)
    acc_text.set_val(accuracy)

    ax.text(0.5, 3.8, "You can use +, -, *, /, **, cos, sin, tan, arc*", fontsize=10)


    def radio_action(event):
        global is_hord
        is_hord = event == 'Hord'


    def submit_func(text):
        global func_str, x
        try:
            b = eval(text)
            func_str = text
            function.color = "white"
            # update(None)
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
        if x[0] <= 0 <= x[-1] or x[0] >= 0 >= x[-1]:
            ax.plot(0 * x, y)
        plt.grid(True)
        plt.draw()


    def calculate_root(event):
        global func_str, y, x, ax, accuracy
        update(None)
        try:
            root = count_root_hord(func_str, yy=y, xx=x, acc=accuracy, ax=ax) if is_hord else count_root_tangent(
                func_str, yy=y, xx=x, acc=accuracy, ax=ax)
            answer.set_val(root)
            ax.scatter(root, 0, color="black")
        except SignError:
            ax.text(x[0], y[0], 'No roots', style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        except Exception:
            ax.text(x[0], y[0], 'Does not coverage', style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})


    left_text.on_text_change(submit_left)
    right_text.on_text_change(submit_right)
    function.on_text_change(submit_func)
    acc_text.on_text_change(submit_accuracy)
    catulate_btn.on_clicked(calculate_root)
    hord_radio.on_clicked(radio_action)
    plt.show()
