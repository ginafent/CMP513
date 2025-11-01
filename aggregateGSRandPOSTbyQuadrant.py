import pandas as pd
import numpy as np

# Assume your GSR features CSV has columns:
# 'Participant', 'Clip', 'Label', 'GSR_Mean', 'GSR_SD'
gsr_df = pd.read_csv('Combined_Data.csv')

# Aggregate mean GSR per Label (quadrant) per participant
gsr_agg = gsr_df.groupby(['Participant', 'Label']).agg({
    'GSR Mean': 'mean',
    'GSR SD': 'mean'  # or 'std' if you prefer
}).reset_index()

post_df = pd.read_excel("VREED Data/03 Self-Reported Questionnaires/02 Post Exposure Ratings.xlsx")  # your POST CSV
# Example columns: ID, Quad_Cat, POST_Valence, POST_Arousal, etc.

# Aggregate mean self-report per quadrant per participant
post_agg = post_df.groupby(['ID', 'Quad_Cat']).agg({
    'POST_Valence': 'mean',
    'POST_Arousal': 'mean',
    # include any other POST columns you want
}).reset_index()

merged_agg = pd.merge(
    gsr_agg,
    post_agg,
    left_on=['Participant', 'Label'],
    right_on=['ID', 'Quad_Cat'],
    how='inner'
)

merged_agg.to_csv("merged_agg.csv", index=False)