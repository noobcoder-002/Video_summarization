import matplotlib.pyplot as plt
import pandas as pd


csv_filename = 'relevance_scores.csv'
df = pd.read_csv(csv_filename)

filenames = df['Image Filename']
scores = df['Relevance Score']

plt.figure(figsize=(12, 6))
bars = plt.bar(filenames, scores, color='b', alpha=0.7)
plt.ylabel('Relevance Score')
plt.title('Relevance Scores for Frames')


plt.xticks([])


plt.show()
