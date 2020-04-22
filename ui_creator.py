import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, RadioButtons
import numpy as np
from numpy import sin, cos, tan, arccos, arcsin, arctan, abs, cbrt, sqrt, exp
from counter.non_linear_solver import (count_root_tangent,
                                       count_root_hord,
                                       SignError,
                                       FirstDiffSignError,
                                       SecondDiffSignError,
                                       newton)

RED = "#E35656"


# class OneEqCreator:
#     def __init__(self):
#         self.left = -2
#         self.right = 2
#         self.accuracy = 0.01
#         self.is_hord = True
#         f = lambda x: - x ** 2 + 1
#         self.delta = (self.right - self.left) / 10000
#         self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
#         self.y = [f(i) for i in self.x]
#         self.func_str = "-x ** 2 + 1"
#         self.main_axes = [0.1, 0.05, 0.6, 0.6]
#         self.fig = plt.figure()
#         self.ax = self.fig.add_axes(self.main_axes)
#         self.plot, *a = plt.plot(self.x, self.y, self.x, 0 * self.x, 0 * self.x, self.y)
#
#         # print(f'plot = {plot}')
#         plt.grid(True)
#
#         axis1 = (plt.axes([0.85, 0.75, 0.14, 0.05]))
#         axis2 = (plt.axes([0.85, 0.65, 0.14, 0.05]))
#         axis3 = (plt.axes([0.85, 0.55, 0.14, 0.05]))
#         axes_f1 = (plt.axes([0.15, 0.9, 0.30, 0.05]))
#         axes_answer = (plt.axes([0.15, 0.75, 0.30, 0.05]))
#         axes_answer_i = (plt.axes([0.15, 0.83, 0.30, 0.05]))
#         axis6 = (plt.axes([0.75, 0.25, 0.2, 0.25]))
#         axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])
#
#         self.left_text = TextBox(axis1, 'Left limit', label_pad=0.01)
#         self.right_text = TextBox(axis2, 'Right limit', label_pad=0.01)
#         self.acc_text = TextBox(axis3, 'Accuracy')
#         self.function = TextBox(axes_f1, 'Function')
#         self.answer = TextBox(axes_answer, 'Answer x = ')
#         self.answer_i = TextBox(axes_answer_i, 'Iterations = ')
#         self.hord_radio = RadioButtons(axis6, ["Hord", "Tangent"], active=0)
#         self.catulate_btn = Button(axes_button_calculate, "Calculate")
#
#     def radio_action(self, event):
#         self.is_hord = event == 'Hord'
#
#     def submit_func(self, text):
#         try:
#             x = self.x
#             b = eval(text)
#             self.func_str = text
#             self.function.color = "white"
#             # update(None)
#         except Exception as e:
#             print(str(e))
#             self.function.color = RED
#             pass
#
#     def submit_left(self, text):
#         global left, func_str
#         try:
#             x = float(text)
#             b = eval(self.func_str)
#             self.left = x
#             self.left_text.color = "white"
#             self.update(None)
#         except Exception as e:
#             print(str(e))
#             self.left_text.color = RED
#             pass
#
#     def submit_right(self, text):
#         try:
#             x = float(text)
#             b = eval(self.func_str)
#             self.right = x
#             self.right_text.color = "white"
#             self.update(None)
#         except Exception as e:
#             print(str(e))
#             self.right_text.color = RED
#             pass
#
#     def submit_accuracy(self, text):
#         try:
#             x = float(text)
#             if x <= 0:
#                 raise ValueError("accuracy need to be positive")
#             self.accuracy = x
#             self.acc_text.color = "white"
#             self.update(None)
#         except Exception as e:
#             print(str(e))
#             self.acc_text.color = RED
#             pass
#
#     def update(self, event):
#         self.delta = (self.right - self.left) / 1000
#         self.x = np.arange(self.left, self.right + self.delta, self.delta, dtype=float)
#         x = self.x
#         self.y = eval(self.func_str)
#         self.plot.remove()
#         plt.delaxes(self.ax)
#         self.ax = self.fig.add_axes(self.main_axes)
#         self.plot, *a = self.ax.plot(self.x, self.y)
#         self.ax.plot(self.x, 0 * self.x)
#         if self.x[0] <= 0 <= self.x[-1] or self.x[0] >= 0 >= self.x[-1]:
#             self.ax.plot(0 * self.x, self.y)
#         plt.grid(True)
#         plt.draw()
#
#     def calculate_root(self, event):
#         self.update(None)
#         try:
#             if self.is_hord:
#                 root, i = count_root_hord(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy, ax=self.ax)
#             else:
#                 root, i = count_root_tangent(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy, ax=self.ax)
#             self.answer.set_val(root)
#             self.answer_i.set_val(i)
#             self.ax.scatter(root, 0, color="black")
#         except SignError:
#             self.ax.text(self.x[0], self.y[0], 'No roots', style='italic',
#                          bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
#         except Exception:
#             self.ax.text(self.x[0], self.y[0], 'Does not coverage', style='italic',
#                          bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
#
#     def show(self):
#         self.answer.color = 'white'
#         self.left_text.set_val("-2")
#         self.right_text.set_val("2")
#         self.function.set_val(self.func_str)
#         self.acc_text.set_val(self.accuracy)
#         self.ax.text(0.5, 3.8, "You can use +, -, *, /, **, cos, sin, tan, arc*", fontsize=10)
#
#         self.left_text.on_text_change(self.submit_left)
#         self.right_text.on_text_change(self.submit_right)
#         self.function.on_text_change(self.submit_func)
#         self.acc_text.on_text_change(self.submit_accuracy)
#         self.catulate_btn.on_clicked(self.calculate_root)
#         self.hord_radio.on_clicked(self.radio_action)
#         plt.show()


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

        plt.grid(True)

        axis1 = (plt.axes([0.65, 0.92, 0.3, 0.05]))
        axis2 = (plt.axes([0.65, 0.85, 0.3, 0.05]))
        axis3 = (plt.axes([0.65, 0.78, 0.3, 0.05]))
        axis_error = (plt.axes([0.65, 0.71, 0.3, 0.05]))
        axes_f1 = (plt.axes([0.15, 0.92, 0.30, 0.05]))
        axes_answer = (plt.axes([0.15, 0.78, 0.30, 0.05]))
        axes_answer_i = (plt.axes([0.15, 0.85, 0.30, 0.05]))
        axes_answer_y = (plt.axes([0.15, 0.71, 0.30, 0.05]))
        axis6 = (plt.axes([0.75, 0.25, 0.2, 0.25]))
        axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])

        self.left_text = TextBox(axis1, 'Left limit ', label_pad=0.01)
        self.right_text = TextBox(axis2, 'Right limit ', label_pad=0.01)
        self.acc_text = TextBox(axis3, 'Accuracy ')
        self.function = TextBox(axes_f1, 'Function ')
        self.answer = TextBox(axes_answer, 'Answer x = ')
        self.answer_error = TextBox(axis_error, 'Got error = ')
        self.answer_i = TextBox(axes_answer_i, 'Iterations = ')
        self.answer_y = TextBox(axes_answer_y, 'Answer y = ')
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
        if self.left * self.right < 0:
            self.ax.plot([0, 0], [max(self.y), min([*self.y, 0])])
        plt.grid(True)
        plt.draw()

    def calculate_root(self, event):
        self.update(None)
        try:
            if self.is_hord:
                root, i, e = count_root_hord(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy)
            else:
                root, i, e = count_root_tangent(self.func_str, yy=self.y, xx=self.x, acc=self.accuracy)
            self.answer.set_val(root)
            self.answer_i.set_val(i)
            self.ax.scatter(root, 0, color="black")
            x = root
            self.answer_y.set_val(eval(self.func_str))
            self.answer_error.set_val(e)
        except SignError:
            self.ax.text(self.x[0], self.y[0], 'No roots', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        except Exception:
            self.ax.text(self.x[0], self.y[0], 'Does not coverage', style='italic',
                         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    def show(self):
        self.answer_y.active = False
        self.answer.active = False
        self.answer_i.active = False
        self.answer_error.active = False

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
        self.x1 = 2
        self.x2 = 2
        self.accuracy = 0.01

        self.funcs = [{'f': lambda x: x[0] ** 2 - 2 * x[0] + x[1] - 3,
                       'x2': lambda x1: - x1 ** 2 + 2 * x1 + 3,
                       'name': "x1^2 - 2 x1 + x2 = 3"},
                      {'f': lambda x: - 2 * x[0] ** 2 - 3 * x[0] + x[1] + 4,
                       'x2': lambda x1: 2 * x1 ** 2 + 3 * x1 - 4,
                       'name': "2 x1^2 - 3 x1 + x2 = -4"},
                      {'f': lambda x: x[1] - 2 * exp(x[0]) + 1,
                       'x2': lambda x1: 2 * exp(x1) - 1,
                       'name': 'x2 - 2 e^x1 = -1'},
                      {'f': lambda x: sin(x[0] ** 3) + x[1] - 2,
                       'x2': lambda x1: (2 - sin(x1 ** 3)),
                       'name': "sin(x1 ^ 3) + x2 = 2"},
                      {'f': lambda x: 2 * x[0] ** 3 - x[0] ** 2 - x[1] / 3 - 6,
                       'x2': lambda x1: 3 * (2 * x1 ** 3 - x1 ** 2 - 6),
                       'name': '2 x1^3 - x1^2 - x2 /3 = 6'}
                      ]
        self.func_indexes = {el['name']: ind for ind, el in enumerate(self.funcs, 0)}
        self.main_axes = [0.1, 0.05, 0.6, 0.6]
        self.fig = plt.figure()
        self.x = np.arange(self.x1 - 5, self.x1 + 5, 1e-2)
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot1, *a = plt.plot(self.x, self.funcs[0]['x2'](self.x))
        self.plot2, *a = plt.plot(self.x, self.funcs[1]['x2'](self.x))

        plt.grid(True)

        axis1 = (plt.axes([0.85, 0.45, 0.14, 0.05]))
        axis2 = (plt.axes([0.85, 0.35, 0.14, 0.05]))
        axis3 = (plt.axes([0.85, 0.25, 0.14, 0.05]))
        axes_f1 = (plt.axes([0.5, 0.67, 0.25, 0.3]))
        axes_f2 = (plt.axes([0.75, 0.67, 0.25, 0.3]))
        axes_answer_x = (plt.axes([0.15, 0.75, 0.30, 0.05]))
        axes_answer_y = (plt.axes([0.15, 0.67, 0.30, 0.05]))
        axes_answer_i = (plt.axes([0.15, 0.83, 0.30, 0.05]))
        axes_button_calculate = plt.axes([0.72, 0.05, 0.25, 0.075])

        self.x1_text = TextBox(axis1, 'Start x1', label_pad=0.01)
        self.x2_text = TextBox(axis2, 'Start x2', label_pad=0.01)
        self.acc_text = TextBox(axis3, 'Accuracy')
        self.answer_x = TextBox(axes_answer_x, 'Answer x1 = ')
        self.answer_y = TextBox(axes_answer_y, 'Answer y2 = ')
        self.answer_i = TextBox(axes_answer_i, 'Iterations = ')
        self.catulate_btn = Button(axes_button_calculate, "Calculate")
        self.radio_f1 = RadioButtons(axes_f1, [el['name'] for el in self.funcs], active=0)
        self.radio_f2 = RadioButtons(axes_f2, [el['name'] for el in self.funcs], active=1)

    def radio_action_1(self, event):
        if self.radio_f1.value_selected == self.radio_f2.value_selected:
            self.radio_f2.set_active((self.func_indexes[event] + 1) % len(self.funcs))
        self.update(None)

    def radio_action_2(self, event):
        if self.radio_f1.value_selected == self.radio_f2.value_selected:
            self.radio_f1.set_active((self.func_indexes[event] + 1) % len(self.funcs))
        self.update(None)

    def submit_x1(self, text):
        try:
            self.x1 = float(text)
            self.x1_text.color = "white"
        except Exception as e:
            print(str(e))
            self.x1_text.color = RED
            pass

    def submit_x2(self, text):
        try:
            self.x2 = float(text)
            self.x2_text.color = "white"
        except Exception as e:
            print(str(e))
            self.x2_text.color = RED
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
        self.plot1.remove()
        self.plot2.remove()
        plt.delaxes(self.ax)
        self.x = np.arange(self.x1 - 5, self.x1 + 5, 1e-2)
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot1, *a = plt.plot(self.x, self.funcs[self.func_indexes[self.radio_f1.value_selected]]['x2'](self.x))
        self.plot2, *a = plt.plot(self.x, self.funcs[self.func_indexes[self.radio_f2.value_selected]]['x2'](self.x))
        plt.grid(True)
        plt.draw()

    def calculate_root(self, event):
        # try:
        root, iter_count = newton([self.funcs[self.func_indexes[self.radio_f1.value_selected]]['f'],
                                   self.funcs[self.func_indexes[self.radio_f2.value_selected]]['f']],
                                  [self.x1, self.x2],
                                  self.accuracy)
        self.answer_x.set_val(root[0])
        self.answer_y.set_val(root[1])
        self.answer_i.set_val(iter_count)

        self.plot1.remove()
        self.plot2.remove()
        plt.delaxes(self.ax)
        self.x = np.arange(root[0] - 2, root[0] + 2, 1e-2)
        self.ax = self.fig.add_axes(self.main_axes)
        self.plot1, *a = plt.plot(self.x, self.funcs[self.func_indexes[self.radio_f1.value_selected]]['x2'](self.x))
        self.plot2, *a = plt.plot(self.x, self.funcs[self.func_indexes[self.radio_f2.value_selected]]['x2'](self.x))
        self.ax.scatter(root[0], root[1], color="black")

        plt.grid(True)
        plt.draw()
        # except Exception as e:
        #     print(str(e))

    def show(self):
        self.answer_x.color = 'white'
        self.answer_y.color = 'white'
        self.x1_text.set_val(f"{self.x1}")
        self.x2_text.set_val(f"{self.x2}")
        self.acc_text.set_val(self.accuracy)

        self.x1_text.on_text_change(self.submit_x1)
        self.x2_text.on_text_change(self.submit_x2)
        self.acc_text.on_text_change(self.submit_accuracy)
        self.catulate_btn.on_clicked(self.calculate_root)
        self.radio_f2.on_clicked(self.radio_action_2)
        self.radio_f1.on_clicked(self.radio_action_1)
        plt.show()
