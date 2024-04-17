import os
import matplotlib.pyplot as plt
import librosa
import gc
import numpy as np

SAMPLING_RATE = 44100


def audio_to_spectrogram(load, save, file_name, chunk_size, mel):
    counter = 0
    create_melspectrogram(load, save, file_name, counter, 0, 0, chunk_size, mel)
    gc.collect()
    return


def create_melspectrogram(load, save, file_name, counter, sound_start, sound_end, chunk_size, mel):
    audio_timeseries, sampling_rate = librosa.load(os.path.join(load, file_name), sr=SAMPLING_RATE, mono=True)
    parts = file_name.split(".")
    if sound_end == 0:
        sound_end = len(audio_timeseries)
    no_of_chunks = (sound_end-sound_start)//chunk_size
    if no_of_chunks == 0:
        return counter
    for j in range(no_of_chunks):
        chunk_start = sound_start + j * chunk_size
        chunk_end = sound_start + (j + 1) * chunk_size
        if chunk_end > sound_end:
            break
        audio_chunk = audio_timeseries[chunk_start: chunk_end]
        if mel is True:
            spectrogram = librosa.feature.melspectrogram(y=audio_chunk, sr=sampling_rate)
            spectrogram = librosa.power_to_db(spectrogram)
        else:
            spectrogram = librosa.stft(y=audio_chunk)
            spectrogram = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)
        new_file_name = parts[len(parts) - 2] + "(" + str(counter) + ").png"
        counter += 1

        plt.imsave(os.path.join(save, new_file_name), spectrogram, cmap='gray')
        del spectrogram
        gc.collect()
    del audio_timeseries
    gc.collect()
    return counter


if __name__ == "__main__":
    load_path = r"D:\Folders\_Engineering_ThesisV2\training_data\wave"
    save_path = r"D:\Folders\_Engineering_ThesisV2\training_data\spectrograms\Slaney"

    # audio_to_melspectrogram(load_path, save_path, "CommonBlackbird\\314165.wav", htk_on=0)

    # for filename in os.listdir(load_path):
    #     audio_to_melspectrogram(load_path, save_path, filename, htk_on=0)

    create_mel = True
    sample_width = int(4 * SAMPLING_RATE)

    for root, dirs, files in os.walk(load_path):
        for dirname in dirs:
            try:
                os.mkdir(os.path.join(save_path, dirname))
            except OSError:
                print(dirname + " folder already exists.")

    for root, dirs, files in os.walk(load_path):
        for filename in files:
            parts_of_dir = root.split("\\")
            dirname = parts_of_dir[len(parts_of_dir)-1]
            audio_to_spectrogram(root, os.path.join(save_path, dirname), filename, sample_width, create_mel)
