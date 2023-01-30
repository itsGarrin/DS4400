

import numpy as np
import matplotlib.pyplot as plt


def surface_plot(x, y, f):
    """ Generate a surface plot
    x: x values (np array)
    y: y values (np array)
    f: function f(x,y) """

    X, Y = np.meshgrid(x,y)
    Z = f(X, Y)

    fig = plt.figure(figsize = (8,8))
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.viridis)

    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=0)

    fig.colorbar(surf, shrink=.5, aspect=8)

    plt.show()


# Contour plot of the function

def contour_plot(x, y, f, dfdx, dfdy, gradient_field=False, ascend=None, alpha=0.01):

    X, Y = np.meshgrid(x,y)
    Z = f(X,Y)
    plt.figure(figsize=(8, 8))
    cp = plt.contour(X,Y,Z, 50)


    # Overlay gradient vector field
    if gradient_field:
        for i in x:
            for j in y:
                dx = alpha * dfdx(i, j)
                dy = alpha * dfdy(i, j)
                plt.arrow(i, j, dx, dy, color='blue', linestyle='-')


    # Plot one gradient ascent
    if ascend:
        i, j = ascend

        # Keep going while we stay in range of the plot
        while i >= x.min() and i <= x.max() and j >= y.min() and j <= y.max():
            dx = alpha * dfdx(i,j)
            dy = alpha * dfdy(i,j)           
            plt.arrow(i, j, dx, dy, color='red', linestyle='-')
            i = i + dx
            j = j + dy
            
          
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())
    plt.show()