#Georgina Fenton
#Student ID: 2404965
#CMP513, User Experience Research, Unit 1

#This program is to cleanse the ESG-GSR .dat files corresponding with each participant in the VREED data.
#I want a CSV with each participant's ID, and their aggregated GSR data per video

import pickle
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\101_ECG_GSR_PreProcessed.dat'
dir = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\'
file_suffix = '_ECG_GSR_PreProcessed.dat'
files = []
df = pd.DataFrame()
participant_id = 101


output_file = 'GSR_all.csv'

# remove file if it exists
if os.path.exists(output_file):
    os.remove(output_file)


for i in range(101, 134):
    files.append(dir + str(i) + file_suffix)

all_rows = []

for f in files:
    print(' file: ', f)
    #the data appears to have been pickled, so we use pickle to load it
    #I verified this previously by printing the first few bytes of the file (which showed pickle header)
    data = pickle.load(open(f, 'rb'))

    #the clips we will iterate through (0-11) 

    for clip in range(len(data['Data'])):  
        clip_data = np.array(data['Data'][clip]) # collect signal array from clip X as numpy array
        #get the first (GSR) column and all rows into signal array
        GSR_signal = clip_data[:, 0]  # in numpy, : means all rows, 0 means first column
        
        df = pd.DataFrame({'GSR': GSR_signal, 'Clip': clip, 'Participant': participant_id})

        df.to_csv(output_file, mode='a', header=not os.path.exists(output_file), index=False)


''' 
plt.figure(figsize=(10,4))
plt.plot(GSR_signal)
plt.title("GSR Signal for 101 - Clip " + str(clip))
plt.xlabel("Samples")
plt.ylabel("GSR")
plt.show() '''

#df = pd.DataFrame(GSR_signal, columns=['GSR'])
