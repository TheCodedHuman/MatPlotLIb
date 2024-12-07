# Here we are fabricating functions for contour plot

# imports
import matplotlib.pyplot as plt
import numpy as np

# literals
x = np.linspace(-10, 3, 100)
y = np.linspace(-7, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(x**2 + Y**2))
plt.rcParams['figure.figsize'] = (12, 8)

# defined
def contour_info():
    print(f"The value for x is -> {x}\n\n\t\tand\n\nThe value for y is -> {y}\n\n")
    print(f"The value for X is -> {X}\n\n\t\tand\n\nThe value for Y is -> {Y}\n\n\t\tand\n\nThe value for Z is -> {Z}\n\n")
    
def runtheplot(title):
    plt.xlabel('X-Axis')    
    plt.ylabel('Y-Axis')
    plt.title(title)
    plt.show()


def contour_plot_1():
    # plt.contour(X, Y, Z, level=20)
    plt.contour(X, Y, Z, level=100, cmap='autumn')                               # This creates a filled contour plot
    plt.colorbar()
    runtheplot('Basic Contour Plot')


def contour_plot_2():
    pass

# Main
contour_info()
contour_plot_1()
# contour_plot_2()




'''

@ Some Attributes of Contour Plot:

X, Y: The coordinates of the values in Z.
Z: The height values at each (X, Y) pair.
levels: Defines the number and positions of the contour lines or filled areas.
colors: A list of colors to be used for the contour lines.

alpha: Transparency level of the contour lines or filled areas.
cmap: The colormap for the filled contours.
norm: Normalize data values to the colormap.
vmin, vmax: Define the data range that the colormap covers.
extend: Whether contour levels extend below or above the data range ('neither', 'both', 'min', 'max').

corner_mask: Whether to mask the triangles that are partially outside the plot area (True or False).
linewidths: Width of the contour lines.
linestyles: Style of the contour lines ('solid', 'dashed', etc.).
antialiased: Enable or disable anti-aliasing (True or False).
ticks: Positions to put ticks in the colorbar.

'''