"""
This was created with folders in mind.
So, we would have to put genres in separate folders for it to work.
"""
import os
import matplotlib.pyplot as plt
import numpy as np


# Counting number of files in each folder.
# upper_limit lets you choose how many samples from one audio file.
def count_files(path, upper_limit=0):
    number_of_files = 0
    if upper_limit <= 0:
        for _ in os.listdir(path):
            number_of_files += 1
    else:
        for file_number in range(upper_limit):
            for file_name in os.listdir(path):
                if "(" + str(file_number) + ")" in file_name:
                    number_of_files += 1
    return number_of_files


# Appending images to dataset.
# upper_limit lets you choose how many samples from one audio file.
def append_to_database(root, species_name, dataset, labels, number_of_images, upper_limit=0):
    path = os.path.join(root, species_name)
    counter = 0

    if upper_limit <= 0:
        for file_name in os.listdir(path):
            if counter >= number_of_images:
                break
            counter += 1
            # Loading in the image with 1 dimension
            image = plt.imread(os.path.join(path, file_name))[:, :, 1]

            # Appending data to appropriate datasets
            dataset.append([image])
            labels.append([species_name])
    else:
        for file_number in range(upper_limit):
            if counter >= number_of_images:
                break
            for file_name in os.listdir(path):
                if counter >= number_of_images:
                    break
                if "(" + str(file_number) + ")" in file_name:
                    counter += 1
                    # Loading in the image with 1 dimension
                    image = plt.imread(os.path.join(path, file_name))[:, :, 1]

                    # Appending data to appropriate datasets
                    dataset.append([image])
                    labels.append([species_name])
    return dataset, labels


def create_dataset(load, number_of_images, upper_limit=0):
    data = []
    lab = []
    for root, dirs, files in os.walk(load):
        for folder in dirs:
            if count_files(os.path.join(root, folder), upper_limit) > number_of_images:
                data, lab = append_to_database(root, folder, data, lab, number_of_images, upper_limit)

    return data, lab


if __name__ == "__main__":
    upperlimit = 0
    number_of_examples = 150
    load_path = r"audio\spectograms"
    save_path = r"audio\ready_dataset"


    try:
        os.mkdir(save_path)
    except OSError:
        print(save_path + " folder already exists.")

    data_set, labs = create_dataset(load_path, number_of_examples, upperlimit)

    np.save(os.path.join(save_path, "features"), np.array(data_set))
    np.save(os.path.join(save_path, "labels"), np.array(labs))
    data_set = np.array(data_set)
    print(data_set.shape)
