import numpy as np
import os
import sklearn.utils
import sklearn.preprocessing
from sklearn.metrics import classification_report, confusion_matrix
import keras
from keras import layers
import matplotlib.pyplot as plt


# Ścieżka zawierająca obrazy zbiory danych
load_path_training = r"D:\Folders\_Engineering_ThesisV2\training_data\ready_dataset\Slaney"
load_path_testing = r"D:\Folders\_Engineering_ThesisV2\testing_data\ready_dataset\Slaney"

features_training = np.load(os.path.join(load_path_training, "features.npy"))
labels_training = np.load(os.path.join(load_path_training, "labels.npy"))

features_testing = np.load(os.path.join(load_path_testing, "features.npy"))
labels_testing = np.load(os.path.join(load_path_testing, "labels.npy"))

features_training = np.swapaxes(features_training, 1, -1)
features_training = np.swapaxes(features_training, 1, 2)

features_testing = np.swapaxes(features_testing, 1, -1)
features_testing = np.swapaxes(features_testing, 1, 2)


# plt.imshow(np.array(features_training[0]).reshape(128, 345, 1))
# plt.show()
# print(features_training.shape[1:])
print(features_testing.shape)
print(features_training.shape)

coding = sklearn.preprocessing.LabelEncoder()
coding.fit(labels_training)

labels_training_coded = coding.transform(labels_training)
labels_testing_coded = coding.transform(labels_testing)

X_train, y_train = sklearn.utils.shuffle(features_training, labels_training_coded, random_state=125)
X_test, y_test = sklearn.utils.shuffle(features_testing, labels_testing_coded)

# Definiowanie modelu
num_classes = 8
input_shape = features_training.shape[1:]
batch_size = 32
epochs = 15    # epoki uczenia modelu, jedna epoka to przedstawienie wszystkich przykładów modelowi

model = keras.Sequential(
        [
keras.Input(shape=input_shape),
            keras.Input(shape=input_shape),
            layers.Conv2D(128, kernel_size=3, activation="relu"),
            #layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Flatten(),
            layers.Dense(64, activation="relu"),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )

model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# Koniec definicji modelu

model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)

y_prob = model.predict(X_test)
y_pred = np.argmax(y_prob, axis=1)

y_test_decoded = coding.inverse_transform(y_test)
y_pred_decoded = coding.inverse_transform(y_pred)

print(classification_report(y_test_decoded, y_pred_decoded))
print(confusion_matrix(y_test_decoded, y_pred_decoded))
