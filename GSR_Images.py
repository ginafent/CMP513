import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

dir = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\'
file_suffix = '_ECG_GSR_PreProcessed.dat'
output_pdf = 'GSR_by_Clip.pdf'

#NOTE: The clips are all different lengths, so do not compare visually

# Remove old PDF if exists
if os.path.exists(output_pdf):
    os.remove(output_pdf)

label_names = {
    0: "High Arousal, High Valence",
    1: "Low Arousal, High Valence",
    2: "Low Arousal, Low Valence",
    3: "High Arousal, Low Valence",
    4: "Baseline"
}

# Collect GSR signals grouped by clip
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

# Create a PDF — one page per clip
with PdfPages(output_pdf) as pdf:
    for clip, entries in clip_data_dict.items():
        if not entries:
            continue

        plt.figure(figsize=(10, 5))
        plt.title(f"Clip {clip} — Label {entries[0][1]}: {label_names[entries[0][1]]}")
        plt.xlabel("Sample")
        plt.ylabel("GSR Signal")

        for participant_id, label, signal in entries:
            plt.plot(signal, alpha=0.4, linewidth=0.5, label=f"P{participant_id}")

        # Optional: show legend only for few participants to reduce clutter
        if len(entries) < 10:
            plt.legend(fontsize=6)

        plt.tight_layout()
        pdf.savefig()
        plt.close()

print(f"All clip-based plots saved to {output_pdf}")
