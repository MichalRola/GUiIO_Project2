import librosa
import numpy as np
from librosa.feature import mfcc

def get_mfcc_for_one_file(path):
    audio, sr = librosa.load(path)
    n_fft = 2048
    hop_length = 512
    frame_length = int(sr * 3)
    hop_length_frames = int(frame_length / 2)  # 50% overlap

    frames = librosa.util.frame(audio, frame_length=frame_length, hop_length=hop_length_frames)
    mfcc_features = []
    for i in range(frames.shape[1]):
        mfccs = librosa.feature.mfcc(
            S=librosa.power_to_db(
                librosa.feature.melspectrogram(y=frames[:, i], sr=sr, n_fft=n_fft, hop_length=hop_length)
            ),
            sr=sr, n_mfcc=13
        )
        mfccs = mfccs.reshape(26, 65)
        mfccs = np.expand_dims(mfccs, axis=-1)
        mfcc_features.append(mfccs)

    mfcc_features = np.array(mfcc_features)  # Convert list to NumPy array
    mfcc_features = mfcc_features.reshape((mfcc_features.shape[0], 26, 65, 1))
    return mfcc_features

def get_mfcc_stft_for_one_file(path):
    audio, sr = librosa.load(path)
    n_fft = 2048
    hop_length = 512
    frame_length = int(sr * 3)
    hop_length_frames = int(frame_length / 2)  # 50% overlap

    frames = librosa.util.frame(audio, frame_length=frame_length, hop_length=hop_length_frames)
    stfts_features = []
    for i in range(frames.shape[1]):
        stfts = mfcc(
            S=librosa.amplitude_to_db(np.abs(librosa.stft(y=frames[:, i], n_fft=n_fft, hop_length=hop_length))),
            n_mfcc=13)
        stfts = stfts.reshape(26, 65)
        stfts = np.expand_dims(stfts, axis=-1)
        stfts_features.append(stfts)

    stfts_features = np.array(stfts_features)  # Convert list to NumPy array
    stfts_features = stfts_features.reshape((stfts_features.shape[0], 26, 65, 1))
    return stfts_features
def get_mfcc_only_for_one_file(path):
    audio, sr = librosa.load(path)
    n_fft = 2048
    hop_length = 512
    frame_length = int(sr * 3)
    hop_length_frames = int(frame_length / 2)  # 50% overlap

    frames = librosa.util.frame(audio, frame_length=frame_length, hop_length=hop_length_frames)
    mfcc_features = []
    for i in range(frames.shape[1]):
        mfccs = mfcc(y=frames[:, i],sr=sr, n_mfcc=13, hop_length= hop_length, n_fft=n_fft)
        mfccs = mfccs.reshape(26, 65)
        mfccs = np.expand_dims(mfccs, axis=-1)
        mfcc_features.append(mfccs)

    mfcc_features = np.array(mfcc_features)  # Convert list to NumPy array
    mfcc_features = mfcc_features.reshape((mfcc_features.shape[0], 26, 65, 1))
    return mfcc_features