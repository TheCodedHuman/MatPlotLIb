#Here we are fabricating several functions showcasing the working of 3D scatter plot

# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go



# literals


file_path= r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\3D_Scatter\Sample_Data.xlsx'
df = pd.read_excel(file_path)
df.to_csv(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\3D_Scatter\Sample_Data.csv', index= False)
print('CSV file generated successfully.')


Label= 'Cyclist Journey'



# defined
def basic_structure():
    fig = plt.figure()
    ax = fig.add_subplot(projection= '3d')
    return fig, ax


def runtheplot(title, ax):
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Speed (km/h)')
    ax.set_zlabel('Elevation (meters)')
    ax.set_title(title)
    ax.legend(loc='upper left')
    # ax.view_init(elev=30, azim=45)                                                            # explaination of this is given below of whole code, but I think manually we can use however we want, you can uncomment this and experiment
    ax.grid(True, zorder= 2)
    plt.show()



def liner_3D_info():
    print(f'\n\nThe data we using for 3D line plot is: \n\n{df}\n\n')


# Main
liner_3D_info()




'''
@ Some attributes and Functions for 3D Scatter Plots in Matplotlib

Basic Data Parameters:
x: The x-coordinates of the points.

y: The y-coordinates of the points.

z: The z-coordinates of the points.



Scatter Plot Properties:
c: Specifies the color of the markers.
Example: ax.scatter(x, y, z, c='red') or ax.scatter(x, y, z, c=colors, cmap='viridis')

marker: Specifies the marker style.
Example: ax.scatter(x, y, z, marker='o')

s: Specifies the size of the markers.
Example: ax.scatter(x, y, z, s=100)

alpha: Sets the transparency level of the markers.
Example: ax.scatter(x, y, z, alpha=0.7)



Labels and Titles:
xlabel: Sets the label for the x-axis.
Example: ax.set_xlabel('X Label')

ylabel: Sets the label for the y-axis.
Example: ax.set_ylabel('Y Label')

zlabel: Sets the label for the z-axis.
Example: ax.set_zlabel('Z Label')

title: Sets the title for the plot.
Example: ax.set_title('3D Scatter Plot Example')



Grid and Ticks:
grid: Toggles the grid on or off.
Example: ax.grid(True)

xticks: Sets the ticks on the x-axis.
Example: ax.set_xticks([0, 0.5, 1])

yticks: Sets the ticks on the y-axis.
Example: ax.set_yticks([0, 0.5, 1])

zticks: Sets the ticks on the z-axis.
Example: ax.set_zticks([0, 0.5, 1])



Plot Customization Options:
cmap: Specifies the colormap to use for the markers.
Example: ax.scatter(x, y, z, c=colors, cmap='viridis')

depthshade: Specifies whether to shade the points based on their depth.
Example: ax.scatter(x, y, z, depthshade=True)

edgecolors: Specifies the edge color of the markers.
Example: ax.scatter(x, y, z, edgecolors='w')

linewidths: Specifies the width of the marker edges.
Example: ax.scatter(x, y, z, linewidths=1)



Annotations:
text: Adds annotations to specific points.
Example: ax.text(x[i], y[i], z[i], 'Point {}'.format(i), color='red')

annotate: Adds annotations with arrows to specific points.
Example: ax.annotate('Point of Interest', xy=(x[i], y[i], z[i]), xytext=(x[i]+0.1, y[i]+0.1, z[i]+0.1), arrowprops=dict(facecolor='black', arrowstyle='->'))


View Angle:
view_init(elev, azim): Sets the elevation and azimuth angles to view the plot.
elev: Elevation angle in the z-plane.
azim: Azimuth angle in the x,y-plane.
Example: ax.view_init(elev=20, azim=45)

Additional Features:
fig.colorbar: Adds a color bar to the plot.
Example: fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)

'''

