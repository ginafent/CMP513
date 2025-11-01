import pickle

file_path = 'VREED Data\\05 ECG-GSR Data\\01 ECG-GSR Data (Pre-Processed)\\101_ECG_GSR_PreProcessed.dat'

with open(file_path, 'rb') as f:
    data = pickle.load(f)

# See what keys exist
print(data.keys())

for key in data.keys():
    print(f"\n=== {key} ===")
    print(type(data[key]))
    if isinstance(data[key], list):
        print("First few items:", data[key][:5])
    elif isinstance(data[key], dict):
        print("Keys:", list(data[key].keys()))
    else:
        print(data[key])

print("Number of clips in Data:", len(data['Data']))
print("Length of Labels:", len(data['Labels']))
