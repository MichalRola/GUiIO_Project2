import os

import librosa
import numpy as np
from librosa.feature import mfcc
from tqdm import tqdm


def get_mfcc(filename):
    file_paths = [os.path.join(filename, x) for x in os.listdir(filename)]
    genres = os.listdir(filename)
    audio_paths = []
    for path in tqdm(file_paths):
        for file in os.listdir(path):
            audio_paths.append(os.path.join(path, file))

    # Generate data for the model
    data = []
    labels = []
    for path in tqdm(audio_paths):
        genre = path.split('\\')[2]  # Extract genre from file path
        try:
            fmccs = get_frame_mfccs(path)
            for frame in fmccs:
                data.append(frame)
                labels.append(genre)
        except Exception:
            pass
    processed_data = np.array([reshape(x) for x in data])
    return processed_data, labels
def get_frame_mfccs(path):
    """Load a .wav audio file, split it into 28-second slices, and calculate MFCCs for all slices."""
    audio, sr = librosa.load(path)
    frames = librosa.util.frame(audio, frame_length=sr * 3, hop_length=sr * 3)
    frame_mfccs = []
    for i in range(frames.shape[1]):
        mfccs = mfcc(y=frames[:, i], sr=sr, n_mfcc=13, hop_length=512, n_fft=2048)
        frame_mfccs.append(mfccs)
    return frame_mfccs

# Reshape data
def reshape(data, shape=(26, 65)):
    print(data.shape)
    assert data.shape == (13, 130), f"The Data shape should be (13, 1206) but got {data.shape}"
    data = data.reshape(shape)
    data = np.expand_dims(data, axis=-1)
    return data

load_path = 'Data\\genres_original'
processed_data, labels = get_mfcc(load_path)
np.save('processed_data_mfcc.npy', processed_data)
np.save('labels_mfcc.npy', labels)