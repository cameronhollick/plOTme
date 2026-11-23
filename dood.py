# Import packages
from tkinter import filedialog as fd
import pandas as pd
from tqdm import tqdm
import numpy as np

print("Welcome to DOOD!")
print()

# Select and load in CSV
print("Please select your CSV data.")
print()
csv_path = fd.askopenfilename(title="Select CSV")
skip = input("How many rows exist in your CSV before your first data point? (Do not include column headings in this count). ")
skip = int(skip)
all_df = pd.read_csv(csv_path, skiprows=skip, sep=",")

# Select data column to look at
col = input("Which column of your data would you like to calculate outliers for? ")
df = all_df.pop(col)
df = df.to_frame()
   
# Calculate outliers
for i in tqdm(range(0,100), desc="Calculating outliers..."):
    
    # Calculate quartiles
    median = np.quantile(df, 0.5)
    q1 = np.quantile(df,0.25)
    q3 = np.quantile(df,0.75)
    iqr = q3 - q1

    # Calculate fences
    minor_lb = q1 - (1.5 * iqr)
    minor_ub = q3 + (1.5 * iqr)
    major_lb = q1 - (3 * iqr)
    major_ub = q3 + (3 * iqr)

    # Find outliers and prepare lists
    df_minor_lb = df[(df[col] <= minor_lb)]
    df_minor_lb = df_minor_lb[(df_minor_lb[col] >= major_lb)]
    df_major_lb = df[(df[col] <= major_lb)]
    df_minor_ub = df[(df[col] >= minor_ub)]
    df_minor_ub = df_minor_ub[(df_minor_ub[col] <= major_ub)]
    df_major_ub = df[(df[col] >= major_ub)]
    major = pd.concat([df_major_lb, df_major_ub], axis=0)
    minor = pd.concat([df_minor_lb, df_minor_ub], axis=0)

# Processing finished
print()
print("Processing complete.")

# Print outliers
print()
print("The following data points were found to be minor outliers: ")
print(minor)
print()
print("The following  data points were found to be major outliers: ")
print(major)

# Ask about stats
while True:
    
    print()
    param = input("Would you like to view the parameters used to calculate these outliers? (y/n) ")
    
    if param == "y":
        
        # Print quartile data
        print()
        print("The median of your data is: ",median)
        print("The lower quartile of your data is: ",q1)
        print("The upper quartile of your data is: ",q3)
        print("The interquartile range of your data is: ",iqr)
        
        # Print fence data
        print()
        print("The lower bound for minor outliers was: ",minor_lb)
        print("The upper bound for minor outliers was: ",minor_ub)
        print("The lower bound for major outliers was: ",major_lb)
        print("The upper bound for major outliers was: ",major_ub)
        
        print()
        print("Have a great day!")
        
        break
        
    elif param == "n":
        print()
        print("Understood. Have a great day!")
        break
        
    else:
        print()
        print("Input not recognised. Please try again.")