# Here we are fabricating a program for functions of Pie Chart

# imports
import matplotlib.pyplot as plt


# literals
x = [25, 35, 20, 10, 10]                                    # Actual Data
y = ['Math', 'Science', 'English', 'History', 'Art']        # Useful for labels
c = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']     # Colors for each category, we can also give words like lightcoral, Cornflowerblue, palegreen, Navojowhite, Lightsteelblue
exp = (0.1, 0, 0, 0, 0)                                     # For Explode attribute
plt.rcParams['figure.figsize'] = (10, 6)                    # Changing default figsize values


# Defined
def title_show(title):
    plt.title(title, fontsize = 20)
    plt.show()  
    
def plotto_info(): print(f''' 

The Data we used here for plotting was -> \t{x}

                    And
                    
The Labels we used for the plotting data was -> \t{y}

''')
        

def pie_plot_1():
    plt.pie(x, labels=y)
    title_show('Basic Pie Plot')


def pie_plot_2():
    plt.pie(x)
    plt.legend(labels=y, loc='lower right')                 # We can just give `y` as at first place, without 'labels', loc can be -> [0, 10] where 0, 10 are included
    title_show('Use Of Legend Only, Without Separate Labels')
    plt.show()


def pie_plot_3():
    plt.pie(x,                                              # wedge:x (slice information)
            labels=y,                                       # labels:y
            colors=c,                                       # colors give colors to each slice
            explode=exp)                                    # explode separates specific slices

    # plt.pie(x,labels=y,colors=c,explode=exp)              # same as upper code snippet
    title_show('Usage of Data, Labels, Colors, Explode')


def pie_plot_4():
    plt.pie(x,
            labels=y, 
            colors=c,
            autopct='%1.1f%%',                              # Shows Percentage
            shadow=True,                                    # Adds Shadow 
            radius=1.5,                                     # Radius of pie chart
            labeldistance=1.15)                             # Distance of labels from center (Inches or DPI [Dots Per Inch])
    plt.legend(labels= y, loc=7)
    title_show('Usage of AutoCPT, Shadow, Radius, LabelDistance')


def pie_plot_5():
    plt.pie(x,
            labels=y, 
            startangle=90,                                  # Sets starting angle of pie chart
            textprops={'fontsize': 12, 'color' : 'blue'},   # Customizing properties of text labels
            counterclock=False,                             # Direction of flow of pie chart
            wedgeprops={'linewidth':3, 'edgecolor':'gold'}) # Customizing properties of wedges/slices
            
    plt.legend(labels= y, loc=10)
    title_show('Usage of StartAngle, TextProps, CounterClock, WedgeProps')


def pie_plot_6():
    plt.pie([1])
    title_show('Dot Pie Chart')


def pie_plot_7():
    x2 = [80, 32, 56]
    plt.pie(x, labels=y)
    plt.pie(x2, radius=0.5)
    title_show('Nested Pie Charts')

def pie_plot_8():
    def way_1():
        plt.pie(x, labels=y, radius=1.5)
        cr= plt.Circle(xy=(0, 0), radius=1.2, facecolor='white')
        plt.gca().add_artist(cr)
        title_show('Usage of Circle() and gca()')

    def way_2():
        plt.pie(x)
        plt.pie([1], colors='white', radius=0.75)
        plt.legend(y, loc='center')
        title_show('Usage Of Dot Pie Chart')

    way_1()
    way_2()


def pie_plot_9(filename='Saving_Da_Pie.png'):
    fig, ax = plt.subplots()

    # Plotting the pie chart with various attributes
    wedges, texts, autotexts = ax.pie(x,
                                      labels=y,
                                      colors=c,
                                      explode=exp,
                                      autopct='%1.1f%%',
                                      startangle=140,
                                      labeldistance=1.1,
                                      textprops={'fontsize': 12},
                                      wedgeprops={'linewidth': 1, 'edgecolor': 'black'},
                                    #   frame=True,                                       # Helps in making frame around pie chart
                                    #   center=(0, 5),                                    # See the outer frame 0(x) and 5(y) values
                                    #   rotatelabels=True,                                # Sets some rotation to the labels
                                    #   pctdistance=0.85,                                 # Distance of percentages from center
                                      shadow=True)

    # Customizing the text and autotexts
    for text in texts:
        text.set_color('navy')
    for autotext in autotexts:
        autotext.set_color('white')

    # Adding a legend
    ax.legend(wedges, y, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Setting the title
    plt.title('Distribution of Students by Favorite Subject', fontsize=18)              # If we use title_show() here the title may not be used correctly 

    # Saving the figure
    plt.savefig(f'D:\\Bhaiyu Ki Files Aur Samaan\\NewEraOfPython\\MatPlotLIb\\Graph_Images\Pie\\{filename}')            # This was just the file location on my pc, you can tweak as per your's
    print(f"Figure saved as {filename}")
    plt.show()


# Main
# plotto_info()
# pie_plot_1()
# pie_plot_2()
# pie_plot_3()
# pie_plot_4()
# pie_plot_5()
# pie_plot_6()
# pie_plot_7()
# pie_plot_8()
# pie_plot_9()




'''
@} Key Attributes for pie():

x: The Data we using for pie chart
labels: Displays labels for each wedge.
colors: Custom colors for each wedge.
explode: Pulls out the first wedge.

autopct: Shows the percentage for each wedge.
shadow: Adds a shadow beneath the pie chart.
radius: Sets the radius of the pie chart.
labeldistance: Sets the distance of the labels from the center.

startangle: Sets the starting angle of the pie chart.
textprops: Customizes the properties of the text labels.
counterclock: Draws the wedges clockwise.
wedgeprops: Customizes the properties of the wedges.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@ Some Useful Kwargs (Keyword-Arguements)

pctdistance: Position of percentage text.
center: Position of center.
frame: Draw frame.
rotatelabels: Rotate labels.
'''

