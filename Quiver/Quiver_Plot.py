# Here we are fabricating functions that shows usage of quiver plot

# imports
import matplotlib.pyplot as plt
import numpy as np


# literals
plt.rcParams['figure.figsize'] = (13, 9)
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)                                                  # Generates a grid of points
X, Y = np.meshgrid(x, y)

U = -Y                                                                      # Define initial vector directions
V = X

# U += 0.2 * np.random.randn(*X.shape)                                        # We can add some noise to make it more realistic
# V += 0.2 * np.random.randn(*X.shape)


# defined
def runtheplot(title):
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title(title)
    plt.show()


def quiver_info():
    sp = '~'*100
    print(f"The value for x is -> {x}\n\n\t\tand\n\nThe value for y is -> {y}\n\n")
    print(f"{sp}\n\nThe value for X[meshgrid] is -> {X}\n\n\t\tand\n\nThe value for Y[meshgrid] is -> {Y}\n\n")
    print(f"{sp}\n\nThe value for U[-Y] is -> {U}\n\n\n\nThe value for V[X] is -> {V}\n\n")
    

def quiver_plot_1():
    plt.quiver(X, Y, U, V)
    runtheplot('Basic Quiver Plot')
    
def quiver_plot_2():
    global U,V                                                                  # just for demonstration of global keyword - if the global ones are commented
    U += 0.2 * np.random.randn(*X.shape)                                        # We can add some noise to make it more realistic
    V += 0.2 * np.random.randn(*X.shape)
    plt.quiver(X, Y, U, V)
    runtheplot('Quiver Plot With U,V Variation')


def quiver_plot_3():
    '''This function uses Scale, Scale_Units, Angles, c and Cmap'''
    magnitude= np.sqrt(U**2 + V**2)
    plt.quiver(X, Y, U, V, magnitude, scale= 40, scale_units= 'xy', angles= 'xy', cmap= 'jet')
    plt.colorbar(label= 'Magnitude')
    runtheplot('Usage of Scale, Scale_Units, Angles, c and Cmap')


def quiver_plot_4():
    '''This function uses alpha, width, headwidth, headlength, headaxislength'''
    plt.quiver(X, Y, U, V, alpha= 0.5, width= 0.005, headwidth= 5, headlength= 7, headaxislength= 4)
    runtheplot('Usage of alpha, width, headwidth, headlength, headaxislength')

def quiver_plot_5():
    '''This function uses pivot, units'''
    magnitude= np.sqrt(U**2 + V**2)
    plt.quiver(X, Y, U, V, magnitude, pivot= 'middle', units= 'xy', angles= 'xy', width= 0.025)
    runtheplot('Usage of pivot, units, color, angles, width')


def quiver_plot_6():
    '''This function saves the quiver plot              ...yeah that's what it do :)
    This function is a quiver plot that uses basic attributes of quiver_plot and saves the plot'''
    
    global U,V                                                                  # just for demonstration of global keyword - if the global ones are commented
    U += 0.2 * np.random.randn(*X.shape)                                        # We can add some noise to make it more realistic
    V += 0.2 * np.random.randn(*X.shape)

    # Calculate the magnitude for coloring
    magnitude = np.sqrt(U**2 + V**2)

    # Create the quiver plot with specified attributes
    # plt.figure(figsize=(10, 10))                                              # not necessary if we've already manipulated default figure size
    plt.quiver(X, Y, U, V, magnitude, scale=50, scale_units='xy', angles='xy', cmap='plasma', alpha=0.8, headwidth=4, headlength=6, headaxislength=5, pivot='middle')
    plt.colorbar(label='Magnitude')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Wind Patterns Around a Low-Pressure System')

    # Save the plot to a file
    plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Quiver\Single_Quiver_Plot.png")         # we can give dpi = 100; 100 is default, 150-200 is optimal; even 30akes 0 tbit time to load online, 600 qill cook :p
    plt.show()


def quiver_plot_7():
    '''This function shows graph having two Quiver Plots'''

    # Define two different vector fields
    U1, V1 = -Y, X  # First vector field
    U2, V2 = Y, -X  # Second vector field (opposite direction)

    # Add some noise to make it more realistic
    U1 += 0.2 * np.random.randn(*X.shape)
    V1 += 0.2 * np.random.randn(*X.shape)
    U2 += 0.2 * np.random.randn(*X.shape)
    V2 += 0.2 * np.random.randn(*X.shape)

    # First quiver plot
    any_variable = plt.quiver(X, Y, U1, V1, color='blue', alpha=0.6, headwidth=4, headlength=6, headaxislength=5, pivot='middle', label='Field 1')

    # Second quiver plot
    plt.quiver(X, Y, U2, V2, color='red', alpha=0.6, headwidth=4, headlength=6, headaxislength=5, pivot='middle', label='Field 2')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Overlay of Two Quiver Plots')
    plt.legend()
    # plt.colorbar()                                                                                                            # not necessary as static colors were already given to fields, also, there isn't any fuzzy(ranging/unclear/mixed) color variation 

    plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Quiver\Multi_Quiver_Plot.png")         # we can give dpi = 100; 100 is default, 150-200 is optimal; even 30akes 0 tbit time to load online, 600 qill cook :p
    plt.show()


# Main
# quiver_info()
# quiver_plot_1()
# quiver_plot_2()
# quiver_plot_3()
# quiver_plot_4()
# quiver_plot_5()
# quiver_plot_6()
# quiver_plot_7()

# print(quiver_plot_6.__doc__)                        # For demonstration / explaination of docstrings in python

'''

@ Some Attributes and Functions for Quiver Plots:

Basic Attributes:
X, Y: The coordinates of the arrow locations.
U, V: The vector components at each point.

Arrow Properties:
scale: Controls the length of the arrows. Smaller values make the arrows longer.
scale_units: The units for scaling (e.g., xy, inches).
angles: Specifies the angles of the arrows (e.g., xy, uv).

Coloring:
C: An array or list to specify colors for the arrows.
cmap: Colormap used if C is specified.

Alpha:
alpha: Transparency level of the arrows (0 is fully transparent, 1 is fully opaque).

Width and Head:
width: The width of the arrow shafts.
headwidth: The width of the arrow heads.
headlength: The length of the arrow heads.
headaxislength: The length of the head axis.

Pivot:
pivot: The part of the arrow that is anchored to the grid point (e.g., tail, middle, tip).

Units:
units: The units for arrow length (e.g., width, height, dots, inches).

'''

