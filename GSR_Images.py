import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

dir = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\'
file_suffix = '_ECG_GSR_PreProcessed.dat'
output_pdf = 'GSR_by_Label.pdf'

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

# Prepare dictionary to collect signals by label
label_data = {k: [] for k in range(5)}

# Gather all data
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
        label_data[label].append((i, clip, GSR_signal))  # (participant ID, clip number, signal)

# Create PDF
with PdfPages(output_pdf) as pdf:
    for label, entries in label_data.items():
        if not entries:
            continue

        plt.figure(figsize=(10, 5))
        plt.title(f"Label {label}: {label_names[label]}")
        plt.xlabel("Sample")
        plt.ylabel("GSR Signal")

        for participant_id, clip, signal in entries:
            plt.plot(signal, alpha=0.4, linewidth=0.5, label=f"P{participant_id}-C{clip}")

        # Optional: legend only if <10 traces (avoids clutter)
        if len(entries) < 10:
            plt.legend(fontsize=6)

        plt.tight_layout()
        pdf.savefig()
        plt.close()

print(f"All label-based plots saved to {output_pdf}")
