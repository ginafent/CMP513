import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

dir = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\'
file_suffix = '_ECG_GSR_PreProcessed.dat'
output_pdf = 'GSR_waveforms.pdf'

pdf = PdfPages(output_pdf)

for i in range(101, 134):
    f = os.path.join(dir, f"{i}{file_suffix}")
    if not os.path.exists(f):
        print(f"Missing file: {f}")
        continue

    data = pickle.load(open(f, 'rb'))
    labels = data['Labels']

    # Loop through clips for this participant
    for clip in range(len(data['Data'])):
        clip_data = np.array(data['Data'][clip])
        GSR_signal = clip_data[:, 0]
        label = labels[clip]

        # Plot GSR waveform
        plt.figure(figsize=(8, 3))
        plt.plot(GSR_signal, linewidth=0.6)
        plt.title(f"Participant {i} | Clip {clip} | Label {label}")
        plt.xlabel("Sample")
        plt.ylabel("GSR")
        plt.tight_layout()

        # Add page to PDF
        pdf.savefig()
        plt.close()

pdf.close()
print(f"✅ All waveform plots saved to {output_pdf}")