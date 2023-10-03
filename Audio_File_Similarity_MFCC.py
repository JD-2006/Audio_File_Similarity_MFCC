import os
import pathlib
import librosa
import librosa.display
import matplotlib.pyplot as plt
from dtw import *

# File paths for audio files
audio_file1 = r"C:\Users\test\Downloads\audio1.wav"
audio_file2 = r"C:\Users\test\Downloads\audio2.wav"

# Loading audio files
y1, sr1 = librosa.load(audio_file1)
y2, sr2 = librosa.load(audio_file2)

# Displaying MFCC plots
plt.subplot(1, 2, 1)
mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1)
librosa.display.specshow(mfcc1)

plt.subplot(1, 2, 2)
mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2)
librosa.display.specshow(mfcc2)

# Computing DTW
alignment = dtw(mfcc1.T, mfcc2.T, keep_internals=True)
dist = alignment.normalizedDistance
path = alignment.index1

print("The normalized distance between the two audio files:", dist)

# Visualizing DTW
plt.imshow(alignment.costMatrix.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
plt.plot(path[0], path[1], 'w')  # Creating plot for DTW

plt.show()  # To display the plots graphically
