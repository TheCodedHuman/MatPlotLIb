# Here we are fabricating functions for contour plot


# imports
from os import system, name
import matplotlib.pyplot as plt
import numpy as np


# literals
x = np.linspace(-10, 3, 100)
y = np.linspace(-7, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(x**2 + Y**2))                        # Notice the + sign in between
plt.rcParams['figure.figsize'] = (10, 6)


# defined
def klear(): system('cls' if name=='nt' else 'clear')   # better not use name, system identifier name anywhere else to handle contradictions

def contour_info():
    sp = '~'*100
    print(f"The value for x is -> {x}\n\n\t\tand\n\nThe value for y is -> {y}\n\n")
    print(f"{sp}\n\nThe value for X is -> {X}\n\n\n\nThe value for Y is -> {Y}\n\n\t\tand\n\nThe value for Z is -> {Z}\n\n")
    
def runtheplot(title):
    '''This function helps in reducing redundancy of xlabel, ylabel, title'''
    plt.xlabel('X-Axis', fontsize=14)    
    plt.ylabel('Y-Axis', fontsize=14)
    plt.title(title, fontsize=16)
    plt.show()


def contour_plot_1():
    '''This creates a basic contour plot'''
    # plt.contour(X, Y, Z)                                # unfilled contour plot - contour()
    plt.contourf(X, Y, Z)                               # filled contour plot - contourf()
    plt.colorbar()
    runtheplot('Basic Contour Plot')


def contour_plot_2():
    '''This function uses levels, colors, zorder, grid'''
    Q = np.arange(-1, 1, 0.1)
    plt.contour(X, Y, Z, levels= Q, zorder= 2)          # levels= 1000 is max before distortions kicks in
    plt.grid(True, zorder= 1)
    plt.colorbar()
    runtheplot("Usage of levels, colors, zorder, grid")


def contour_plot_3():
    '''This function uses alpha, cmap, norm, vmin, vmax'''
    from matplotlib.colors import Normalize
    norm = Normalize(vmin=-1.0, vmax=1.0)

    plt.contourf(X, Y, Z, alpha= 0.7, cmap= 'rainbow', norm=norm,)
    plt.colorbar()
    runtheplot('Usage of alpha, cmap, norm, vmin, vmax')


def contour_plot_4():
    '''This function uses extend, corner_mask, ticks'''
    plt.contourf(X, Y, Z, extend='both', corner_mask=True, levels = 10)
    colorbar = plt.colorbar()
    colorbar.set_label('Z values')                      #Just adding a name to the colorbar

    colorbar.set_ticks([0, 0.2, 0.4, 0.6])
    runtheplot('Usage of extend, corner_mask, ticks')


def contour_plot_5():
    '''This function uses linewidths, linestyles, antialiased'''
    plt.contour(X, Y, Z, linewidths= 1.5, linestyles='dashdot', antialiased=False)
    plt.colorbar()
    runtheplot('Usage of linewidths, linestyles, antialiased')


def contour_plot_6():
    '''This function saves the plot...          yeah, that's it :)'''
    import matplotlib.pyplot as plt
    import numpy as np

    # Data
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x, y)
    Z = np.cos(np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * (X**2 + Y**2))

    # Plotting
    plt.figure(figsize=(12, 8))
    levels = np.linspace(-1.0, 1.0, 50)
    cmap = plt.cm.plasma                                # cmap can be used like this too

    # Filled contour plot
    contour_filled = plt.contourf(X, Y, Z, levels=levels, cmap=cmap, alpha=0.85)
    cbar = plt.colorbar(contour_filled)
    cbar.set_ticks(np.arange(-1.0, 1.1, 0.2))
    cbar.set_label('Z values', fontsize=12)

    # Contour lines
    contour_lines = plt.contour(X, Y, Z, levels=levels, colors='white', linewidths=0.5, linestyles='dotted')
    plt.clabel(contour_lines, inline=True, fontsize=8, fmt="%.1f", colors='black')

    # Additional Styling
    plt.title('Single Contour Plot', fontsize=18, fontweight='bold')
    plt.xlabel('X-Axis', fontsize=14)
    plt.ylabel('Y-Axis', fontsize=14)
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    

    plt.savefig(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Contour\Single_Contour_Plot.png', dpi=600)            # This was just the file location on my pc, you can tweak as per your's
    plt.show()


def contour_plot_7():
    '''This function shows multiple contour plots in single graph'''

    # Data for the first contour plot
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x, y)
    Z1 = np.sin(np.sqrt(X**2 + Y**2))
    Z2 = np.cos(np.sqrt(X**2 + Y**2))

    # First contour plot (filled)
    contour_filled = plt.contourf(X, Y, Z1, levels=20, cmap='viridis', alpha=0.6)
    cbar = plt.colorbar(contour_filled)
    cbar.set_ticks(np.arange(-1.0, 1.1, 0.5))
    cbar.set_label('Z1 values')

    # Second contour plot (lines)
    contour_lines = plt.contour(X, Y, Z2, levels=20, colors='white', linewidths=0.8)
    plt.clabel(contour_lines, inline=True, fontsize=8, fmt="%.1f", colors='black')

    # Additional Styling
    plt.title('Multiple Contour Plots', fontsize=18, fontweight='bold')
    plt.xlabel('X-Axis', fontsize=14)
    plt.ylabel('Y-Axis', fontsize=14)
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()

    plt.savefig(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Contour\Multi_Contour_Plot.png', dpi=600)            # This was just the file location on my pc, you can tweak as per your's
    plt.show()



# Main
# klear()                       # You may not see erros due to this
# contour_info()
# contour_plot_1()
# contour_plot_2()
# contour_plot_3()
# contour_plot_4()
# contour_plot_5()
# contour_plot_6()
# contour_plot_7()





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