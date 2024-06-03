import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import librosa
import gc
import glob

from get_mfcc_for_one_file_28 import get_mfcc_for_one_file_28, get_mfcc_stft_for_one_file_28


def load_image(path):
    image = plt.imread(path)[:, :, 1]
    image = np.repeat(image[:, :, np.newaxis], 3, axis=2)
    image = np.expand_dims(image, axis=0)
    image = np.transpose(image, (0, 2, 1, 3))
    return tf.convert_to_tensor(image)


def generate_heatmap_from_audio(model_path: str,
                                chunk_size: int = 30,
                                audio_path: str = "Data/genres_original",
                                save_spectogram_path: str = "Data/spectrograms/custom",
                                sample_length = 28):

    is_model_mfcc = False
    if model_path == "Model/my_model_28.h5":
        is_model_mfcc = True

    all_pred = list()
    mfcc = None
    SAMPLING_RATE = 44100  # 44.1 kHz is a "standard" sampling rate.

    length_of_sample = sample_length  # Sample length in seconds.
    chunk_size = int(length_of_sample * SAMPLING_RATE)  # C

    counter = 0
    audio_timeseries, sampling_rate = librosa.load(audio_path, sr=SAMPLING_RATE, mono=True)
    sound_end = len(audio_timeseries)
    no_of_chunks = sound_end // chunk_size

    if no_of_chunks != 0:
        for j in range(no_of_chunks):
            chunk_start = j * chunk_size
            chunk_end = (j + 1) * chunk_size
            if chunk_end > sound_end:
                break
            audio_chunk = audio_timeseries[chunk_start: chunk_end]
            spectrogram = librosa.feature.melspectrogram(y=audio_chunk, sr=sampling_rate)
            spectrogram = librosa.power_to_db(spectrogram)
            new_file_name = "spectrogram" + "(" + str(counter) + ").png"
            counter += 1

            plt.imsave(save_spectogram_path + r"/" + new_file_name, spectrogram, cmap='gray')
            del spectrogram
            gc.collect()
        del audio_timeseries
        gc.collect()
        
    if is_model_mfcc:
        mfcc = get_mfcc_for_one_file_28(audio_path)
    model = tf.keras.models.load_model(model_path)

    whole_audio_predictions = []
    labels = ['blues', 'klasyczna', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    spectrograms = os.listdir(save_spectogram_path)

    prediction = None
    predicted_class_index = 0

    print(is_model_mfcc)
    if not is_model_mfcc:
        for _, spectrogram in enumerate(spectrograms):
            img_array = load_image(os.path.join(save_spectogram_path, spectrogram))

            predictions = model.predict(img_array)
            whole_audio_predictions.append(labels[np.argmax(predictions)])

            unique, counts = np.unique(whole_audio_predictions, return_counts=True)
            prediction = unique[np.argmax(counts)]
            predicted_class_index = labels.index(prediction)

        grad_model = tf.keras.models.Model([model.inputs], [model.get_layer('conv_pw_13_relu').output, model.output])

        # generating example gradient from one of spectrograms
        spectrogram = spectrograms[int(len(spectrograms))-1]
        img_array = load_image(os.path.join(save_spectogram_path, spectrogram))
        with tf.GradientTape() as tape:
            conv_output, predictions = grad_model(img_array)
            loss = predictions[:, predicted_class_index]

        grads = tape.gradient(loss, conv_output)
        pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
        conv_output = conv_output[0]
        heatmap = tf.reduce_mean(tf.multiply(pooled_grads, conv_output), axis=-1)
        heatmap = np.maximum(heatmap, 0)
        heatmap /= np.max(heatmap)

        img = cv2.imread(os.path.join(save_spectogram_path, spectrogram))
        heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
        heatmap = np.uint8(255 * heatmap)
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
        overlay_img = cv2.addWeighted(img, 0.7, heatmap, 0.3, 0)

        ret = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2RGB)

    else:
        predictions = model.predict(mfcc)
        avg = np.mean(predictions, axis=0)
        average_pred = np.mean(avg, axis=0)
        predicted_label = labels[np.argmax(average_pred)]
        if predicted_label == "rock":
            mfcc_stft = get_mfcc_stft_for_one_file_28(audio_path)
            model_stft = tf.keras.models.load_model('..\Model\my_model_stft_28.h5')
            pred_stft = model_stft.predict(mfcc_stft)
            avg_stft = np.mean(pred_stft, axis=0)
            average_pred_stft = np.mean(avg_stft, axis=0)
            predicted_label_stft = labels[np.argmax(average_pred_stft)]
            if predicted_label_stft == "metal":
                mfcc = mfcc_stft
                model = model_stft
                predictions = pred_stft
                avg = avg_stft
                average_pred = average_pred_stft
                predicted_label = predicted_label_stft
        whole_audio_predictions.append(predicted_label)
        
        unique, counts = np.unique(whole_audio_predictions, return_counts=True)
        prediction = unique[np.argmax(counts)]
        predicted_class_index = labels.index(prediction)
        ret = None
    
    for label, probability in zip(labels, predictions[0]):
         if max(predictions[0]) == probability:
             pred = label
         print(f"{label}: {probability*100:.4f} %")
         all_pred.append(f"{probability*100:.4f} %")
    maxi = max(predictions[0])

    # Clear spectrograms directory
    files = glob.glob(save_spectogram_path + "/*")
    for f in files:
        os.remove(f)
    

    return pred, ret, all_pred, f"{maxi*100:.4f} %"
