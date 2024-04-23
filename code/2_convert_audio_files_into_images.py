"""
For now, it creates melspectrograms with a sample length of 10 seconds.
"""
import os
import matplotlib.pyplot as plt
import librosa
import gc
import numpy as np

SAMPLING_RATE = 44100   # 44.1 kHz is a "standard" sampling rate.


# Code is based on the following article.
# https://www.kaggle.com/code/rftexas/converting-sounds-into-images-a-general-guide
def create_melspectrogram(load, save, file_name, chunk_size):
    counter = 0
    audio_timeseries, sampling_rate = librosa.load(os.path.join(load, file_name), sr=SAMPLING_RATE, mono=True)
    parts = file_name.split(".")
    sound_end = len(audio_timeseries)
    no_of_chunks = sound_end//chunk_size
    if no_of_chunks == 0:
        return
    for j in range(no_of_chunks):
        chunk_start = j * chunk_size
        chunk_end = (j + 1) * chunk_size
        if chunk_end > sound_end:
            break
        audio_chunk = audio_timeseries[chunk_start: chunk_end]
        spectrogram = librosa.feature.melspectrogram(y=audio_chunk, sr=sampling_rate)
        spectrogram = librosa.power_to_db(spectrogram)
        new_file_name = parts[len(parts) - 2] + "(" + str(counter) + ").png"
        counter += 1

        plt.imsave(os.path.join(save, new_file_name), spectrogram, cmap='gray')
        del spectrogram
        gc.collect()
    del audio_timeseries
    gc.collect()
    return


if __name__ == "__main__":
    load_path = r"Data\genres_original\jazz"
    save_path = r"Data\spectograms\jazz"

    length_of_sample = 10                                   # Sample length in seconds.
    sample_width = int(length_of_sample * SAMPLING_RATE)    # Converting to sample length with sampling rate.

    # Creating folders, if necessary.
    for root, dirs, files in os.walk(load_path):
        for dirname in dirs:
            try:
                os.mkdir(os.path.join(save_path, dirname))
            except OSError:
                print(dirname + " folder already exists.")

    # Converting audio files to image files with melspectrograms.
    for root, dirs, files in os.walk(load_path):
        for filename in files:
            parts_of_dir = root.split("\\")
            dirname = parts_of_dir[len(parts_of_dir)-1]
            create_melspectrogram(root,save_path, filename, sample_width)
