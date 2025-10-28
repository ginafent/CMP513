#This file is to extract the GSR features

'''
We want:
Participant ID, Clip Number, Label, 
GSR Mean, GSR Std, Min-Max, Num of peaks?, Post Valence, Post Arousal

TODO: Check data is comparible
'''
import pickle
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

dir = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\'
file_suffix = '_ECG_GSR_PreProcessed.dat'
output_file = 'GSR_Features_Data.csv'

label_names = {
    0: "High Arousal, High Valence",
    1: "Low Arousal, High Valence",
    2: "Low Arousal, Low Valence",
    3: "High Arousal, Low Valence",
    4: "Baseline"
}


files = []
participant_ids = []
df = pd.DataFrame()

# remove file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

first = True

for participant_id in range(101, 134):
    f = f"{dir}{participant_id}{file_suffix}"
    if os.path.exists(f):
        files.append(f)
        print(' file: ', f)


clip_data_dict = {i: [] for i in range(13)}  # up to 13 clips (some have 12, some 13)

for i in range(101, 134):
    f = os.path.join(dir, f"{i}{file_suffix}")
    if not os.path.exists(f):
        print(f"Missing file: {f}")
        continue

    data = pickle.load(open(f, 'rb'))
    labels = data['Labels']

    for clip in range(len(data['Data'])):
        clip_data = np.array(data['Data'][clip])
        GSR_signal = clip_data[:, 0]
        label = labels[clip]
        clip_data_dict[clip].append((i, label, GSR_signal))

gsr_features = []

for participant_id in range(101, 134):
    f = os.path.join(dir, f"{participant_id}{file_suffix}")
    if not os.path.exists(f):
        print(f"Missing file: {f}")
        continue

    data = pickle.load(open(f, 'rb'))
    labels = data['Labels']

    for clip in range(len(data['Data'])):
        GSR_signal = np.array(data['Data'][clip])[:, 0]
        label = labels[clip]

        gsr_features.append({
            'Participant': participant_id,
            'GSR Mean': np.mean(GSR_signal),
            'GSR SD': np.std(GSR_signal),
            'GSR Range': np.max(GSR_signal) - np.min(GSR_signal),
            'Clip': clip,
            'Label': label            
        })

df_features = pd.DataFrame(gsr_features)
df_features['Label_Name'] = df_features['Label'].map(label_names)
df_features.to_csv(output_file, index=False)
print("Saved ", output_file)





