import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statistics as stats

df = pd.read_csv('Tunes_csv.csv')
df['Track_Duration_s'] = df['Track_Duration_(ms)'] / 1000
song_lengths = np.array(df.Track_Duration_s)
print(df.head())
Max_length = np.max(song_lengths)
Min_length = np.min(song_lengths)
Avg_length = np.mean(song_lengths)
Med_length = np.median(song_lengths)
q1_length = np.quantile(song_lengths, 0.25)
q3_length = np.quantile(song_lengths, 0.75)
Mode_length = stats.mode(song_lengths)
print('The Longest Song Length is ', Max_length)
print('The Shortest Song Length is ', Min_length) 
print('The Average Song Length is ', Avg_length) 
print('The Most Common Song Length is ', Mode_length)
print('The Quartiles are at ', q1_length, Med_length, q3_length)

ax = plt.subplot()
plt.hist(df.Track_Duration_s, range=(0,Max_length), bins=100)
plt.title('Songs by Length')
plt.xlabel('Song Length (mins)')
plt.ylabel('Count')
plt.axvline(song_lengths.mean(), linestyle='dashed', color='black')
plt.axvline(Med_length, linestyle='dashed', color='red')
plt.axvline(Mode_length, linestyle='dashed', color='yellow')
plt.axvline(q1_length, linestyle='dashed', color='red')
plt.axvline(q3_length, linestyle='dashed', color='red')
plt.legend(['Mean','Quartiles','Mode'])
ax.set_xticks([0,60,120,180,240,300,360,420,480,540,600,660])
ax.set_xticklabels(range(12))
plt.show()