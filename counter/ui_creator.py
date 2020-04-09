import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, RadioButtons
import numpy as np
from numpy import sin, cos, tan, arccos, arcsin, arctan, abs
from non_linear_solver import count_root_tangent, count_root_hord, SignError, FirstDiffSignError, SecondDiffSignError

RED = "#E35656"

class OneEqCreator:
    def __init__(self):
        self.left = -2
        self.right = 2
        self.accuracy = 0.01
        self.is_hord = True
        f = lambda x: - x ** 2 + 1
        self.delta = (self.right - self.left) / 10000
        self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
        self.y = [f(i) for i in self.x]
        self.func_str = "-x ** 2 + 1"
        self.main_axes = [0.1, 0.05, 0.6, 0.6]
        self.fig = plt.figure()
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot, *a = plt.plot(self.x, self.y, self.x, 0 * self.x, 0 * self.x, self.y)

        # print(f'plot = {plot}')
        plt.grid(True)

        axis1 = (plt.axes([0.85, 0.75, 0.14, 0.05]))
        axis2 = (plt.axes([0.85, 0.65, 0.14, 0.05]))
        axis3 = (plt.axes([0.85, 0.55, 0.14, 0.05]))
        axes_f1 = (plt.axes([0.15, 0.9, 0.30, 0.05]))
        axes_answer = (plt.axes([0.15, 0.75, 0.30, 0.05]))
        axis6 = (plt.axes([0.75, 0.25, 0.30, 0.15]))
        axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])

        self.left_text = TextBox(axis1, 'Left limit', label_pad=0.01)
        self.right_text = TextBox(axis2, 'Right limit', label_pad=0.01)
        self.acc_text = TextBox(axis3, 'Accuracy')
        self.function = TextBox(axes_f1, 'Function')
        self.answer = TextBox(axes_answer, 'Answer x = ')
        self.hord_radio = RadioButtons(axis6, ["Hord", "Tangent"], active=0)
        self.catulate_btn = Button(axes_button_calculate, "Calculate")

    def radio_action(self, event):
        self.is_hord = event == 'Hord'

    def submit_func(self, text):
        try:
            x = self.x
            b = eval(text)
            self.func_str = text
            self.function.color = "white"
            # update(None)
        except Exception as e:
            print(str(e))
            self.function.color = RED
            pass

    def submit_left(self, text):
        global left, func_str
        try:
            x = float(text)
            b = eval(self.func_str)
            self.left = x
            self.left_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.left_text.color = RED
            pass

    def submit_right(self, text):
        try:
            x = float(text)
            b = eval(self.func_str)
            self.right = x
            self.right_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.right_text.color = RED
            pass

    def submit_accuracy(self, text):
        try:
            x = float(text)
            if x <= 0:
                raise ValueError("accuracy need to be positive")
            self.accuracy = x
            self.acc_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.acc_text.color = RED
            pass

    def update(self, event):
        self.delta = (self.right - self.left) / 1000
        self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
        x = self.x
        self.y = eval(self.func_str)
        self.plot.remove()
        plt.delaxes(self.ax)
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot, *a = self.ax.plot(self.x, self.y)
        self.ax.plot(self.x, 0 * self.x)
        if self.x[0] <= 0 <= self.x[-1] or self.x[0] >= 0 >= self.x[-1]:
            self.ax.plot(0 * self.x, self.y)
        plt.grid(True)
        plt.draw()

    def calculate_root(self, event):
        self.update(None)
        try:
            if self.is_hord:
                root = count_root_hord(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy, ax=self.ax)
            else:
                root = count_root_tangent(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy, ax=self.ax)
            self.answer.set_val(root)
            self.ax.scatter(root, 0, color="black")
        except SignError:
            self.ax.text(self.x[0], self.y[0], 'No roots', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        except Exception:
            self.ax.text(self.x[0], self.y[0], 'Does not coverage', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    def show(self):
        self.answer.color = 'white'
        self.left_text.set_val("-2")
        self.right_text.set_val("2")
        self.function.set_val(self.func_str)
        self.acc_text.set_val(self.accuracy)
        self.ax.text(0.5, 3.8, "You can use +, -, *, /, **, cos, sin, tan, arc*", fontsize=10)

        self.left_text.on_text_change(self.submit_left)
        self.right_text.on_text_change(self.submit_right)
        self.function.on_text_change(self.submit_func)
        self.acc_text.on_text_change(self.submit_accuracy)
        self.catulate_btn.on_clicked(self.calculate_root)
        self.hord_radio.on_clicked(self.radio_action)
        plt.show()


class OneEqCreator:
    def __init__(self):
        self.left = -2
        self.right = 2
        self.accuracy = 0.01
        self.is_hord = True
        f = lambda x: - x ** 2 + 1
        self.delta = (self.right - self.left) / 10000
        self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
        self.y = [f(i) for i in self.x]
        self.func_str = "-x ** 2 + 1"
        self.main_axes = [0.1, 0.05, 0.6, 0.6]
        self.fig = plt.figure()
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot, *a = plt.plot(self.x, self.y, self.x, 0 * self.x, 0 * self.x, self.y)

        # print(f'plot = {plot}')
        plt.grid(True)

        axis1 = (plt.axes([0.85, 0.75, 0.14, 0.05]))
        axis2 = (plt.axes([0.85, 0.65, 0.14, 0.05]))
        axis3 = (plt.axes([0.85, 0.55, 0.14, 0.05]))
        axes_f1 = (plt.axes([0.15, 0.9, 0.30, 0.05]))
        axes_answer = (plt.axes([0.15, 0.75, 0.30, 0.05]))
        axis6 = (plt.axes([0.75, 0.25, 0.30, 0.15]))
        axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])

        self.left_text = TextBox(axis1, 'Left limit', label_pad=0.01)
        self.right_text = TextBox(axis2, 'Right limit', label_pad=0.01)
        self.acc_text = TextBox(axis3, 'Accuracy')
        self.function = TextBox(axes_f1, 'Function')
        self.answer = TextBox(axes_answer, 'Answer x = ')
        self.hord_radio = RadioButtons(axis6, ["Hord", "Tangent"], active=0)
        self.catulate_btn = Button(axes_button_calculate, "Calculate")

    def radio_action(self, event):
        self.is_hord = event == 'Hord'

    def submit_func(self, text):
        try:
            x = self.x
            b = eval(text)
            self.func_str = text
            self.function.color = "white"
            # update(None)
        except Exception as e:
            print(str(e))
            self.function.color = RED
            pass

    def submit_left(self, text):
        global left, func_str
        try:
            x = float(text)
            b = eval(self.func_str)
            self.left = x
            self.left_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.left_text.color = RED
            pass

    def submit_right(self, text):
        try:
            x = float(text)
            b = eval(self.func_str)
            self.right = x
            self.right_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.right_text.color = RED
            pass

    def submit_accuracy(self, text):
        try:
            x = float(text)
            if x <= 0:
                raise ValueError("accuracy need to be positive")
            self.accuracy = x
            self.acc_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.acc_text.color = RED
            pass

    def update(self, event):
        self.delta = (self.right - self.left) / 1000
        self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
        x = self.x
        self.y = eval(self.func_str)
        self.plot.remove()
        plt.delaxes(self.ax)
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot, *a = self.ax.plot(self.x, self.y)
        self.ax.plot(self.x, 0 * self.x)
        if self.x[0] <= 0 <= self.x[-1] or self.x[0] >= 0 >= self.x[-1]:
            self.ax.plot(0 * self.x, self.y)
        plt.grid(True)
        plt.draw()

    def calculate_root(self, event):
        self.update(None)
        try:
            if self.is_hord:
                root = count_root_hord(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy, ax=self.ax)
            else:
                root = count_root_tangent(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy, ax=self.ax)
            self.answer.set_val(root)
            self.ax.scatter(root, 0, color="black")
        except SignError:
            self.ax.text(self.x[0], self.y[0], 'No roots', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        except Exception:
            self.ax.text(self.x[0], self.y[0], 'Does not coverage', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    def show(self):
        self.answer.color = 'white'
        self.left_text.set_val("-2")
        self.right_text.set_val("2")
        self.function.set_val(self.func_str)
        self.acc_text.set_val(self.accuracy)
        self.ax.text(0.5, 3.8, "You can use +, -, *, /, **, cos, sin, tan, arc*", fontsize=10)

        self.left_text.on_text_change(self.submit_left)
        self.right_text.on_text_change(self.submit_right)
        self.function.on_text_change(self.submit_func)
        self.acc_text.on_text_change(self.submit_accuracy)
        self.catulate_btn.on_clicked(self.calculate_root)
        self.hord_radio.on_clicked(self.radio_action)
        plt.show()


class OneEqCreator:
    def __init__(self):
        self.left = -2
        self.right = 2
        self.accuracy = 0.01
        self.is_hord = True
        f = lambda x: - x ** 2 + 1
        self.delta = (self.right - self.left) / 10000
        self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
        self.y = [f(i) for i in self.x]
        self.func_str = "-x ** 2 + 1"
        self.main_axes = [0.1, 0.05, 0.6, 0.6]
        self.fig = plt.figure()
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot, *a = plt.plot(self.x, self.y, self.x, 0 * self.x, 0 * self.x, self.y)

        # print(f'plot = {plot}')
        plt.grid(True)

        axis1 = (plt.axes([0.85, 0.75, 0.14, 0.05]))
        axis2 = (plt.axes([0.85, 0.65, 0.14, 0.05]))
        axis3 = (plt.axes([0.85, 0.55, 0.14, 0.05]))
        axes_f1 = (plt.axes([0.15, 0.9, 0.30, 0.05]))
        axes_answer = (plt.axes([0.15, 0.75, 0.30, 0.05]))
        axis6 = (plt.axes([0.75, 0.25, 0.30, 0.15]))
        axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])

        self.left_text = TextBox(axis1, 'Left limit', label_pad=0.01)
        self.right_text = TextBox(axis2, 'Right limit', label_pad=0.01)
        self.acc_text = TextBox(axis3, 'Accuracy')
        self.function = TextBox(axes_f1, 'Function')
        self.answer = TextBox(axes_answer, 'Answer x = ')
        self.hord_radio = RadioButtons(axis6, ["Hord", "Tangent"], active=0)
        self.catulate_btn = Button(axes_button_calculate, "Calculate")

    def radio_action(self, event):
        self.is_hord = event == 'Hord'

    def submit_func(self, text):
        try:
            x = self.x
            b = eval(text)
            self.func_str = text
            self.function.color = "white"
            # update(None)
        except Exception as e:
            print(str(e))
            self.function.color = RED
            pass

    def submit_left(self, text):
        global left, func_str
        try:
            x = float(text)
            b = eval(self.func_str)
            self.left = x
            self.left_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.left_text.color = RED
            pass

    def submit_right(self, text):
        try:
            x = float(text)
            b = eval(self.func_str)
            self.right = x
            self.right_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.right_text.color = RED
            pass

    def submit_accuracy(self, text):
        try:
            x = float(text)
            if x <= 0:
                raise ValueError("accuracy need to be positive")
            self.accuracy = x
            self.acc_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.acc_text.color = RED
            pass

    def update(self, event):
        self.delta = (self.right - self.left) / 1000
        self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
        x = self.x
        self.y = eval(self.func_str)
        self.plot.remove()
        plt.delaxes(self.ax)
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot, *a = self.ax.plot(self.x, self.y)
        self.ax.plot(self.x, 0 * self.x)
        if self.x[0] <= 0 <= self.x[-1] or self.x[0] >= 0 >= self.x[-1]:
            self.ax.plot(0 * self.x, self.y)
        plt.grid(True)
        plt.draw()

    def calculate_root(self, event):
        self.update(None)
        try:
            if self.is_hord:
                root = count_root_hord(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy, ax=self.ax)
            else:
                root = count_root_tangent(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy, ax=self.ax)
            self.answer.set_val(root)
            self.ax.scatter(root, 0, color="black")
        except SignError:
            self.ax.text(self.x[0], self.y[0], 'No roots', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        except Exception:
            self.ax.text(self.x[0], self.y[0], 'Does not coverage', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    def show(self):
        self.answer.color = 'white'
        self.left_text.set_val("-2")
        self.right_text.set_val("2")
        self.function.set_val(self.func_str)
        self.acc_text.set_val(self.accuracy)
        self.ax.text(0.5, 3.8, "You can use +, -, *, /, **, cos, sin, tan, arc*", fontsize=10)

        self.left_text.on_text_change(self.submit_left)
        self.right_text.on_text_change(self.submit_right)
        self.function.on_text_change(self.submit_func)
        self.acc_text.on_text_change(self.submit_accuracy)
        self.catulate_btn.on_clicked(self.calculate_root)
        self.hord_radio.on_clicked(self.radio_action)
        plt.show()


class SystemEqCreator:
    def __init__(self):
        self.left = -2
        self.right = 2
        self.accuracy = 0.01

        f1 = lambda x: - x ** 2 + 1
        f2 = lambda x: x - 2
        self.delta = (self.right - self.left) / 10000
        self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
        self.y1 = [f1(i) for i in self.x]
        self.y2 = [f2(i) for i in self.x]
        self.func1_str = "-x ** 2 + 1"
        self.func2_str = "x - 2"
        self.main_axes = [0.1, 0.05, 0.6, 0.6]
        self.fig = plt.figure()
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot1, *a = plt.plot(self.x, self.y1)
        self.plot2, *a = plt.plot(self.x, self.y2)

        plt.grid(True)

        axis1 = (plt.axes([0.85, 0.75, 0.14, 0.05]))
        axis2 = (plt.axes([0.85, 0.65, 0.14, 0.05]))
        axis3 = (plt.axes([0.85, 0.55, 0.14, 0.05]))
        axes_f1 = (plt.axes([0.15, 0.9, 0.30, 0.05]))
        axes_f2 = (plt.axes([0.15, 0.83, 0.30, 0.05]))
        axes_answer_x = (plt.axes([0.15, 0.75, 0.30, 0.05]))
        axes_answer_y = (plt.axes([0.15, 0.67, 0.30, 0.05]))
        axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])

        self.left_text = TextBox(axis1, 'Left limit', label_pad=0.01)
        self.right_text = TextBox(axis2, 'Right limit', label_pad=0.01)
        self.acc_text = TextBox(axis3, 'Accuracy')
        self.function1 = TextBox(axes_f1, 'Function 1')
        self.function2 = TextBox(axes_f2, 'Function 2')
        self.answer_x = TextBox(axes_answer_x, 'Answer x = ')
        self.answer_y = TextBox(axes_answer_y, 'Answer y = ')
        self.catulate_btn = Button(axes_button_calculate, "Calculate")

    def submit_func1(self, text):
        try:
            x = self.x
            b = eval(text)
            self.func1_str = text
            self.function1.color = "white"
            # update(None)
        except Exception as e:
            print(str(e))
            self.function1.color = RED
            pass

    def submit_func2(self, text):
        try:
            x = self.x
            b = eval(text)
            self.func2_str = text
            self.function2.color = "white"
            # update(None)
        except Exception as e:
            print(str(e))
            self.function2.color = RED
            pass

    def submit_left(self, text):
        global left, func_str
        try:
            x = float(text)
            b = eval(self.func1_str)
            b = eval(self.func2_str)
            self.left = x
            self.left_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.left_text.color = RED
            pass

    def submit_right(self, text):
        try:
            x = float(text)
            b = eval(self.func1_str)
            b = eval(self.func2_str)
            self.right = x
            self.right_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.right_text.color = RED
            pass

    def submit_accuracy(self, text):
        try:
            x = float(text)
            if x <= 0:
                raise ValueError("accuracy need to be positive")
            self.accuracy = x
            self.acc_text.color = "white"
            self.update(None)
        except Exception as e:
            print(str(e))
            self.acc_text.color = RED
            pass

    def update(self, event):
        self.delta = (self.right - self.left) / 1000
        self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
        x = self.x
        self.y1 = eval(self.func1_str)
        self.y2 = eval(self.func2_str)
        self.plot1.remove()
        self.plot2.remove()
        plt.delaxes(self.ax)
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot1, *a = self.ax.plot(self.x, self.y1)
        self.plot2, *a = self.ax.plot(self.x, self.y2)
        plt.grid(True)
        plt.draw()

    def calculate_root(self, event):
        self.update(None)
        try:
            root = 0
            self.answer_x.set_val(root)
            self.ax.scatter(root, 0, color="black")
        except SignError:
            self.ax.text(self.x[0], self.y[0], 'No roots', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        except Exception:
            self.ax.text(self.x[0], self.y[0], 'Does not coverage', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    def show(self):
        self.answer_x.color = 'white'
        self.answer_y.color = 'white'
        self.left_text.set_val("-2")
        self.right_text.set_val("2")
        self.function1.set_val(self.func1_str)
        self.function2.set_val(self.func2_str)
        self.acc_text.set_val(self.accuracy)
        self.ax.text(0.5, 3.8, "You can use +, -, *, /, **, cos, sin, tan, arc*", fontsize=10)

        self.left_text.on_text_change(self.submit_left)
        self.right_text.on_text_change(self.submit_right)
        self.function1.on_text_change(self.submit_func1)
        self.function2.on_text_change(self.submit_func2)
        self.acc_text.on_text_change(self.submit_accuracy)
        self.catulate_btn.on_clicked(self.calculate_root)
        plt.show()
