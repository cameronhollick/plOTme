## plOTme: A little set of scripts for visualising Orbitrap data
A few Python scripts designed to aid in the plotting of MS2 and associated HPLC data obtained on an Orbitrap. After initial data processing in FreeStyle, export your data in CSV format, load things into the relevant script, and let Python take care of the rest.

### How to install

1) Download this repo as a ZIP file and extract it to get access to the scripts.
2) Open a terminal with ```pip``` installed, and create a virtual environment (venv) to complete the installation in.
3) Activate your venv and enter the command ```pip install plOTme-for-Orbitrap``` to get the newest version from PyPI.
4) Open the script you want to use in your IDE of choice (I recommend Spyder).
5) Click run, select the folder containing your data files, and let plOTme do its work!

### General-purpose scripts

***FLASC:*** <ins>F</ins>u<ins>l</ins>l m<ins>as</ins>s spe<ins>c</ins>trometry plots. Feed a folder with your CSVs into the script, and it'll plot up all your data into individual MS1 spectra.

***FLEX:*** <ins>F</ins>u<ins>l</ins>l <ins>ex</ins>tracted ion chromatograms. Feed a folder with your CSVs into the script, and it'll plot up all your data into individual EICs. Also works with TICs!

### Scripts for studying isotope patterns

***MIP:*** <ins>M</ins>olecular <ins>i</ins>on <ins>p</ins>eak plotting. Upload a CSV, specify the m/z of your molecular ion peak, and get the zoomed MS1 spectrum out of the other end.
*With thanks to Zak Freear for coding the backbone of this script.*

***MIP-FLASC:*** Study multiple CSVs at once. Coming soon.

### Scripts for studying changing injection volumes

***SINCH:*** <ins>S</ins>tudying <ins>in</ins>jection volumes by <ins>ch</ins>romatogram comparison. Designed for plotting chromatograms on the same set of axes where the independent factor is the injection volume (i.e. runtime is the same across all samples). By default, reads the first 5 CSV files in a user-specified folder and assigns them to 1, 2, 5, 10 and 20 μL (can be changed in the script).

***SINTA:*** <ins>S</ins>tudying <ins>in</ins>jection volumes by <ins>ta</ins>ndem mass spectrometry. Coming soon.
