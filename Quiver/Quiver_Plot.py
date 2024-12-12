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

U += 0.2 * np.random.randn(*X.shape)                                        # We can add some noise to make it more realistic
V += 0.2 * np.random.randn(*X.shape)


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
    global U,V                                                                  # just for demonstration of global keyword
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
    plt.quiver(X, Y, U, V, magnitude, pivot= 'middle', units= 'xy', color= 'r', angles= 'xy', width= 0.025)
    runtheplot('Usage of pivot, units, color, angles, width')


def quiver_plot_6():
    '''This function saves the quiver plot              ...yeah that's what it do :)
    This function is a quiver plot of Earth's wind rotation'''
    
    # Generate a grid of points
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)

    # Define the vector field (Coriolis effect)
    U = -Y / np.sqrt(X**2 + Y**2)  # Simplified vector field
    V = X / np.sqrt(X**2 + Y**2)

    # Avoid division by zero
    U[np.isinf(U)] = 0
    V[np.isinf(V)] = 0
    U[np.isnan(U)] = 0
    V[np.isnan(V)] = 0

    # Calculate the magnitude for coloring
    magnitude = np.sqrt(U**2 + V**2)

    # Create the quiver plot with specified attributes
    plt.figure(figsize=(10, 10))
    plt.quiver(X, Y, U, V, magnitude, scale=50, scale_units='xy', angles='xy', cmap='viridis', alpha=0.8, headwidth=4, headlength=6, headaxislength=5, pivot='middle')
    plt.colorbar(label='Magnitude')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Quiver Plot of Earth\'s Wind Rotation (Coriolis Effect)')
    
    # Save the plot to a file; we can't do it if we use runtheplot() as show() terminates the figure after showing
    plt.savefig('earth_wind_rotation_quiver_plot.png')                          
    plt.show()



# Main
# quiver_info()
# quiver_plot_1()
# quiver_plot_2()
# quiver_plot_3()
# quiver_plot_4()
# quiver_plot_5()
quiver_plot_6()


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

