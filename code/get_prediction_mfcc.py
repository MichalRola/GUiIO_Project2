import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from get_mfcc_for_one_file import get_mfcc_for_one_file, get_mfcc_stft_for_one_file


def get_prediction_mfcc(model_selector, path):
    if model_selector == 1:
        model = tf.keras.models.load_model('my_model.h5')
        mfcc = get_mfcc_for_one_file(path)
    elif model_selector == 2:
        model = tf.keras.models.load_model('my_model_stft.h5')
        mfcc = get_mfcc_stft_for_one_file(path)
    else:
        raise ValueError("Invalid model type")

    labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

    pred = model.predict(mfcc)

    # Calculate the average prediction
    average_pred = np.mean(pred, axis=0)

    # Print probabilities for each genre
    for label, probability in zip(labels, average_pred):
        print(f"{label}: {probability:.4f}")

    # Get the label with the highest average prediction
    predicted_label = labels[np.argmax(average_pred)]
    print("\nPredicted label:", predicted_label)

