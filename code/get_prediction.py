import tensorflow as tf
import sys
from PIL import Image
from numpy import asarray
import imageio
import matplotlib.pyplot as plt
import numpy as np


model = tf.saved_model.load('./models/saved_model/MobileNet')
image = plt.imread("code/Data/spectrograms/pop/00000(0).png")[:, :, 1]

image = np.repeat(image[:, :, np.newaxis], 3, axis=2)
image = np.expand_dims(image, axis=0)
image = np.transpose(image, (0, 2, 1, 3))

labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

pred = model(image) 
print(pred)

print(labels[np.argmax(pred)])