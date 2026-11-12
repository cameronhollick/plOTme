# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:38:39 2026

@author: mh2656
"""

# Import packages
from tkinter.filedialog import askdirectory
import pandas as pd
import os
import matplotlib.pyplot as plt
from tqdm import tqdm

# Check run times
print("Welcome to FLASC!")
print()
print("Please select your data folder.")
print()
   
# Load in files
path = askdirectory(title="Select Folder")
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]

# Create plotting loop
for file in csv_files:
    
    for i in tqdm(range(0, 100), desc = "Processing..."):

        # Define data
        df = pd.read_csv(os.path.join(path, file), skiprows=7, sep=",")
        fig, ax = plt.subplots()
        x = df["Mass"]
        y = df["Intensity"]
    
        # Add graph features
        ax.plot(x,y)
        ax.set_xlabel("m/z")
        ax.set_ylabel("Intensity")
    
        # Save files
        no_csv = file.replace(".csv","")
        save_name = no_csv + ".jpg"
        saved = plt.savefig(os.path.join(path, save_name), bbox_inches = 'tight')
        
        # Free up memory
        plt.close()
            
print()
print()
print("All done!")