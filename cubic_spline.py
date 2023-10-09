# to construct cubic spline function and draw the picture
# in the file, we test the function sin(x)

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x_value = np.linspace(0, 10, 5)
y_value = np.sin(x_value)

def get_cs_func(x_v, y_v):
    return CubicSpline(x_v, y_v)

def cs_expression(x,y) -> list:
    '''
    get the expression of cubic spline function,which is a segmentation function
    form the left of number axis to the right
    '''
    
    coef = CubicSpline(x, y).c
    
    def coef_to_expression(coefficients):
        x = sp.symbols('x')
        poly = []
        for j in range(len(coefficients[0])):
            # cubic spline function has degree of 3, i.e. len(coefficients) == 4
            poly.append(coefficients[0][j]*x**3+coefficients[1][j]*x**2+coefficients[2][j]*x+coefficients[3][j])
        return poly
    
    return coef_to_expression(coef)

def plot_show(x_v, y_v):
    ''' to draw the picture,in the case we consider interval[0,10] '''
    x_t = np.linspace(0, 10, 100)
    y_t_lag = get_cs_func(x_v, y_v)(x_t)
    y_t_ori = np.sin(x_t)
    
    plt.plot(x_t, y_t_lag, c='y', label='cubic spline of sin(x)')
    plt.plot(x_t, y_t_ori, c='g', label='sin(x)')
    plt.scatter(x_v, y_v, c='b')
    plt.title("sin(x) and its cubic spline ")
    plt.legend()
    plt.show()

print(cs_expression(x_value, y_value))
plot_show(x_value, y_value)
