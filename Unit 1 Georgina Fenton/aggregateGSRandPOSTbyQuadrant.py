import pandas as pd
import numpy as np

gsr_df = pd.read_csv('GSR_withChange.csv')


gsr_agg = gsr_df.groupby(['Participant', 'Label']).agg({
    'GSR Mean': 'mean',
    'GSR SD': 'mean',
    'GSR Change': 'mean'
}).reset_index()

post_df = pd.read_excel("VREED Data/03 Self-Reported Questionnaires/02 Post Exposure Ratings.xlsx")

# Aggregate mean self-report per quadrant per participant
#Note, baseline gets dropped since it wasn't included in the POST data
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

merged_agg.to_csv("GSR_Post_Data_Merged.csv", index=False)