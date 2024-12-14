# #Here we are fabricating functions to represent the working of 3D plots in matplotlib, but we may have to utilize subplots and other libraries too for effectiveness (tbh, this is wayy new concept for me to learn so I could've made mistakes too :p )

# imports
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D                 # Its necessary as it helps integrating matplotlib in 3D axis
import numpy as np
import pandas as pd


# literals
# synthetic information related to a cyclist journey
time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
speed = np.array([10, 15, 20, 25, 22, 18, 15, 17, 20, 23, 25])
elevation = np.array([100, 150, 200, 250, 230, 210, 190, 200, 220, 250, 270])
df = pd.DataFrame({'time': time, 'speed': speed, 'elevation': elevation})


# defined
def basic_structure():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection= '3d')
    return fig, ax

def runtheplot(title, ax):
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Speed (km/h)')
    ax.set_zlabel('Elevation (meters)')
    ax.set_title(title)
    ax.legend(loc='upper left')
    # ax.view_init(elev=30, azim=45)                                                            # explaination of this is given below of whole code, but I think manually we can use however we want, you can uncomment this and experiment
    ax.grid(True)
    plt.show()

def liner_3D_info():
    print(f'\n\nThe data we using for 3D line plot is: \n\n{df}\n\n')


def liner_3D_plot_1():
    '''This 3D line plot shows basic and simple line plot'''
    fig, ax = basic_structure()
    ax.plot(time, speed, elevation, label='Cyclist Journey')
    runtheplot('basic 3D line plot', ax)                                                        # here's important to use ax due to runtheplot() requirements;    similarly for all the runtheplot() below   
    

def liner_3D_plot_2():
    '''This 3D line plot shows usage of linestyle, color, marker, markersize'''
    fig, ax = basic_structure()
    ax.plot(time, speed, elevation,
            linestyle= ':', 
            color= 'orangered',
            marker= '*',
            markersize= 10,
            label='Cyclist Journey')
    runtheplot('Usage of linestyle, color, marker, markersize', ax)


def liner_3D_plot_3():
    '''This 3D line plot shows usage of linewidth, markerfacecolor, xticks, yticks'''
    pass


# Main
# liner_3D_info()
# liner_3D_plot_1()
# liner_3D_plot_2()
# liner_3D_plot_3()





'''
@ Some attributes and Functions for 2D Line Plots [but, we can indeed use most of them in 3D plots too]:

Basic Data Parameters:
x: The x-coordinates of the line.
y: The y-coordinates of the line.


Line Properties:
color: Specifies the color of the line.
Example: plt.plot(x, y, color='blue')

linestyle: Specifies the style of the line (e.g., '-', '--', '-.', ':').
Example: plt.plot(x, y, linestyle='--')

linewidth: Specifies the width of the line.
Example: plt.plot(x, y, linewidth=2.0)


Markers:
marker: Specifies the marker style (e.g., 'o', '^', 's', '.').
Example: plt.plot(x, y, marker='o')

markerfacecolor: Specifies the fill color of the marker.
Example: plt.plot(x, y, marker='o', markerfacecolor='red')

markeredgecolor: Specifies the edge color of the marker.
Example: plt.plot(x, y, marker='o', markeredgecolor='black')

markersize: Specifies the size of the marker.
Example: plt.plot(x, y, marker='o', markersize=10)


Labels and Titles:
xlabel: Sets the label for the x-axis.
Example: plt.xlabel('X Axis')

ylabel: Sets the label for the y-axis.
Example: plt.ylabel('Y Axis')

title: Sets the title for the plot.
Example: plt.title('Line Plot')

Legend:
legend: Adds a legend to the plot.
Example: plt.legend(['Data 1', 'Data 2'], loc='upper left')


Grid and Ticks:
grid: Toggles the grid on or off.
Example: plt.grid(True)

xticks: Sets the ticks on the x-axis.
Example: plt.xticks([0, 2, 4, 6, 8, 10])

yticks: Sets the ticks on the y-axis.
Example: plt.yticks([0, 1, 2, 3, 4])


Plot Customization Options:
alpha: Sets the transparency level of the line.
Example: plt.plot(x, y, alpha=0.7)

label: Sets the label for the line, which appears in the legend.
Example: plt.plot(x, y, label='Sample Line')


Annotations:
annotate: Adds annotations to the plot.
Example: plt.annotate('Point of Interest', xy=(x, y), xytext=(x+1, y+1), arrowprops=dict(facecolor='black', shrink=0.05))


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@ Additional Attributes for 3D Line Plots:

View Angle:
view_init(elev, azim): Sets the elevation and azimuth angles to view the plot.
elev: Elevation angle in the z-plane.
azim: Azimuth angle in the x,y plane.
Example: ax.view_init(elev=30, azim=45)

Depth Shading:
depthshade: Specifies whether to shade the points based on their depth.
Example: ax.plot(x, y, z, depthshade=True)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Understanding view_init:
elev (Elevation Angle):
This parameter specifies the angle in the z-plane, essentially how "high" you are looking from above the plot.
For example, elev=30 means you are looking at the plot from an angle of 30 degrees above the xy-plane.

azim (Azimuth Angle):
This parameter specifies the angle in the x,y-plane, essentially how the plot is rotated around the z-axis.
For example, azim=45 means the plot is rotated 45 degrees around the z-axis, providing a view from a diagonal perspective.

Why Use view_init:
Better Visualization: Adjusting the view angles helps in visualizing the data better. For instance, if your data is clustered in a certain way, changing the view can make these clusters more apparent.
Highlight Specific Features: By adjusting the view, you can highlight specific features or trends in your data that might not be visible from the default view.
Creating Engaging Visuals: Different angles can make your plot more engaging and can help in presentations or reports by showcasing your data from the best possible perspective.

'''

