# Here we are fabricating functions for def by scatter plot

# imports
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.colors import Normalize


# information
x = [7, 4, 2, 4, 6, 6]
y = [7, 2, 5, 7, 2, 1]
size = 1000


# program
plt.scatter(x, y, s=size, c= ['k', 'gold', 'blue', 'm', 'green', 'yellow'], marker='^', zorder= 3, alpha=0.5)
plt.legend()
plt.grid(True, zorder = 1)
plt.show()




'''
@} Key Attributes for scatter():

x, y: Coordinates of the data points.                                           # Two data points are necessary unlike histogram
s: Size of the markers. It can be a single value or an array of values.
c: Color of the markers. This can be a single color format string, or an array of numbers, or a 2D array with shape (n, 3) or (n, 4) for RGB(A) values.
marker: Marker style. E.g., 'o' for circle, 's' for square, '^' for triangle, etc.
alpha: The transparency of the markers, a float between 0 (transparent) and 1 (opaque).


norm: Normalize object to scale luminance data to 0-1 range.
vmin, vmax: Scalar values that define the data range that colormap covers.
linewidths: The width of the marker edges.
edgecolor or edgecolors: The color of the marker edges.
cmap: Colormap for mapping intensity of colors.

facecolor or facecolors: The color of the marker face.
label: A string to label the data points, useful for legends.
sizes: An array specifying the size of each point.
color: An array specifying the color of each point.
data: Optional parameter to pass other data.
****kwargs**: Any additional keyword arguments for the marker style (e.g., 'linestyle', 'alpha').
'''
float = 