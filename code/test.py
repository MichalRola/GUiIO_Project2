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

# get_prediction_mfcc(2, "Data/genres_original/Metal/Metal.00006.wav")

import os
from pydub import AudioSegment
import pandas as pd


# Funkcja zmieniająca sufiks pliku z .mp3 na .wav
# Funkcja przetwarzająca wyniki predykcji na słownik
# Funkcja zmieniająca sufiks pliku z .mp3 na .wav
def change_suffix(filename):
    return os.path.splitext(filename)[0] + '.wav'

# Ścieżki
input_folder = 'code\Data\genres_original'
save_path = r'code\Data\genres_original'
results = []
genres = ["Blues", "Classical", "Country", "Disco", "HipHop", "Jazz", "Metal", "Pop", "Reggae", "Rock"]
model_names = [
    "MFCC na spektogramie dla 28 sekund",
    "Ten lepszy model spec"
]
# Przejście przez wszystkie pliki MP3 w podfolderach
for root, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.mp3') or file.endswith('.wav'):
            # Pełna ścieżka do pliku wejściowego
            filename = os.path.join(root, file)

            if file.endswith('.mp3'):
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
            else:
                # Jeśli plik jest już WAV, użyjemy go bez konwersji
                output_path = filename

            # Wywołanie funkcji predykcyjnych i zapis wyników dla każdego modelu
            for model_id, model_name in enumerate(model_names,1):

                prediction = get_prediction_mfcc(model_id, output_path)
                max_genre = genres[np.argmax(prediction)]
                result = [filename, model_name] + prediction.tolist() + [max_genre]
                results.append(result)

# Przygotowanie nagłówków dla kolumn
genres = ["Blues", "Classical", "Country", "Disco", "HipHop", "Jazz", "Metal", "Pop", "Reggae", "Rock"]
columns = ['Original File', 'Model'] + genres + ['Predicted Genre']

# Zapis wyników do pliku Excel
df = pd.DataFrame(results, columns=columns)
df.to_excel('predictions_origin.xlsx', index=False)