import os

import numpy as np
import sys

from pydub import AudioSegment

from mp3_to_wav import mp3_to_wav, change_suffix
from get_prediction_mfcc import get_prediction_mfcc


#y_train = np.load('processed_data_mfcc_28.npy')
# y_train2 = np.load('processed_data_mfcc_stft.npy')
# print(y_train)
# print(y_train2.shape)
# print(y_train.shape)

# get_prediction_mfcc(2, "Data/genres_original/metal/metal.00006.wav")

import os
from pydub import AudioSegment
import pandas as pd


# Funkcja zmieniająca sufiks pliku z .mp3 na .wav
# Funkcja przetwarzająca wyniki predykcji na słownik
# Funkcja zmieniająca sufiks pliku z .mp3 na .wav
def change_suffix(filename):
    return os.path.splitext(filename)[0] + '.wav'

# Ścieżki
input_folder = 'GUiIO_utwory'
save_path = r'audio\wave'
results = []
genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
model_names = [
    "MFCC na spektogramie",
    "MFCC na STFT",
    "MFCC",
    "MFCC na spektogramie dla 28 sekund",
    "MFCC na STFT na 28 sekund"
]
# Przejście przez wszystkie pliki MP3 w podfolderach
for root, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.mp3'):
            # Pełna ścieżka do pliku wejściowego
            filename = os.path.join(root, file)

            # Konwersja MP3 na WAV
            sound = AudioSegment.from_mp3(filename)
            new_filename = change_suffix(file)

            # Pełna ścieżka do zapisu pliku wyjściowego
            output_folder = os.path.join(save_path, os.path.relpath(root, input_folder))
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            output_path = os.path.join(output_folder, new_filename)

            # Eksport pliku WAV
            sound.export(output_path, format="wav")

            for model_id, model_name in enumerate(model_names, 1):
                print(model_id, model_name)
                prediction = get_prediction_mfcc(model_id, output_path)
                max_genre = genres[np.argmax(prediction)]
                result = [filename, model_name] + prediction.tolist() + [max_genre]
                results.append(result)

# Przygotowanie nagłówków dla kolumn
genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
columns = ['Original File', 'Model'] + genres + ['Predicted Genre']

# Zapis wyników do pliku Excel
df = pd.DataFrame(results, columns=columns)
df.to_excel('predictions.xlsx', index=False)