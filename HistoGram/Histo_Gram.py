# Here we are fabricating different functioning functions regarding the histogram in matplotlib

# imports
import matplotlib.pyplot as plt
import numpy as np
import random as rd


# Information
np.random.seed(108)                      # This let's the generation of random numbers be consistant or same
x = np.random.uniform(0, 100, 20)       # 20 random numbers in range 0, 100

def phigure(): plt.figure(figsize=(10, 6))

def histo_info(): print(f"\nThe data we used here by x was:\t--->\t {x} \n\n")


# defined
def histo_plot_1():

    phigure()                           # Just using function again and again rather than figure(figsize=(m, n))
    plt.hist(x)                         # only x is requried (name can be different)
    plt.title('Basic Histogram Plot')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()


def histo_plot_2():

    phigure()                           
    plt.hist(x, label='Uniform Data Plot', zorder= 2)       # zorder (actually its z_order) which tell the placement of the things in the graph(bars, grids, etc)                    
    plt.title('Basic Histogram Plot')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.legend()
    plt.grid(True, zorder = 1)                              # Try the same code but without both z orders, 
    plt.show()


def histo_plot_3():                                         # Using only 5 attributes for now just for simplicity and understanding purpose, we can use all of them too

    weights = np.random.rand(20)
    phigure()
    plt.hist(x)   # (x, bins= 10, range= (1, 100), density= True, weights=weights, cumulative=True)           # Try cumulative with True/False/1/-1/0
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('No Usage Of Attributes -> Bins, Range, Density, Weights, Cumulative ')
    plt.legend()                                            # See the output terminal, as we didn't passed `label=`
    plt.grid(True)
    plt.show()


def histo_plot_4():                                         # Using only 5 attributes for now just for simplicity and understanding purpose, we can use all of them too

    weights = np.random.rand(20)
    phigure()
    plt.hist(x, bins= 10, range= (1, 100), density= True, weights=weights, cumulative=-1)           # Try cumulative with True/False/1/-1/0
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Usage Of Attributes -> Bins, Range, Density, Weights, Cumulative ')
    plt.legend()                                            # Did you checked the output terminal ?, as we didn't passed `label=`
    plt.grid(True)
    plt.show()


def histo_plot_5():
    
    phigure()
    # plt.hist(x, edgecolor='black', histtype='stepfilled', align='mid', orientation='vertical', rwidth=1)
    plt.hist(x, bins=30, edgecolor='black', bottom=0.5, histtype='step', orientation='horizontal', rwidth=0.9)                   # histtype supported values are 'bar', 'barstacked', 'step', 'stepfilled'    Try 'barstacked'
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Usage Of Attributes -> edgecolor, histtype, bottom, orientation, rwidth')
    plt.grid(True)
    plt.show()


def histo_plot_6():
    
    np.random.seed(42)
    dataA = np.random.randn(1000)
    dataB = np.random.randn(1000)

    def new_histo_info(): print(f"\nThe data we used here by dataA was:\t--->\t {dataA[:10]}...   and so on... \n\t\tAnd\nThe data we used here by dataB was:\t--->\t {dataB[:10]}...   and much more...\n")
    # def new_histo_info(): print(f"\nThe data we used here by dataA was:\t--->\t {dataA}...   and so on... \n\t\tAnd\nThe data we used here by dataB was:\t--->\t {dataB}...   and much more...\n")

    phigure()
    plt.hist([dataA, dataB], bins=30, align='mid',stacked=True, alpha= 0.7, zorder=2)  # here alpha is like opacity
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Usage Of Attributes -> two data, align, stacked, alpha, zordor')
    plt.grid(True, zorder=1)
    new_histo_info()
    plt.show()


def histo_plot_7():     # must try this function

    data1 = np.random.randn(1000)
    data2 = np.random.randn(1000)

    # def new_histo_info(): print(f"\nThe data we used here by dataA was:\t--->\t {dataA} \n\t\tAnd\nThe data we used here by dataB was:\t--->\t {dataB}\n")        # uncomment the line of code and see that there exist nested functions, so we can't use things like local variables, local function
    def new_histo_info(A, B): print(f"\nThe data we used here by dataA was:\t--->\t {A[:10]}...   and so on... \n\n\t\t\tAnd\n\nThe data we used here by dataB was:\t--->\t {B[:10]}...   and much more...\n")

    phigure()
    plt.hist([data1, data2], bins=30, edgecolor='black', histtype='barstacked')  # 'barstacked' histtype is being used here
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Usage Of Attributes -> edgecolor, bins, histtype, and passing requirements in nested function')
    plt.grid(True)
    new_histo_info(data1, data2)
    plt.show()


def histo_plot_8():         #savefig() 

    X = np.random.randn(1000)
    Y = np.random.randn(1000)

    phigure()
    plt.hist([X, Y], bins=30, edgecolor= 'k', linewidth= 1.5, histtype='bar',label= ['Data_X', 'Data_Y'],  zorder=2)    # Remember the spelling of zorder its not `zord'O'r`; somewhat like Z_order
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Usage Of Attributes -> linewidth; saving the graph in this function too')
    plt.legend()
    plt.grid(True, zorder=1)
    plt.savefig(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Histo_Gram\Histo_Plot_Graph.png')            # This was just the file location on my pc, you can tweak as per your's
    plt.show()

# Main
# histo_info()
histo_plot_1()
# histo_plot_2()
# histo_plot_3()
# histo_plot_4()
# histo_plot_5()
# histo_plot_6()
# histo_plot_7()
# histo_plot_8()
# new_histo_info()   # uncomment this line of code to understand here also we can't use functions globally (yeah that's a term) that is made local(this is too a term in programming) withing a function itself


# *Homework: Write one or more functions that use the concepts discussed in this program.



'''
there are various attributes in hist()
such as

@} Key Attributes of plt.hist()

x: The data to be plotted.                              # we usually use this as data
bins: Number of bins or intervals. You can also specify bin edges.
range: The lower and upper range of the bins.
density: If True, the result is the probability density function at the bin. Default is False.
weights: An array of weights, of the same shape as x.
cumulative: If True, a histogram is computed where each bin gives the counts in that bin plus all bins for smaller values.

bottom: Location of the bottom baseline of each bin (default is 0).
histtype: Type of histogram to draw: 'bar', 'barstacked', 'step', 'stepfilled'.
align: Controls how the histogram is plotted: 'left', 'mid', 'right'.
orientation: 'vertical' or 'horizontal'. Default is 'vertical'.
rwidth: Relative width of the bars as a fraction of the bin width.

color: Color or sequence of colors for the bars.
label: A string or sequence of strings to label the bars.
log: If True, the histogram axis will be set to a log scale.
stacked: If True, multiple data are stacked on top of each other.
alpha: The transparency of the bars (between 0 and 1).
'''

''' yahan jo likhte hain wo comment ho jata hai => multi-line comment'''