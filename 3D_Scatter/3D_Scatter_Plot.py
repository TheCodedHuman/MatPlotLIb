# Here we are fabricating functions that show the working of 3D scatter plot


# imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# literals
# 1} using already existing excel file to convert to csv automatedly; then reading it and printing a dataframe
excel_file_path = r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\3D_Scatter\Sample_Data_Info.xlsx"
csv_file_path = r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\3D_Scatter\Sample_Data.csv'
df = pd.read_excel(excel_file_path)
# df.to_csv(csv_file_path, index= False)


# 2} If you don't want to use openpyxl (we have to use pip install openpyxl), then we can manually convert the excel file from MS Excel and use that similarly , we just have to tell the location where it is
# Implementing the data
df_csv= pd.read_csv(csv_file_path)
time= df_csv['Time'].values
speed= df_csv['Speed'].values
elevation= df_csv['Elevation'].values


# 3} using python's inbuilt open(), close() and maybe with loops too
time_= []
speed_= []
elevation_= []

with open(csv_file_path, mode= 'r') as file:
    next(file)                                      # this skips the most upper header of file

    for line in file:
        values= line.strip().split(',')
        time_.append(int(values[1]))
        speed_.append(int(values[2]))
        elevation_.append(int(values[3]))

data = {'Time (hours)': time_, 'Speed (km/h)': speed_, 'Elevation (meters)': elevation_}
df_ = pd.DataFrame(data, index= time_)
    

Label= 'Cyclist Journey'
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


# defined
def scato_3D_info():
    print(f'\n\nThe data we using for 3D scatter plot is: \n\n{df}\n\n')                                            # we primarily going to use this data
    print(f'\n\nThe data we using for 3D scatter plot by python\' open() close() is: \n\n{df_}\n\n')                # we can use this too similarly


def basic_structure():
    fig = plt.figure()
    ax= fig.add_subplot(111, projection= '3d')
    return fig, ax


def runtheplot(title, ax):
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Speed (km/h)')
    ax.set_zlabel('Elevation (meters)')
    ax.set_title(title)
    ax.legend(loc='upper left')
    # ax.view_init(elev=30, azim=45)                                                            # explaination of this is given below as usage in code, but I think manually we can use however we want, you can uncomment this and experiment
    # ax.grid(True, zorder= 2)
    ax.grid(True)
    plt.show()


def scato_1_3d():
    '''This 3D scatter plot shows the basic and simple scatter plot'''
    fig, ax= basic_structure()
    ax.scatter(time, speed, elevation, label= Label)
    runtheplot('Basic 3D Scatter Plot', ax)

def scato_2_3d():
    '''This 3D scatter plot shows the usage of c, marker, s, alpha'''
    fig, ax = basic_structure()
    sizes= [100 * (i / max(elevation)) for i in elevation]
    skatter= ax.scatter(time, speed, elevation, c= speed, s= sizes, marker= '*', alpha= 0.6, label= Label)
    fig.colorbar(skatter, shrink= 0.5, aspect= 5)
    runtheplot('Usage of c, marker, s, alpha', ax)


def scato_3_3d():
    '''This 3D scatter plot shows the usage of xticks, yticks, zticks, c+cmap'''
    fig, ax = basic_structure()
    x= [i for i in range(min(time), max(time) +1, 2)]
    y= [i for i in range(min(speed), max(speed) +1, 5)]
    z= [i for i in range(min(elevation), max(elevation), 30)]

    skatter= ax.scatter(time, speed, elevation, marker= '*', c= elevation, cmap= 'Reds', label= Label)
    fig.colorbar(skatter, shrink= 0.5, aspect= 5)

    # Changing the range ticks in panes of graph
    ax.set_xticks(x) 
    ax.set_yticks(y) 
    ax.set_zticks(z)

    runtheplot('Usage of xticks, yticks, zticks, cmap', ax)



def scato_4_3d():
    '''This 3D scatter plot shows the usage of depthshade{by default True}, edgecolors, linewidths'''
    fig, ax= basic_structure()
    skatter= ax.scatter(time, speed, elevation, depthshade= False, edgecolors= 'black', linewidths= 2, label= Label, c= elevation, cmap= 'Reds_r')
    fig.colorbar(skatter, shrink= 0.5, aspect= 5)
    runtheplot('Usage of depthshade{by default True}, edgecolors, linewidths', ax)
    

def scato_5_3d():
    '''This 3D scatter plot shows the usage of gradient colors for clarity'''
    fig, ax= basic_structure()
    skatter= ax.scatter(time, speed, elevation, depthshade= False, edgecolors= 'black', linewidths= 2, label= Label, c= elevation, cmap= plt.cm.Spectral)
    # skatter= ax.scatter(time, speed, elevation, depthshade= False, edgecolors= 'black', linewidths= 2, label= Label, c= elevation, cmap= 'rainbow')
    fig.colorbar(skatter, shrink= 0.5, aspect= 5)
    runtheplot('Usage of depthshade{by default True}, edgecolors, linewidths', ax)
    

def scato_6_3d():
    '''This 3D scatter plot shows the usage of text, suptitle'''

    # Creating a figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': '3d'}, figsize=(14, 7))

    # Adding a super title for the entire figure
    fig.suptitle('Comprehensive 3D Scatter Plot with Text and Annotations', fontsize=16)

    # First subplot - with text
    skatter= ax1.scatter(time, speed, elevation, c=elevation, cmap='viridis', marker='o', label=Label)
    fig.colorbar(skatter, ax=ax2, shrink=0.5, aspect=5)
    ax1.set_title('3D Scatter Plot with Text')

    # Adding text at specific points
    for i in range(len(time)):
        ax1.text(time[i], speed[i], elevation[i], f'{time[i]}, {speed[i]}', color='black')

    # Second subplot - with annotations
    scatter = ax2.scatter(time, speed, elevation, c=elevation, cmap='inferno', marker='^', label=Label)
    ax2.set_title('3D Scatter Plot with Annotations')

    # Adding text annotations at specific points
    for i in range(len(time)):
        ax2.text(time[i], speed[i], elevation[i], f'({time[i]}, {speed[i]}, {elevation[i]})', color='black')

    # Adding color bar to the second subplot
    fig.colorbar(scatter, ax=ax2, shrink=0.5, aspect=5)

    # Adjust layout and show the plot
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit the suptitle
    plt.show()


def scato_7_3d():
    '''This 3D scatter plot shows the usage of text, suptitle'''

    # Creating a figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': '3d'}, figsize=(14, 7))

    # Adding a super title for the entire figure
    fig.suptitle('Comprehensive 3D Scatter Plot with Text and Annotations', fontsize=16)

    # First subplot - with text
    skatter = ax1.scatter(time, speed, elevation, c=elevation, cmap='viridis', marker='o', label=Label)
    fig.colorbar(skatter, ax=ax1, shrink=0.5, aspect=5)
    ax1.set_title('3D Scatter Plot with Text')

    # Adding text at specific points
    for i in range(len(time)):
        ax1.text(time[i], speed[i], elevation[i], f'{time[i]}, {speed[i]}', color='black')

    # Second subplot - with annotations
    scatter = ax2.scatter(time, speed, elevation, c=elevation, cmap='inferno', marker='^', label=Label)
    fig.colorbar(scatter, ax=ax2, shrink=0.5, aspect=5)
    ax2.set_title('3D Scatter Plot with Annotations')

    # Adding text annotations at specific points
    for i in range(len(time)):
        ax2.text(time[i], speed[i], elevation[i], f'({time[i]}, {speed[i]}, {elevation[i]})', color='black')

    # Adjust layout and show the plot
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit the suptitle
    plt.show()


import matplotlib.pyplot as plt
import numpy as np

def scato_8_3d():
    '''This 3D scatter plot shows the presence of multiple scatter plots within single figure'''

    # Creating random data for multiple scatter plots
    np.random.seed(108)  # For reproducibility
    
    num_points = 100
    x1 = np.random.uniform(-100, 100, num_points)
    y1 = np.random.uniform(-100, 100, num_points)
    z1 = np.random.uniform(-100, 100, num_points)
    
    x2 = np.random.uniform(-150, 150, num_points)
    y2 = np.random.uniform(-150, 150, num_points)
    z2 = np.random.uniform(-150, 150, num_points)
    
    x3 = np.random.uniform(-50, 50, num_points)
    y3 = np.random.uniform(-50, 50, num_points)
    z3 = np.random.uniform(-50, 50, num_points)
    
    # Creating the figure and 3D axis
    fig, ax = basic_structure()

    scatter1 = ax.scatter(x1, y1, z1, c='r', marker='o', label='Group 1', alpha=0.6)
    scatter2 = ax.scatter(x2, y2, z2, c='g', marker='^', label='Group 2', alpha=0.6)
    scatter3 = ax.scatter(x3, y3, z3, c='b', marker='s', label='Group 3', alpha=0.6)
    
    # Adding legends for clarity
    runtheplot('3D Scatter Plot with Multiple Groups', ax)
    


def scato_9_3d():
    '''This 3D scatter plot saves the image of 3D scatter plot by savefig()'''

    # Creating random data for star positions
    np.random.seed(108)  # For reproducibility
    num_stars = 100
    x = np.random.uniform(-100, 100, num_stars)  # X-coordinates
    y = np.random.uniform(-100, 100, num_stars)  # Y-coordinates
    z = np.random.uniform(-100, 100, num_stars)  # Z-coordinates
    magnitudes = np.random.uniform(0.5, 3, num_stars)  # Star magnitudes (sizes)
    colors = np.random.uniform(0, 1, num_stars)  # Color based on star brightness

    # Creating the figure and 3D axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot for star positions
    scatter = ax.scatter(x, y, z, c=colors, cmap='cool', s=magnitudes * 100, alpha=0.8, edgecolors='w')

    # Adding a color bar
    fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)

    # Setting labels and title
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Z Coordinate')
    ax.set_title('3D Scatter Plot of Star Positions in the Galaxy')

    # Saving the plot as an image
    # plt.savefig(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\3D_Scatter_Plot\3D_Star_Positions.png', dpi=300)
    plt.show()




def scato_10_3d():
    '''This 3D scatter plot saves the dynamic/interactive visually appealing and mentally intruiging 3D scatter plot by plotly'''

    # Creating random data for asteroid positions
    np.random.seed(108)  # For reproducibility
    num_asteroids = 200
    x = np.random.uniform(-500, 500, num_asteroids)  # X-coordinates
    y = np.random.uniform(-500, 500, num_asteroids)  # Y-coordinates
    z = np.random.uniform(-500, 500, num_asteroids)  # Z-coordinates
    sizes = np.random.uniform(1, 20, num_asteroids)  # Asteroid sizes
    colors = np.random.uniform(0, 1, num_asteroids)  # Color based on random values

    # Create a 3D scatter plot with Plotly
    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=sizes,
            color=colors,
            colorscale='Viridis',
            opacity=0.8,
            colorbar=dict(title='Random Value'),
        )
    )])

    # Adding labels and title
    fig.update_layout(
        title='Interactive 3D Scatter Plot of Asteroid Positions',
        scene=dict(
            xaxis_title='X Coordinate',
            yaxis_title='Y Coordinate',
            zaxis_title='Z Coordinate'
        )
    )

    # Save the interactive plot as an HTML file and show the figure
    # fig.write_html(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\3D_Scatter_Plot\3D_Star_Positions.html')
    fig.show()




# Main
# scato_3D_info()
# scato_1_3d()
# scato_2_3d()
# scato_3_3d()
# scato_4_3d()
# scato_5_3d()
# scato_6_3d()
# scato_7_3d()
# scato_8_3d()
# scato_9_3d()
# scato_10_3d()



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

