#Here we are fabricating a simple program demonstrating the easy read_csv

# imports
import pandas as pd


# literals
csv_file_path = r'D:\Bhaiyu Ki Files Aur Samaan\NewEraOfPython\MatPlotLIb\3D_Scatter\Sample_Data.csv'


# defined
df = pd.read_csv(csv_file_path)


# Main
print(df)
