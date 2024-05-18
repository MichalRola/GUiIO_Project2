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
    data_stft = []
    labels_stft = []
    for path in tqdm(audio_paths):
        genre = path.split('\\')[2]  # Extract genre from file path
        try:
            fmccs,stfts = get_frame_mfccs(path)
            for frame in fmccs:
                data.append(frame)
                labels.append(genre)
            for frame in stfts:
                data_stft.append(frame)
                labels_stft.append(genre)
        except Exception:
            pass
    processed_data = np.array([reshape(x) for x in data])
    processed_data_stft = np.array([reshape(x) for x in data_stft])
    return processed_data, labels , processed_data_stft, labels_stft
def get_frame_mfccs(path):
    """Load a .wav audio file, split it into 3-second slices, and calculate MFCCs for all slices."""
    audio, sr = librosa.load(path)

    n_fft = 2048
    hop_length = 512
    frame_length = int(sr * 3)
    hop_length_frames = int(frame_length / 2)  # 50% overlap

    frames = librosa.util.frame(audio, frame_length=frame_length, hop_length=hop_length_frames)

    mfcc_features = []
    stft_features = []
    for i in range(frames.shape[1]):
        mfccs = mfcc(
        S=librosa.power_to_db(librosa.feature.melspectrogram(y=frames[:, i], sr=sr, n_fft=n_fft, hop_length=hop_length)), n_mfcc=13)
        mfcc_features.append(mfccs)

        stfts = mfcc(
            S=librosa.amplitude_to_db(np.abs(librosa.stft(y=frames[:, i], n_fft=n_fft, hop_length=hop_length))),
            n_mfcc=13)
        stft_features.append(stfts)
        stft_features.append(stfts)
    return mfcc_features, stft_features




# Reshape data
def reshape(data, shape=(26, 65)):
    print(data.shape)
    # assert data.shape == (13, 130), f"The Data shape should be (13, 1206) but got {data.shape}"
    # data = data.reshape(shape)
    data = np.expand_dims(data, axis=-1)
    return data

load_path = 'Data\\genres_original'
processed_data, labels , processed_data_stft, labels_stft = get_mfcc(load_path)
np.save('processed_data_mfcc.npy', processed_data)
np.save('labels_mfcc.npy', labels)
np.save('processed_data_mfcc_stft.npy', processed_data_stft)
np.save('labels_mfcc_stft.npy', labels_stft)