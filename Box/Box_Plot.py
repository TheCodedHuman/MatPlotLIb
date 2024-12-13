# Here we are fabricating functions that shows some use case working of Box Plot in Matplotlib [box plot is also known as whisker plot, but boxprops and whiskerprops plays different working roles]

# imports
import matplotlib.pyplot as plt
import numpy as np


# literals
plt.rcParams['figure.figsize'] = (10, 6)                                                    # generates 100 random data points from a normal distribution (also called Gaussian distribution).

np.random.seed(108)
math_scores = np.random.normal(75, 10, 100)                                                 # Mathematics: Mean 75, Std 10              Group A
science_scores = np.random.normal(70, 15, 100)                                              # Science: Mean 70, Std 15                  Group B
english_scores = np.random.normal(80, 12, 100)                                              # English: Mean 80, Std 12                  Group C

data = [math_scores, science_scores, english_scores]



# defined
def runtheplot(title):
    plt.xlabel('Subjects')
    plt.ylabel('Scores')
    plt.title(title)
    plt.show()


def box_info():
    sp = '~'*100
    print(f"The Math Score are -> {math_scores}\n\n{sp}\n\nThe Science Scores are -> {science_scores}\n\n{sp}\n\nThe English Scores are -> {english_scores}\n\n")


def box_plot_1():
    plt.boxplot(math_scores)
    # plt.boxplot(data)
    runtheplot('Basic Box or Whisker Plot')


def box_plot_2():
    '''This function uses notch, vert, patch_artist'''
    plt.boxplot(data, notch= True, vert= False, patch_artist= True, whis= 0.5)                     # try whis attribute as whis = False and whis=(5, 95) {btw, ts extends or shrinks the extreme(min, max) range allowing or hindering(stopping) outliers to be in the parallel line like looking range}
    runtheplot('Usage of Data Parameters{notch, vert, patch_artist}')


def box_plot_3():
    '''This function uses boxprops, whiskerprops, capprops, flierprops, medianprops, meanprops'''
    plt.boxplot(data,
                patch_artist= True,                                         # This parameter is necessary for applying box properties
                flierprops= dict(marker= '*', color= 'm', alpha= 0.5),
                medianprops= dict(color= 'orange', linewidth= 2),
                meanprops= dict(marker= 'o', markerfacecolor= 'k', markeredgecolor= 'aqua')) 
    runtheplot('Usage of Box Properties{flierprops, medianprops, meanprops}')
    # remember its FLIERprops and not FILTERprops


def box_plot_4():
    '''This function uses showmeans, showextrema, mediansshow'''
    # plt.boxplot(data, patch_artist=True, showmeans= True, showextrema= True, Showmedians= True)
    # runtheplot('Usage of Additional Options{showmeans, showextrema, showmedians')

    plt.boxplot(data,  
                patch_artist=True,
                boxprops= dict(facecolor= 'limegreen', color= 'blue'),
                whiskerprops= dict(color= 'darkblue', linewidth= 1.5),
                capprops= dict(color= 'gold', linewidth= 1.5),
                showmeans=True)
    runtheplot('Usage of Box Properties{boxprops, whiskerprops, capprops} and showmeans')               # there isn't showmedians and showextremas now

    
def box_plot_5():
    '''This function saves image for single box plot'''

    # Generate synthetic and random data
    np.random.seed(0)
    group1 = np.random.normal(0, 1, 100)
    group2 = np.random.exponential(1, 100)
    group3 = np.random.uniform(-2, 2, 100)
    data = [group1, group2, group3]

    # Create a box plot
    plt.figure(figsize=(10, 7))
    plt.boxplot(data, notch=True, vert=True, patch_artist=True,
                boxprops=dict(facecolor='skyblue', color='blue'),
                whiskerprops=dict(color='blue'),
                capprops=dict(color='blue'),
                flierprops=dict(marker='o', color='red', alpha=0.5),
                medianprops=dict(color='red'),
                meanprops=dict(marker='D', markerfacecolor='black', markeredgecolor='black'),
                showmeans=True )

    # Add labels and title
    plt.xlabel('Groups')
    plt.ylabel('Values')
    plt.title('Single Box Plot Example with Multiple Distributions')
    plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])

    # Show plot
    # plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Box\Single_Box_Plot.png")         # we can give dpi = 100; 100 is default, 150-200 is optimal; even 30akes 0 tbit time to load online, 600 qill cook :p
    plt.show()


def box_plot_6():
    '''This function saves image for multiple box plots'''

    # literals
    np.random.seed(108)
    math_scores = np.random.normal(75, 10, 100)  # Mathematics: Mean 75, Std 10
    science_scores = np.random.normal(70, 15, 100)  # Science: Mean 70, Std 15
    english_scores = np.random.normal(80, 12, 100)  # English: Mean 80, Std 12
    data_subjects = [math_scores, science_scores, english_scores]

    group1 = np.random.normal(0, 1, 100)
    group2 = np.random.exponential(1, 100)
    group3 = np.random.uniform(-2, 2, 100)
    data_groups = [group1, group2, group3]

    # defined
    def runtheplot(title):
        plt.suptitle(title, fontsize=16)

    def box_plot_multiple():
        '''Displays multiple box plots in a single figure'''

        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

        # Box plot for subject scores
        axes[0].boxplot(data_subjects, notch=True, patch_artist=True,
                        boxprops=dict(facecolor='lightblue', color='blue'),
                        whiskerprops=dict(color='darkblue', linewidth=1.5),
                        capprops=dict(color='blue', linewidth=1.5),
                        flierprops=dict(marker='o', color='red', alpha=0.5),
                        medianprops=dict(color='green', linewidth=2),
                        meanprops=dict(marker='D', markerfacecolor='black', markeredgecolor='black'),
                        showmeans=True)
        axes[0].set_xticks([1, 2, 3])
        axes[0].set_xticklabels(['Mathematics', 'Science', 'English'])
        axes[0].set_title('Box Plot of Exam Scores')

        # Box plot for different distributions
        axes[1].boxplot(data_groups, notch=True, patch_artist=True,
                        boxprops=dict(facecolor='lightcoral', color='red'),
                        whiskerprops=dict(color='darkred', linewidth=1.5),
                        capprops=dict(color='red', linewidth=1.5),
                        flierprops=dict(marker='o', color='blue', alpha=0.5),
                        medianprops=dict(color='orange', linewidth=2),
                        meanprops=dict(marker='D', markerfacecolor='black', markeredgecolor='black'),
                        showmeans=True)
        axes[1].set_xticks([1, 2, 3])
        axes[1].set_xticklabels(['Group 1', 'Group 2', 'Group 3'])
        axes[1].set_title('Box Plot of Different Distributions')

        # Adjust layout and show plot
        plt.tight_layout()
        runtheplot('Multiple Box Plots by Subplots')
        # plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Box\Multiple_Box_Plots.png")

    # Call the function to create the plot
    box_plot_multiple()
    plt.show()



# Main
# box_info()
# box_plot_1()
# box_plot_2()
# box_plot_3()
# box_plot_4()
# box_plot_5()
# box_plot_6()



'''
@ Some attributes and Functions for Box Plots:

Data Parameters:
x: The data to be plotted, which can be a sequence or an array of sequences.
notch: Whether to display a notched box plot (True or False).
vert: Whether to display the box plot vertically (True) or horizontally (False).
patch_artist: Whether to fill the box with color (True or False).
whis: The length of the whiskers, specified as a float (multiple of the IQR), a tuple (percentiles), or 'range' (min and max).

Box Properties:
boxprops: Dictionary of properties for the boxes, such as facecolor and edgecolor.
whiskerprops: Dictionary of properties for the whiskers, such as color and linewidth.
capprops: Dictionary of properties for the caps, such as color and linewidth.
flierprops: Dictionary of properties for the outliers, such as marker, markerfacecolor, markeredgecolor, and alpha.
medianprops: Dictionary of properties for the medians, such as color and linewidth.
meanprops: Dictionary of properties for the mean markers, such as marker, markerfacecolor, and markeredgecolor.

Additional Options:
showmeans: Whether to show the means as points (True or False).
showextrema: Whether to show the extrema (minimum and maximum) values (True or False).
showmedians: Whether to show the medians (True or False).
'''

