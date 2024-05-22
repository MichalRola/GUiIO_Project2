import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

'''
DZALAMY NA SYGNALACH AUDIO O DLUGOSCI 28 SEKUND
WYMAGANY tensorflow==2.15 to załadowania modelu

Link do wytrenowanych modeli:
https://drive.google.com/drive/folders/1OqRRcUV6otdt9Ynfwu7OgZ11JHahvS4Y?usp=drive_link

Link do logów:
https://drive.google.com/drive/folders/1qEjVXV-c2gv3BTmcR580F8YPZ5mPbaUS?usp=drive_link
'''

model = tf.keras.models.load_model('../models/saved_model/MobileNet_3s_v3.h5')
image = plt.imread("code/Data/spectrograms/pop/00000(0).png")[:, :, 1]

image = np.repeat(image[:, :, np.newaxis], 3, axis=2)
image = np.expand_dims(image, axis=0)
image = np.transpose(image, (0, 2, 1, 3))

labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

pred = model(image)
print(pred)

print(labels[np.argmax(pred)])