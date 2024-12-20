# Here we are fabricating set of functions for the explaination of scatter plot in matplotlib

# imports
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

# literals
np.random.seed(108)
x = np.random.rand(50)
y = np.random.rand(50)

plt.rcParams['figure.figsize'] = (10, 6)                        # we can use user defined functins to change figsize as per user too

sizes = 1000 * np.random.rand(50)
colors = np.random.rand(50)



# Klassed
class BasePlotter:
    def __init__(self):                                             # something is required, it could be 'self' or 'any_variable', it implies to 'whom should I communicate to...', here is goes for ownself -> instance creation of its own
        print('#_$')
        # pass                                                      # __init__(self) can't be empty
        
    def set_labels(self, title, xlabel, ylabel):
        plt.title(title, fontsize = 20)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def show_plot(self):
        plt.show()
 

class ScatterPlotter(BasePlotter):
    def __init__(self, x, y):
        super().__init__()                          # calls parent class
        self.x = x                                     # self.x leads to instance variable मामला
        self.y = y

    def scato_info(self): print(f''' 

    The Data we used for x was -> \t{x}

                And

    The Data we used for y was -> \t{y}

    ''')

    def scatter_plot_1(self):
        plt.scatter(self.x, self.y)
        self.set_labels('Basic Scatter Plot', 'X-Axis', 'Y-Axis')
        self.show_plot()                                                    # self is instance


    def scatter_plot_2(self):
        plt.scatter(self.x, self.y, label= 'Rand Form Data', zorder = 2)
        self.set_labels('Usage of Zorder and Legend', 'X-Axis', 'Y-Axis')
        plt.grid(True, zorder = 1)
        plt.legend()
        self.show_plot()

    def scatter_plot_3(self):
        plt.scatter(self.x, self.y, color = 'k', s = sizes, marker = 's', alpha = 0.5, zorder = 2)
        self.set_labels('Usage Of Color, Size, Alpha, Marker, linestyle', 'X-Axis', 'Y-Axis')               # Still for explaination I am not using DRY (Do not Repeat Yourself) concept, but for demonstration did for plt.title, xlabel, ylable, figure(),which we can even set scaler forever too
        plt.grid(True, linestyle= '--', alpha = 0.7, zorder = 1)
        self.show_plot()
        
    def scatter_plot_4(self):
        norm = Normalize(vmin = min(colors), vmax = max(colors))
        plt.scatter(self.x, self.y, c = colors, norm=norm, cmap = 'viridis', linewidths=2, edgecolor = 'gold', s = sizes)
        self.set_labels('Usage Of Norm, Cmap, linewidths, edgecolor, vmin-vmax', 'X-axis', 'Y-Axis')
        plt.colorbar()
        self.show_plot()

    def scatter_plot_5(self):
        # from matplotlib.colors import Normalize       # We can import in here too, also in scatter_plot_4()
        temperaturs = np.random.rand(50) * 40          # Random temperature between [0, 40]
        norm = Normalize(vmin=0, vmax=40)
        plt.scatter(self.x, self.y, c = temperaturs, cmap = 'coolwarm', s = 1000, edgecolor = 'black')
        self.set_labels('Example Usage IRL', 'X-Axis', 'Y-Axis')
        plt.colorbar(label= 'Temperature (*C)')
        self.show_plot()

    def scatter_plot_6(self):
        plt.scatter(self.x, self.y, facecolor = 'lightblue', label = 'Sample Data', sizes = sizes)
        plt.show()                          # we still can use simple functions, but classes, user defined functions can help us add extra functionalities

    def scatter_plot_7(self):

        np.random.seed(72)
        m = np.random.rand(50)
        n = np.random.rand(50)
        norm = Normalize(vmin = min(colors), vmax = max(colors))

        scatter1 = plt.scatter(self.x, self.y, c= colors, norm = norm, cmap='cool', s=sizes, alpha= 0.6, edgecolors='white', linewidths=0.75, label='Data_A', zorder = 2)
        # plt.colorbar(label= 'Color Intensity')                                            #We can use this too, this make colorbar() more simple and easier
        plt.scatter(m, n, c= 'green', s=sizes, alpha= 0.5, edgecolors='black', linewidths=0.5, label='Data_B', zorder = 3)
        
        self.set_labels('Saving Da Scatter Plot', 'X-Axis', 'Y-Axis')
        plt.grid(True, linestyle= ':', linewidth= 2, alpha= 0.5, zorder = 1)                # linestyle supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
        plt.legend()
        
        
        # plt.colorbar(label= 'Color Intensity', fontsize= 17.5)                            # maybe fontsize isn't part of plt.colorbar()
        cbar = plt.colorbar(scatter1, label='Color Intensity')                                                   # Link colorbar to the first scatter plot                                  
        cbar.ax.tick_params(labelsize=12)                                                                        # Adjust the size of colorbar ticks, changes the size of 0.2, 0.4, 0.6, 0.8
        
        plt.savefig(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Scatter\SaveDaScatterPlot.png', dpi=300)
        # plt.savefig(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Scatter\SaveDaScatterPlot.svg', dpi=300)                   # Scalable Vector Graphic File
        self.show_plot()


# Main
scatter_plotter = ScatterPlotter(x, y)
# scatter_plotter.scato_info()
# scatter_plotter.scatter_plot_1()
# scatter_plotter.scatter_plot_2()
# scatter_plotter.scatter_plot_3()
# scatter_plotter.scatter_plot_4()
# scatter_plotter.scatter_plot_5()
# scatter_plotter.scatter_plot_6()
# scatter_plotter.scatter_plot_7()


# *Homework: Write one or more functions that use the concepts discussed in this program.                       {scatter_plot_8()}
# *Homework: Answer the question> in which scenario we can use Scatter Plot rather than Bar Graph or Histogram  {Hint: Venn Diagram}


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