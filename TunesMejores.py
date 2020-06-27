import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import statistics as stats

df = pd.read_csv('Tunes_csv.csv')
df['Track_Duration_s'] = df['Track_Duration_(ms)'] / 1000
song_lengths_t = np.array(df.Track_Duration_s)
print(df.head())

Max_length = np.max(song_lengths_t)
Min_length = np.min(song_lengths_t)
Avg_length = np.mean(song_lengths_t)
Med_length = np.median(song_lengths_t)
q1_length = np.quantile(song_lengths_t, 0.25)
q3_length = np.quantile(song_lengths_t, 0.75)
Mode_length = stats.mode(song_lengths_t)

df2 = pd.read_csv('Mejores_CSV.csv')
df2['Track_Duration_s'] = df2['Track_Duration_ms'] / 1000
song_lengths_m = np.array(df2.Track_Duration_s)
print(df2.head())

Max_length_t = np.max(song_lengths_m)
Min_length_t = np.min(song_lengths_m)
Avg_length_t = np.mean(song_lengths_m)
Med_length_t = np.median(song_lengths_m)
q1_length_t = np.quantile(song_lengths_m, 0.25)
q3_length_t = np.quantile(song_lengths_m, 0.75)
Mode_length_t = stats.mode(song_lengths_m)

print('The Longest Song Lengths are ', Max_length, Max_length_t)
print('The Shortest Song Lengths are ', Min_length, Min_length_t) 
print('The Average Song Lengths are ', Avg_length, Avg_length_t) 
print('The Most Common Song Lengths are ', Mode_length, Mode_length_t)

ax = plt.subplot(313)
plt.hist([df.Track_Duration_s, df2.Track_Duration_s], range=(0,Max_length), bins=100, histtype='step', density=True)
plt.title('Songs by Length')
plt.xlabel('Song Length (mins)')
ax.set_xticks([0,60,120,180,240,300,360,420,480,540,600,660])
ax.set_xticklabels(range(12))

ax2 = plt.subplot(312)
plt.hist(df2.Track_Duration_s, range=(0,Max_length), bins=100, color='orange', density=True)
plt.title('Mejores Songs by Length')
plt.xlabel('Song Length (mins)')
plt.axvline(song_lengths_m.mean(), linestyle='dashed', color='black')
plt.axvline(Med_length_t, linestyle='dashed', color='red')
ax2.set_xticks([0,60,120,180,240,300,360,420,480,540,600,660])
ax2.set_xticklabels(range(12))

ax3 = plt.subplot(311)
plt.hist(df.Track_Duration_s, range=(0,Max_length), bins=100, density=True)
plt.title('Tunes Songs by Length')
plt.xlabel('Song Length (mins)')
plt.axvline(song_lengths_t.mean(), linestyle='dashed', color='black')
plt.axvline(Med_length, linestyle='dashed', color='red')
ax3.set_xticks([0,60,120,180,240,300,360,420,480,540,600,660])
ax3.set_xticklabels(range(12))

plt.legend(['Mean', 'Median'])
plt.subplots_adjust(hspace=1)
plt.show()