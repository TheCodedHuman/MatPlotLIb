# imports
import matplotlib.pyplot as plt
import numpy as np

# literals
plt.rcParams['figure.figsize'] = (12, 8)

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
    runtheplot('Multiple Box Plots in a Single Figure')
    plt.savefig(r"D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Box\Multiple_Box_Plots.png")
    plt.show()

# Call the function to create the plot
box_plot_multiple()
