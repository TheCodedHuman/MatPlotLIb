# Here we are fabricating a program to show subplots of various plots

# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# literals
np.random.seed(108)
data = {
    'Student ID' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Subject' : ['Math', 'Math', 'Science', 'Science', 'English', 'English', 'History', 'History', 'Math', 'Math'],
    'Score' : [85, 90, 78, 88, 92, 85, 75, 80, 70, 95],
    'Gender' : ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Age' : np.random.randint(15, 25, 10),
    'color' : ['blue', 'female', 'blue', 'female', 'blue', 'female', 'blue', 'female', 'blue', 'female']
} 
df = pd.DataFrame(data)



# Defined
def info(): print(f"\n{df}\n")

def scato():
    axs[0, 0].scatter(df['Age'], df['Score'], c=df['Gender'].apply(lambda x: 'blue' if x == 'Male' else 'pink'), s = 250, zorder = 2)
    axs[0, 0].set_title('Scatter Plot: Score vs Age')
    axs[0, 0].set_xlabel('Age')
    axs[0, 0].set_ylabel('Score')
    axs[0, 0].grid(True, zorder = 1)

def histo():
    axs[0, 1].hist(df['Score'].unique(), bins=10, color='green', alpha=0.85, zorder = 2)
    axs[0, 1].set_title('Histogram: Score Frequency')
    axs[0, 1].set_xlabel('Score')
    axs[0, 1].set_ylabel('Frequency')
    axs[0, 1].grid(True, zorder = 1, alpha = 0.7)

def line():
    
    # # bit complex but basic python and pandas functionality
    # for subject in df['Subject'].unique():  
    #     subject_data = df[df['Subject'] == subject]     # df[something] accesses the column directly without filtering, whereas df[df[something]] applies a condition to filter rows based on the column's values)
    #     axs[1, 0].plot(subject_data['Student ID'], subject_data['Score'], marker='o', label=subject, zorder = 2)
    

    # same and simple to above but uses groupby
    grouped = df.groupby('Subject')                 # Group the dataframe by 'Subject'
    for name, group in grouped:                     # Plot each group
        axs[1, 0].plot(group['Student ID'], group['Score'], marker='o', label=name, zorder = 2)


    axs[1, 0].set_title('Line Chart: Score by Student ID')
    axs[1, 0].set_xlabel('Student ID')
    axs[1, 0].set_ylabel('Score')
    axs[1, 0].legend()
    axs[1, 0].grid(True, linestyle = "dashdot", alpha = 0.7, zorder = 1)

    

def plotto():
    gender_count = df['Gender'].value_counts()              # Value counts is a function of pandas library
    axs[1, 1].pie(gender_count, labels = gender_count.index, autopct = '%1.1f%%', colors = ['blue', 'pink'])
    axs[1, 1].set_title('Pie Chart: Distribution by Gender')










# Main

fig, axs = plt.subplots(2, 2, figsize = (12, 10))
# fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 10), dpi=100, sharex=False, sharey=False, gridspec_kw={'wspace': 0.3, 'hspace': 0.4})


info()
scato()
histo()
line()
plotto()
plt.tight_layout()

# Save the figure with various attributes
plt.savefig(
    r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\Graph_Images\Sub_Plot\Sub_Plotter.png',       # Filename            # This was just the file location on my pc, you can tweak as per your's
    dpi=300,                                                                                        # Resolution
    facecolor='white',                                                                              # Background color
    edgecolor='black',                                                                              # Edge color
    transparent=True,                                                                              # Transparency
    bbox_inches='tight',                                                                            # Tight bounding box to remove extra whitespace
    pad_inches=0.1,                                                                                 # Padding around the figure
    format='png'                                                                                    # File format
)

plt.show()





'''

@ Key attributes of subplot()

nrows:
Type: int
Description: Number of rows of subplots.
Example: nrows=2

ncols:
Type: int
Description: Number of columns of subplots.
Example: ncols=2

sharex:
Type: bool or {'none', 'all', 'row', 'col'}, default: False
Description: Whether the subplots share the x-axis. If True, the x-axis will be shared among all subplots.
Example: sharex=True

sharey:
Type: bool or {'none', 'all', 'row', 'col'}, default: False
Description: Whether the subplots share the y-axis. If True, the y-axis will be shared among all subplots.
Example: sharey=True

subplot_kw:
Type: dict, optional
Description: Dictionary with keywords passed to the add_subplot call to add each subplot to the figure.
Example: subplot_kw={'projection': 'polar'}

gridspec_kw:
Type: dict, optional
Description: Dictionary with keywords passed to the GridSpec constructor to create the grid the subplots are placed on.
Example: gridspec_kw={'wspace': 0.3, 'hspace': 0.3}

figsize:
Type: tuple, optional
Description: Width and height in inches.
Example: figsize=(10, 8)

dpi:
Type: int, optional
Description: The resolution of the figure in dots per inch.
Example: dpi=100

num:
Type: int or str, optional
Description: A unique identifier for the figure.
Example: num=1



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@ Key attributes of Savefig()

fname:
Type: string
Description: The filename or the path where the image will be saved. The file extension determines the format (e.g., .png, .pdf, .svg).

dpi:
Type: float or 'figure'
Description: The resolution of the output file in dots per inch. Higher values produce higher quality images.
Example: dpi=300

facecolor:
Type: color or 'auto'
Description: The background color of the figure. Can be any color specification that Matplotlib understands.
Example: facecolor='white'

edgecolor:
Type: color or 'auto'
Description: The border color of the figure.
Example: edgecolor='black'

orientation:
Type: 'landscape' or 'portrait'
Description: The orientation of the saved figure.

format:
Type: string
Description: The file format (e.g., 'png', 'pdf', 'svg', 'ps', 'eps'). If not specified, it is inferred from the file extension in fname.
Example: format='png'

transparent:
Type: boolean
Description: If True, the background will be transparent. Useful for presentations or overlays.
Example: transparent=True

bbox_inches:
Type: string, scalar, or tuple
Description: Bounding box in inches. 'tight' removes any extra whitespace around the plot.
Example: bbox_inches='tight'

pad_inches:
Type: float
Description: Amount of padding around the figure when bbox_inches is 'tight'.
Example: pad_inches=0.1

metadata:
Type: dictionary
Description: Metadata to include in the file (e.g., title, author, subject).
'''

