# Import packages
from tkinter import filedialog as fd
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from tqdm import tqdm
from scipy.signal import find_peaks

print("Welcome to MIP!")
print()

# Select and load in CSV
print("Please select your CSV data.")
print()
csv_path = fd.askopenfilename(title="Select CSV")
df = pd.read_csv(csv_path, skiprows=7, sep=",")

# Select and load in ChemDraw
print("Please select your ChemDraw PNG file.")
print()
png_path = fd.askopenfilename(title="Select ChemDraw PNG")
   
# Set desired m/z range
min_mz = input("Enter the minimum m/z you would like to look at: ")
min_mz = float(min_mz)
max_mz = input("Enter the maximum m/z you would like to look at: ")
max_mz = float(max_mz)
df_filtered = df[(df["Mass"] >= min_mz) & (df["Mass"] <= max_mz)].reset_index(drop=True)
print()

# Create plotting loop
for file in tqdm(range(0,100), desc="Processing..."): 

    # Define axes    
    fig, ax = plt.subplots()
    x = df_filtered["Mass"]
    y = df_filtered["Intensity"]
        
    # Detect peaks
    peaks, _ = find_peaks(y, height=y.max() * 0.10, distance=5)
    
    # Add graph features
    ax.plot(x,y)
    ax.set_xlabel("m/z")
    ax.set_ylabel("Intensity")
    ax.set_ylim(0, y.max() * 1.20)
        
    # Label peaks
    for idx in peaks:
        ax.annotate(
        "{:.2f}".format(x[idx]),
        xy=(x[idx], y[idx]),
        xytext=(0,5),
        textcoords="offset points",
        ha="center",
        fontsize=7,
        rotation=90
        )
                
    # Overlay ChemDraw structure_file
    #if structure_file:
        #structure_path = os.path.join(structures_folder, structure_file)
        if os.path.exists(png_path):
            img = mpimg.imread(png_path)
            imagebox = OffsetImage(img, zoom=0.25) # change zoom in script as appropriate
            ab = AnnotationBbox(
            imagebox,
            xy=(0.97, 0.96),
            xycoords="axes fraction",
            box_alignment=(1,1),
            frameon=False
        )
        ax.add_artist(ab)
    
    # Save files
    no_csv = csv_path.replace(".csv","")
    save_name = no_csv + ".jpg"
    saved = plt.savefig(save_name, bbox_inches = 'tight', dpi=300)
        
    # Free up memory
    plt.close()
            
print()
print()
print("All done!")