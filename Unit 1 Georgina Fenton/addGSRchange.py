import pandas as pd

df = pd.read_csv("Combined_Data.csv")
rows = []

# Loop through participants
for pid, group in df.groupby("Participant"):
    # Find baseline mean for this participant
    baseline = group.loc[group["Label"] == 4, "GSR Mean"]
    if baseline.empty:
        continue  # skip if no baseline for this participant
    baseline_mean = baseline.iloc[0]

    # Compute change for each clip
    group["GSR Change"] = group["GSR Mean"] - baseline_mean
    rows.append(group)

# Combine all participant groups back together
df_change = pd.concat(rows)
df_change.to_csv("GSR_withChange.csv", index=False)
print("Saved GSR_withChange.csv")
