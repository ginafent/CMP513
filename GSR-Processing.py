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
import re


dir = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\'
file_suffix = '_ECG_GSR_PreProcessed.dat'
output_file = 'GSR_all.csv'

files = []
participant_ids = []
df = pd.DataFrame()

# remove file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

first = True

for participant_id in range(101, 134):
    f = f"{dir}{participant_id}{file_suffix}"
    print(' file: ', f)
    
    #participant_ids.append(str(i))
    data = pickle.load(open(f, 'rb'))

    for clip in range(len(data['Data'])):
        clip_data = np.array(data['Data'][clip]) # collect signal array from clip X as numpy array
        #get the first (GSR) column and all rows into signal array
        GSR_signal = clip_data[:, 0]  # in numpy, : means all rows, 0 means first column
        label = data['Labels'][clip]

        df_clip = pd.DataFrame({
            'GSR': GSR_signal,
            'Clip': clip,
            'Participant': participant_id,
            'Label': label
        })
        
        print(' Participant: ', participant_id, 'Label: ', label, ' Clip: ', clip, ' GSR length: ', len(GSR_signal))
        df_clip.to_csv(output_file, mode='a', header=first, index=False)
        first = False


    

