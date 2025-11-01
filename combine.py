#Combine GSR and Self-Report Data
#Use Num Code and 'Clip' as corresponding keys

import pandas as pd

# Load the data
gsr_df = pd.read_csv("Combined_Data.csv")
post_df = pd.read_excel("VREED Data/03 Self-Reported Questionnaires/02 Post Exposure Ratings.xlsx")

# Ensure the linking columns are the same type
gsr_df['Participant'] = gsr_df['Participant'].astype(int)
post_df['ID'] = post_df['ID'].astype(int)

# Merge on Participant and Clip ↔ Num_Code
merged_df = pd.merge(
    gsr_df,
    post_df,
    left_on=['Participant', 'Clip'],
    right_on=['ID', 'Num_Code'],
    how='inner'
)

# Optional: Drop redundant columns (like 'ID' or 'Trial_Num')
merged_df = merged_df.drop(columns=['ID'])

# Save
merged_df.to_csv("Merged_GSR_POST.csv", index=False)

print("Merged dataset shape:", merged_df.shape)
print(merged_df[['Participant', 'GSR Mean', 'Clip', 'Num_Code', 'Quad_Cat']].head())

