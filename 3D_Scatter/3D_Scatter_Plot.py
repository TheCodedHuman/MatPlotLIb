#Here we are fabricating functions that show the working of 3D scatter plot


# imports
import matplotlib.pyplot as plt
import pandas as pd


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
    print(f'\n\nThe data we using for 3D scatter plot is: \n\n{df}\n\n')
    print(f'\n\nThe data we using for 3D scatter plot by python\' open() close() is: \n\n{df_}\n\n')


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
    # ax.view_init(elev=30, azim=45)                                                            # explaination of this is given below of whole code, but I think manually we can use however we want, you can uncomment this and experiment
    # ax.grid(True, zorder= 2)
    ax.grid(True)
    plt.show()


def scato_1_3d():
    '''This 3D scatter plot shows the basic and simple scatter plot'''
    fig, ax= basic_structure()
    ax.scatter(time, speed, elevation, label= Label)
    runtheplot('Basic 3D Scatter Plot', ax)





# Main
scato_3D_info()
scato_1_3d()