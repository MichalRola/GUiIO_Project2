import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import librosa

from get_mfcc_for_one_file import get_mfcc_for_one_file, get_mfcc_stft_for_one_file, get_mfcc_only_for_one_file
from get_mfcc_for_one_file_28 import get_mfcc_for_one_file_28, get_mfcc_stft_for_one_file_28
#modele znajdują się pod linkiem: https://aghedupl-my.sharepoint.com/:f:/g/personal/pmamos_student_agh_edu_pl/EqU9cP9q_jRBuiR489nSu7MBm48MUUj7pxSA0Wy94y6plw?e=iT8kO8


def get_spectogram_for_one_file(path, sample_length=28):

    SAMPLING_RATE = 44100  # 44.1 kHz is a "standard" sampling rate.

    length_of_sample = sample_length  # Sample length in seconds.
    chunk_size = int(length_of_sample * SAMPLING_RATE)  # C

    counter = 0
    audio_timeseries, sampling_rate = librosa.load(path, sr=SAMPLING_RATE, mono=True)
    sound_end = len(audio_timeseries)
    no_of_chunks = sound_end // chunk_size

    spec = []
    if no_of_chunks != 0:
        for j in range(no_of_chunks):
            chunk_start = j * chunk_size
            chunk_end = (j + 1) * chunk_size
            if chunk_end > sound_end:
                break
            audio_chunk = audio_timeseries[chunk_start: chunk_end]
            spectrogram = librosa.feature.melspectrogram(y=audio_chunk, sr=sampling_rate)
            spectrogram = librosa.power_to_db(spectrogram)
            plt.imsave("aha.png", spectrogram, cmap='gray')

            image = plt.imread("aha.png")[:, :, 1]
            
            image = np.repeat(image[:, :, np.newaxis], 3, axis=2)
            image = np.expand_dims(image, axis=0)
            image = np.transpose(image, (0, 2, 1, 3))

            # plt.imshow(image[0])
            # plt.show()

            spec.append(image)

    return np.array(spec)

def get_prediction_mfcc(model_selector, path):
    pred = []
    if model_selector == 1:

        model = tf.keras.models.load_model('..\Model\my_model_28.h5')
        mfcc = get_mfcc_for_one_file_28(path)
        pred = model.predict(mfcc)
        average_pred = np.mean(pred, axis=0)
    elif model_selector == 2:
        model = tf.keras.models.load_model('..\Model\MobileNet.h5')
        mfcc = get_spectogram_for_one_file(path, 28)

        for el in mfcc:
            pred.append(model.predict(el))
        # pred = model.predict(mfcc)
        average_pred = np.mean(pred, axis=0)[0]
    elif model_selector == 3:
        model = tf.keras.models.load_model('..\Model\my_model_stft_28.h5')
        mfcc = get_mfcc_stft_for_one_file_28(path)
        pred = model.predict(mfcc)
        average_pred = np.mean(pred, axis=0)
    else:
        raise ValueError("Invalid model type")

    labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

    

    # Calculate the average prediction
    
    print(average_pred)

    # Print probabilities for each genre
    for label, probability in zip(labels, average_pred):
         print(f"{label}: {probability:.4f}")

    # Get the label with the highest average prediction
    predicted_label = labels[np.argmax(average_pred)]
    print("\nPredicted label:", predicted_label)
    return average_pred
    


# get_prediction_mfcc(5, "code/Data/genres_original/blues/blues.00064.wav")