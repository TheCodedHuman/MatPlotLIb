#Here we are fabricating functions demonstrating the working of violin plot in matplotlib

# imports
import matplotlib.pyplot as plt
import numpy as np



# literals
plt.rcParams['figure.figsize'] = (10, 6)
np.random.seed(108)

math_scores = np.random.normal(75, 10, 100)                                                                     # Mathematics: Mean 75, Std 10
science_scores = np.random.normal(70, 15, 100)                                                                  # Science: Mean 70, Std 15
english_scores = np.random.normal(80, 12, 100)                                                                  # English: Mean 80, Std 12

data = [math_scores, science_scores, english_scores]



# defined
def violin_info():
    sp = '~'*100
    print(f"The Math Score are -> {math_scores}\n\n{sp}\n\nThe Science Scores are -> {science_scores}\n\n{sp}\n\nThe English Scores are -> {english_scores}\n\n")



def runtheplot(title):                                                                                          # Add labels and title
    plt.xticks([1, 2, 3], ['Mathematics', 'Science', 'English'])
    plt.xlabel('Subjects')
    plt.ylabel('Scores')
    plt.title(title)
    plt.show()


def customization(whatever_the_plot_name_is):                                                                   # This is not required to do always, but shown just for demonstration of what things are possible to do
    for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans', 'showextrema'):
        if partname in whatever_the_plot_name_is:
            vp = whatever_the_plot_name_is[partname] 
            vp.set_edgecolor('gold') 
            vp.set_linewidth(1) 
        
    for pc in whatever_the_plot_name_is['bodies']: 
        pc.set_facecolor('lightblue') 
        pc.set_edgecolor('black') 
        pc.set_alpha(0.5)


def violin_plot_1():
    '''This function shows the basic violin plot'''
    plt.violinplot(data)
    runtheplot('Basic Violin Plot')


def violin_plot_2():
    '''This function shows the usage of positions, vert, widths, showmeans'''
    da_plot = plt.violinplot(data,
                            positions= [1, 2, 3],
                            vert= False,
                            widths= 0.7,
                            showmeans= True
                   )
    customization(da_plot)
    runtheplot('Usage of positions, vert, widths, showmeans')


def violin_plot_3():
    '''This function shows the usage of showmedians, quantiles, bw_method'''
    da_plot = plt.violinplot(data, 
                             showextrema= False,                                                                # don't know why but in dropdown menu it is coming, but I am not able to call it correctly
                             showmeans= True, 
                             showmedians= True,                                                                 # showextrema and color aren't part of violin plot
                             quantiles= [[0.25, 0.5, 0.75],[0.25, 0.5, 0.75],[0.25, 0.5, 0.75]],                # should be a list or array;                                for eg,  quantiles=[0.25, 0.5, 0.75] would show the 25th, 50th (median), and 75th percentiles.
                             bw_method= 'silverman'                                                             # Can be 'scott', 'silverman', or a scalar constant
                   )
    customization(da_plot)
    runtheplot('Usage of showmedians, quantiles, bw_method')


def violin_plot_4():
    '''This function shows the working of multiple attributes of violin plot WIHOUT intersecting violin plots               ...and saves figure'''

    # Generate some data
    np.random.seed(0)
    data1 = np.random.normal(0, 1, 100)
    data2 = np.random.normal(2, 1.5, 100)
    data3 = np.random.normal(3, 0.5, 100)
    data = [data1, data2, data3]

    # Create a violin plot with customizations
    fig, ax = plt.subplots(figsize=(12, 8))
    violin_parts = ax.violinplot(data, 
                                positions=[1, 2, 3], 
                                vert=True, 
                                widths=0.7,
                                showmeans=True, 
                                showmedians=True, 
                                showextrema=True,
                                bw_method='silverman')

    # Customizing the colors
    customization(violin_parts)

    # Add labels and title
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3'])
    ax.set_xlabel('Groups')
    ax.set_ylabel('Values')
    ax.set_title('Customized Violin Plot Example')
    # plt.savefig(r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Violin\Violin_Plot_04.png')
    plt.show()


def violin_plot_5():
    '''This function shows the intersecting violin plots'''

    # Generate synthetic data for demonstration
    np.random.seed(108)
    data1 = np.random.normal(0, 1, 100)
    data2 = np.random.normal(1, 2, 100)
    data3 = np.random.normal(-1, 1.5, 100)
    data4 = np.random.normal(2, 1.2, 100)
    # data = [data1, data2, data3, data4]
    
    # Create the violin plot
    # plt.violinplot(data1, showmeans=True, showmedians=True, showextrema=True, widths=0.9)
    plt.violinplot(data2, showmeans=True, showmedians=True, showextrema=True, widths=0.9)
    plt.violinplot(data3, showmeans=True, showmedians=True, showextrema=True, widths=0.9)
    # plt.violinplot(data4, showmeans=True, showmedians=True, showextrema=True, widths=0.9)
    
    plt.xlabel('Groups')
    plt.ylabel('Values')
    plt.title('Violin Plot with Multiple Groups and Intersecting Distributions')


    # plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Violin\Violin_Plot_05.png")
    plt.show()


def violin_plot_6():
    '''This function shows the working of multiple attributes of violin plot WITH intersecting violin plots and saves figure'''

    # Generate synthetic data for demonstration
    np.random.seed(108)
    data1 = np.random.normal(0, 1, 100)
    data2 = np.random.normal(1, 2, 100)
    data3 = np.random.normal(-1, 1.5, 100)
    data4 = np.random.normal(2, 1.2, 100)
    data = [data1, data2, data3, data4]
    
    # Create the violin plot
    violin_parts = plt.violinplot(data, showmeans=True, showmedians=True, showextrema=True, widths=0.9)

    
    # Customizing the colors and transparency
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightyellow']
    for i, pc in enumerate(violin_parts['bodies']):
        pc.set_facecolor(colors[i])
        pc.set_edgecolor('black')
        pc.set_alpha(0.7)
    
    for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians'):
        if partname in violin_parts:
            vp = violin_parts[partname]
            vp.set_edgecolor('black')
            vp.set_linewidth(1)
    
    # Add labels and title
    plt.xticks([1, 2, 3, 4], ['Group 1', 'Group 2', 'Group 3', 'Group 4'])
    plt.xlabel('Groups')
    plt.ylabel('Values')
    plt.title('Violin Plot with Multiple Groups and Intersecting Distributions')
    
    # Save the figure
    # plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Violin\Violin_Plot_06.png")
    plt.show()



# Main
violin_info()
violin_plot_1()
violin_plot_2()
violin_plot_3()
violin_plot_4()
violin_plot_5()
violin_plot_6()



'''
@ Some attributes and Functions of Violin Plots in Matplotlib:

Data Parameters:
dataset: The data to be plotted, which can be a sequence or array of sequences.

Customization Options:
positions: Sets the positions of the violins. Default is 1, 2, 3, ... (depending on the number of datasets).
vert: Whether to plot the violins vertically (True) or horizontally (False). Default is True.
widths: Sets the maximum width of each violin. Default is 0.5.
showmeans: Whether to show the mean of each dataset. Default is False.
showmedians: Whether to show the median of each dataset. Default is False.

showextrema: Whether to show the min/max of each dataset. Default is True.
quantiles: An array of quantiles to be shown on the violin plots.
bw_method: The method used to calculate the estimator bandwidth. Can be 'scott', 'silverman', or a scalar constant.
color: The color of the violin plot. Can be specified for body, points, and lines.
alpha: The transparency level of the violins.

Return Value:
violin_parts: A dictionary containing the bodies, cbars, cmins, cmaxes, and cmeans.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@ Basic Usage:

matplotlib.pyplot.violinplot(dataset, 
                            positions=None, 
                            vert=True, 
                            widths=0.5, 
                            showmeans=False, 
                            showextrema=True, 
                            showmedians=False, 
                            quantiles=None, 
                            points=100, 
                            bw_method=None, 
                            side='both', *, 
                            data=None)


violin_parts = plt.violinplot(data, 
                            showmeans=True, 
                            showmedians=True, 
                            showextrema=True)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@ Customization dummy usage

# Customizing the colors
for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans'):
    vp = violin_parts[partname]
    vp.set_edgecolor('black')
    vp.set_linewidth(1)

for pc in violin_parts['bodies']:
    pc.set_facecolor('lightblue')
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

'''
