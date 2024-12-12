# Here we are fabricating functions that shows some use case working of Box Plot in Matplotlib [box plot is also known as whisker plot]

# imports
import matplotlib.pyplot as plt
import numpy as np


# literals
plt.rcParams['figure.figsize'] = (10, 6)                                                    # generates 100 random data points from a normal distribution (also called Gaussian distribution).

np.random.seed(108)
math_scores = np.random.normal(75, 10, 100)                                                 # Mathematics: Mean 75, Std 10
science_scores = np.random.normal(70, 15, 100)                                              # Science: Mean 70, Std 15
english_scores = np.random.normal(80, 12, 100)                                              # English: Mean 80, Std 12

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
    plt.boxplot(data)
    runtheplot('Basic Box or Whisker Plot')


def box_plot_2():
    pass



def box_plot_n():
    import matplotlib.pyplot as plt
    import numpy as np

    # Generate synthetic data
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
                showmeans=True, meanprops=dict(marker='D', markerfacecolor='black', markeredgecolor='black'))

    # Add labels and title
    plt.xlabel('Groups')
    plt.ylabel('Values')
    plt.title('Custom Box Plot Example with Multiple Distributions')
    plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])

    # Show plot
    plt.show()



# Main
# box_info()
# box_plot_1()
# box_plot_n()




'''
@ Some attributes and Functions for Box Plots:

Data Parameters:
x: The data to be plotted, which can be a sequence or an array of sequences.
notch: Whether to display a notched box plot (True or False).
vert: Whether to display the box plot vertically (True) or horizontally (False).
patch_artist: Whether to fill the box with color (True or False).

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


