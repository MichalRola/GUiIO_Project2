import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from get_mfcc_for_one_file import get_mfcc_for_one_file, get_mfcc_stft_for_one_file, get_mfcc_only_for_one_file
from get_mfcc_for_one_file_28 import get_mfcc_for_one_file_28, get_mfcc_stft_for_one_file_28
#modele znajdują się pod linkiem: https://aghedupl-my.sharepoint.com/:f:/g/personal/pmamos_student_agh_edu_pl/EqU9cP9q_jRBuiR489nSu7MBm48MUUj7pxSA0Wy94y6plw?e=iT8kO8
def get_prediction_mfcc(model_selector, path):
    if model_selector == 1:
        model = tf.keras.models.load_model('my_model.h5')
        mfcc = get_mfcc_for_one_file(path)
    elif model_selector == 2:
        model = tf.keras.models.load_model('my_model_stft.h5')
        mfcc = get_mfcc_stft_for_one_file(path)
    elif model_selector == 3:
        model = tf.keras.models.load_model('my_model_only.h5')
        mfcc = get_mfcc_only_for_one_file(path)
    elif model_selector == 4:
        model = tf.keras.models.load_model('my_model_stf_28.h5')
        mfcc = get_mfcc_stft_for_one_file_28(path)
    elif model_selector == 5:
        model = tf.keras.models.load_model('my_model_28.h5')
        mfcc = get_mfcc_for_one_file_28(path)
    else:
        raise ValueError("Invalid model type")

    labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

    pred = model.predict(mfcc)

    # Calculate the average prediction
    average_pred = np.mean(pred, axis=0)

    # Print probabilities for each genre
    # for label, probability in zip(labels, average_pred):
    #      print(f"{label}: {probability:.4f}")

    # Get the label with the highest average prediction
    predicted_label = labels[np.argmax(average_pred)]
    return average_pred
    # print("\nPredicted label:", predicted_label)

