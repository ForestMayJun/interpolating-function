# get lagrange interpolating function with given data and draw the picture
# in the file, I use the date to fit the sin function


import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#given data as np.array form
x_value = np.linspace(0, 10, 8)
y_value = np.sin(x_value)

def lag_func(x_v, y_v):
    ''' giving the data of x and y,returning the sympy expression class,not the function'''
    x = sp.symbols('x')

    def lagrange_pri(i, value = x_value):
        ''' 
        to get the lagrange primary function l_i(x)
        l_i(x_i) == y_i and l_i(x_j) == 0 if j != i
        '''
        x_new = np.concatenate((value[:i], value[i+1:]))  # remove the element of the order i
        
        numera = np.prod(x - x_new)
        denomi = np.prod(value[i] - x_new)
        return numera/denomi
    
    index_list = np.arange(len(x_v))
    bases = list(map(lagrange_pri, index_list))
    f = np.dot(y_v, bases)
    
    return f

def lag_func_expression(x_v, y_v):
    ''' return the normal polynomial expression of the function'''
    return sp.expand(lag_func(x_v, y_v))

def get_lag_func(x_v, y_v):
    ''' return the lagrange interpolating function'''
    x = sp.symbols('x')
    return sp.lambdify(x, lag_func(x_v, y_v,), 'numpy')

def plot_show(x_v, y_v):
    ''' to draw the picture,in the case we consider interval[0,10] '''
    x_t = np.linspace(0, 10, 100)
    y_t_lag = get_lag_func(x_v, y_v)(x_t)
    y_t_ori = np.sin(x_t)
    
    plt.plot(x_t, y_t_lag, c='y', label='lagrange interpolating function of sin(x)')
    plt.plot(x_t, y_t_ori, c='g', label='sin(x)')
    plt.title("sin(x) and its lagrange interpolating function ")
    plt.legend()
    plt.show()

plot_show(x_value, y_value)