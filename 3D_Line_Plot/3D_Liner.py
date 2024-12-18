# #Here we are fabricating functions to represent the working of 3D plots in matplotlib, but we may have to utilize subplots and other libraries too for effectiveness (tbh, this is wayy new concept for me to learn so I could've made mistakes too :p )

# imports
# from mpl_toolkits.mplot3d import Axes3D                   # this module can also be used, but, here plotly is already helping us in 3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go                           # helps in SAVING interactive 3D plots   ;   have to do in cmd "pip install plotly"


# literals
# synthetic information related to a cyclist journey
time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
speed = np.array([10, 15, 20, 25, 22, 18, 15, 17, 20, 23, 25])
elevation = np.array([100, 150, 200, 250, 230, 210, 190, 200, 220, 250, 270])
df = pd.DataFrame({'Time': time, 'Speed': speed, 'Elevation': elevation})
Label= 'Cyclist Journey'


# defined-
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
    ax.grid(True, zorder= 2)
    plt.show()

def liner_3D_info():
    print(f'\n\nThe data we using for 3D line plot is: \n\n{df}\n\n')


def liner_3D_plot_1():
    '''This 3D line plot shows basic and simple line plot'''
    fig, ax = basic_structure()
    ax.plot(time, speed, elevation, label= Label)
    runtheplot('basic 3D line plot', ax)                                                        # here's important to use ax due to runtheplot() requirements;    similarly for all the runtheplot() below   
    

def liner_3D_plot_2():
    '''This 3D line plot shows usage of linestyle, color, marker, markersize'''
    fig, ax = basic_structure()
    ax.plot(time, speed, elevation,
            linestyle= ':', 
            color= 'orangered',
            marker= '*',
            markersize= 10,
            label= Label)
    runtheplot('Usage of linestyle, color, marker, markersize', ax)


def liner_3D_plot_3():
    '''This 3D line plot shows usage of linewidth, markerfacecolor, xticks, yticks'''
    fig, ax = basic_structure()
    ax.plot(time, speed, elevation,
            linewidth= 3,
            linestyle= "--",
            markerfacecolor= 'green',
            label= Label)

    # Custom ticks
    ax.set_xticks([0, 2, 4, 6, 8, 10]) 
    ax.set_yticks([10, 15, 20, 25]) 
    ax.set_zticks([100, 150, 200])


    runtheplot('Usage of linewidth, markerfacecolor, xticks, yticks', ax)
    

def liner_3D_plot_4():
    '''This 3D line plot shows usage of alpha, annotation, depthshade'''
    fig, ax = basic_structure()
    ax.plot(time, speed, elevation,
            color= 'purple',
            linestyle= '-',
            marker= 'o',
            zorder = 1,
            label= Label,
            alpha= 0.6)

    ax.text(4, 22, 230, '(4, 22, 230)', color='purple', fontsize=10)

    # ax.annotate('Peak',                               # I don't know why annotate doesn't worked here, maybe it can't be used in 3D   ;   but... later below I got to know about its working by ChatGPT and Copilot (in my opinion, no problem in using AI if one learns while copying too a.k.a. Anukaran)
    #             xy= (4, 22),
    #             xytext= (5, 25),
    #             textcoords= 'offset points',
    #             annotation_clip=False,
    #             arrowprops= dict(facecolor= 'limegreen', shrink= 0.05))    
    runtheplot('Usage of alpha, annotation, depthshade, zorder', ax)
    
    
def liner_3D_plot_5():
    '''This 3D line plot shows dynamic coordinates annotation by plt.text()'''
    fig, ax = basic_structure()
    ax.plot(time, speed, elevation,
            color='purple',
            linestyle='-',
            marker='o',
            zorder=1,
            label=Label,
            alpha=0.6)

    # Dynamically annotate each point
    for i in range(len(time)):
        ax.text(time[i], speed[i], elevation[i], f'({time[i]}, {speed[i]}, {elevation[i]})', fontsize=8, color='purple')

    runtheplot('Usage of alpha, dynamic annotation, zorder', ax)


def liner_3D_plot_6():
    '''This 3D line plot shows dynamic coordinates annotation by plt.text(), changes background color, and saves the figure'''
    fig, ax = basic_structure()
    fig.patch.set_facecolor('black')  # Change figure background color
    ax.set_facecolor('whitesmoke')  # Change axes background color
    ax.grid(color='lightblue')  # Change grid color

    ax.plot(time, speed, elevation,
            color='purple',
            linestyle='-',
            marker='o',
            zorder=1,
            label=Label,
            alpha=0.6)

    # Dynamically annotate each point
    for i in range(len(time)):
        ax.text(time[i], speed[i], elevation[i], f'({time[i]}, {speed[i]}, {elevation[i]})', fontsize=8, color='purple')

    # Making customization in figure
    fig.patch.set_facecolor('lightcoral')
    
    ax.set_facecolor('darkturquoise')
    ax.xaxis.set_pane_color((0.9, 0.9, 0.9, 1.0))
    ax.yaxis.set_pane_color((0.9, 0.9, 0.9, 1.0))
    ax.zaxis.set_pane_color((0.9, 0.9, 0.9, 1.0))

    ax.xaxis._axinfo['grid'].update(color= '#c2c2f0')
    ax.yaxis._axinfo['grid'].update(color= '#99ff99')
    ax.zaxis._axinfo['grid'].update(color= '#ffcc99')

    # plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\3D_Line_Plot\3D_liner", bbox_inches= 'tight', dpi= 200)

    runtheplot('Usage of alpha, dynamic annotation, zorder, and background color changes', ax)


def liner_3D_plot_7():
    '''This 3D line plot saves the interactive figure'''

    # Create Plotly figure
    fig = go.Figure()

    # Adding 3D line plot
    fig.add_trace(go.Scatter3d(
        x=time,
        y=speed,
        z=elevation,
        mode='markers+lines',
        marker=dict(size=5, color='purple', opacity=0.8),
        line=dict(color='purple', width=2),
        text=[f'({t}, {s}, {e})' for t, s, e in zip(time, speed, elevation)],
        hoverinfo='text'
    ))

    # Setting layout
    fig.update_layout(
        title='Cyclist Journey: Time vs Speed vs Elevation',
        scene=dict(
            xaxis_title='Time (hours)',
            yaxis_title='Speed (km/h)',
            zaxis_title='Elevation (meters)',
            bgcolor='lightgrey'
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    # Save the interactive plot as an HTML file
    # fig.write_html(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\3D_Line_Plot\3D_liner_interactive.html")
    fig.show()



def liner_3D_plot_8():
    '''This 3D line plot saves the interactive figure - ANOTHER IMPLEMENTATION'''

    # Create a 3D plot
    fig = go.Figure()

    # Add a line plot with markers
    fig.add_trace(go.Scatter3d(
        x=time, y=speed, z=elevation,
        mode='markers+lines',
        marker=dict(size=5, color='purple', opacity=0.8),
        line=dict(color='purple', width=2),
        name=Label
    ))

    # Annotate points dynamically
    annotations = [                                                         # Okay, so annotations is going to work like this; this works
        dict(
            x=time[i], y=speed[i], z=elevation[i],
            text=f"({time[i]}, {speed[i]}, {elevation[i]})",
            showarrow=True,
            arrowhead=2,
            ax=20, ay=-30,
            font=dict(color="purple", size=10)
        )
        for i in range(len(time))
    ]
    fig.update_layout(scene_annotations=annotations)

    # Set titles and background colors
    fig.update_layout(
        title='Interactive 3D Line Plot',
        scene=dict(
            xaxis_title='Time',
            yaxis_title='Speed',
            zaxis_title='Elevation',
            xaxis=dict(backgroundcolor="lightcoral"),
            yaxis=dict(backgroundcolor="darkturquoise"),
            zaxis=dict(backgroundcolor="lightgrey")
        )
    )

    # Save as an interactive HTML file
    # fig.write_html(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\3D_Line_Plot\3D_liner_interactive_II.html")
    fig.show()




# Main
# liner_3D_info()
# liner_3D_plot_1()
# liner_3D_plot_2()
# liner_3D_plot_3()
# liner_3D_plot_4()
# liner_3D_plot_5()
# liner_3D_plot_6()
# liner_3D_plot_7()
# liner_3D_plot_8()
   





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

