import os
import matplotlib.pyplot as plt
import numpy as np


def append_to_database(root, species_name, dataset, labels, number_of_images):
    path = os.path.join(root, species_name)
    counter = 0

    for file_number in range(2):
        for file_name in os.listdir(path):
            if counter >= number_of_images:
                break
            elif "(" + str(file_number) + ")" in file_name:
                counter += 1
                # Wczytanie obrazu oraz ograniczenie jego wymiarów do 1
                image = plt.imread(os.path.join(path, file_name))[:, :, 1]

                # Dodawania wczytanych danych do odpowiednich list
                dataset.append([image])
                labels.append([species_name])
    return dataset, labels


def create_dataset(load, numeber_of_images):
    data = []
    lab = []
    species = ["CommonBlackbird", "CommonChiffchaff", "CommonCrane", "EurasianWren", "GreatSpottedWoodpecker", "GreatTit", "RedCrossbill", "SongThrush"]
    for root, dirs, files in os.walk(load):
        for folder in dirs:
            if folder in species:
                data, lab = append_to_database(root, folder, data, lab, numeber_of_images)

    return data, lab


if __name__ == "__main__":
    number_of_examples = 40
    load_path = r"D:\Folders\_Engineering_ThesisV2\testing_data\spectrograms\control"
    save_path = r"D:\Folders\_Engineering_ThesisV2\testing_data\ready_dataset\control"

    try:
        os.mkdir(save_path)
    except OSError:
        print(save_path + " folder already exists.")

    dataset, labels = create_dataset(load_path, number_of_examples)

    np.save(os.path.join(save_path, "features"), np.array(dataset))
    np.save(os.path.join(save_path, "labels"), np.array(labels))
    dataset = np.array(dataset)
    print(dataset.shape)
