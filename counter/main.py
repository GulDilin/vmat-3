import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, RadioButtons
import numpy as np
from numpy import sin, cos, tan, arccos, arcsin, arctan, abs
from non_linear_solver import count_root_tangent, count_root_hord, SignError, FirstDiffSignError, SecondDiffSignError
import argparse
import ui_creator

left = -2
right = 2
accuracy = 0.01
RED = "#E35656"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--system', default=False, help='System of equations')
    args = parser.parse_args()
    print(f'args = {args}')

    if 'system' in args and args.system:
        ui = ui_creator.SystemEqCreator()
    else:
        ui = ui_creator.OneEqCreator()
    ui.show()
