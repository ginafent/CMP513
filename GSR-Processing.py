#Georgina Fenton
#Student ID: 2404965
#CMP513, User Experience Research, Unit 1

#This program is to cleanse the ESG-GSR .dat files corresponding with each participant in the VREED data.
#I want a CSV with each participant's ID, and their aggregated GSR data per video

import pickle
import os
import pandas as pd
import numpy as np

file = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\101_ECG_GSR_PreProcessed.dat'
dir = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\'
file_suffix = '_ECG_GSR_PreProcessed.dat'

files = []
for i in range(101, 134):
    files.append(dir + str(i) + file_suffix)


data = pickle.load(open(file, 'rb'))
#keys(['Labels', 'Data'])

print("Labels:", data['Labels'])
print("Data:", data['Data'])

# Check the shape and type of Data
print("Data type:", type(data['Data']))

for i, vid in enumerate(data['Data']):
    gsr_len = len(vid[0])
    ecg_len = len(vid[1])
    print(f"Video {i}: GSR len={gsr_len}, ECG len={ecg_len}")


import matplotlib.pyplot as plt

for i, vid in enumerate(data['Data']):
    print(f"Video {i}, Label {data['Labels'][i]}:")
    print("  GSR:", vid[0])
    print("  ECG:", vid[1])


rows = []
labels = data['Labels']

for i, vid in enumerate(data['Data']):
    #vid[0] is the GSR data, so we don't need vid[1]
    gsr1, gsr2 = vid[0]
    rows.append({
        'Index': i,
        'Label': labels[i],
        'GSR_Feature1': gsr1,
        'GSR_Feature2': gsr2
    })

df = pd.DataFrame(rows)
print(df)