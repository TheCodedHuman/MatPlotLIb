# Here we are fabricating program different functions to understand Line Chart/Plot in Matplotlib


# imports
import matplotlib.pyplot as plt
import numpy as np


# information
x = np.linspace(0, 10, 1000)
y = np.sin(x)
y2 = np.cos(x)

    

# defined
def plot_1():

    plt.figure(figsize=(10, 6))     # Figure size of the graph
    plt.plot(x, y)  # variable names could be anything, but both x and y values are required
    plt.title('Sine Wave')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()


def plot_2():

    plt.figure(figsize=(10, 6))     # Figure size of the graph
    plt.plot(x, y, label = 'Sine Wave')
    plt.title('Basic Line Plot with figure size')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend()                    # label we gave in plot function
    plt.grid(True)
    plt.show()


def plot_3():

    plt.figure(figsize=(10, 6))     # Figure size of the graph
    plt.plot(x, y, color = 'k', linestyle ='', label = 'Sine Wave')  # linestyle supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
    plt.title('Custumized LIne Plot')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_4():

    plt.figure(figsize=(10, 6))     # Figure size of the graph
    plt.plot(x, y, color='blue', linestyle='-', linewidth=1, marker='*', markersize= 10, label='Sine Wave with Markers')
    plt.title('Line Plot with Markers')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_5():

    plt.figure(figsize=(10, 6))     # Figure size of the graph
    plt.plot(x, y, label='Sine Wave')                      # We can add other attributes too as required (done in plot_4)
    plt.plot(x, y2, label='Cosine Wave', linestyle='--')
    plt.title('Multiple Lines Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_6():

    plt.figure(figsize=(10, 6))     # Figure size of the graph
    plt.plot(x, y, label='Sine Wave')                      # We can add other attributes too as required (done in plot_4)
    plt.plot(x, y2, label='Cosine Wave', linestyle='--')    
    plt.annotate('Intersection', xy=(np.pi/4, np.sin(np.pi/4)), xytext=(3, 0.5), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.grid()
    plt.title('Line Plot with Annotation')
    plt.legend()
    plt.show()


def plot_7():
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Sine Wave')
    plt.plot(x, y2, label='Cosine Wave', linestyle='dotted')
    plt.title('Saving the Line Plot')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend()
    plt.grid(True)
    
    # Save the plot as a PNG file before showing it
    # plt.savefig(r'D:/Bhaiyu Ki Files Aur Samaan/NewEraOfPython/MatPlotLIb/Graph_Images/line_plot00.png')
    plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Complete_Line_Plot77.png")

    # Display the plot
    plt.show()


def plot_8():

    # Create and customize the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue', linestyle='-', linewidth=2, marker='o', markersize=4, label='Sine Wave')
    plt.plot(x, y2, color='red', linestyle='--', linewidth=2, label='Cosine Wave')
    plt.title('Complete Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Annotate the point where sine and cosine intersect
    plt.annotate('Intersection', xy=(np.pi/4, np.sin(np.pi/4)), xytext=(7, 3),
                arrowprops=dict(facecolor='black', shrink=0.05))
                #  arrowprops = {'facecolor': 'black', 'shrink' : 0.05})

    plt.legend()
    plt.grid(True)
    plt.savefig("D:\\Bhaiyu Ki Files Aur Samaan\\NewEraOfPython\\MatPlotLIb\\Graph_Images\\Complete_Line_Plot88.png")
    plt.show()


# Main
# plot_1()
# plot_2()
# plot_3()
# plot_4()
# plot_5()
# plot_6()
# plot_7()
# plot_8()

# Remember, if you don't change file name, then the savefig() will rewrite the pre-saved graphs