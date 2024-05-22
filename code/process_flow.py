import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import librosa
import gc

from get_mfcc_for_one_file import get_mfcc_for_one_file


def load_image(path):
    image = plt.imread(path)[:, :, 1]

    image = np.repeat(image[:, :, np.newaxis], 3, axis=2)
    image = np.expand_dims(image, axis=0)
    image = np.transpose(image, (0, 2, 1, 3))
    return tf.convert_to_tensor(image)


def generate_heatmap_from_audio(model_path: str,
                                chunk_size,
                                audio_path: str = "Data\genres_original",
                                save_spectogram_path: str = "Data\spectrograms\custom",
                                sample_length: int = 30,
                                is_model_mfcc: bool = False):

    mfcc = None
    SAMPLING_RATE = 44100  # 44.1 kHz is a "standard" sampling rate.
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

            plt.imsave(os.path.join(save_spectogram_path, new_file_name), spectrogram, cmap='gray')
            del spectrogram
            gc.collect()
        del audio_timeseries
        gc.collect()
    if is_model_mfcc:
        mfcc = get_mfcc_for_one_file(audio_path)
    model = tf.keras.models.load_model(model_path)

    whole_audio_predictions = []
    labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    spectrograms = os.listdir(save_spectogram_path)

    prediction = None
    predicted_class_index = 0

    if not is_model_mfcc:
        for idx, spectrogram in enumerate(spectrograms):
            img_array = load_image(os.path.join(save_spectogram_path, spectrogram))

            predictions = model.predict(img_array)
            whole_audio_predictions.append(labels[np.argmax(predictions)])

            unique, counts = np.unique(whole_audio_predictions, return_counts=True)
            prediction = unique[np.argmax(counts)]
            predicted_class_index = labels.index(prediction)

    else:
        prediction = model.predict(mfcc)
        predicted_class_index = labels.index(prediction)

    grad_model = tf.keras.models.Model([model.inputs], [model.get_layer('conv_pw_13_relu').output, model.output])

    # generating example gradient from one of spectrograms
    spectrogram = spectrograms[int(len(spectrograms))]
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

    plt.imshow(cv2.cvtColor(overlay_img, cv2.COLOR_BGR2RGB), aspect='auto')
    plt.axis('off')
    plt.show()

    return prediction
