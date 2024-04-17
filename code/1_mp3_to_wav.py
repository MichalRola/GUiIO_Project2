import os
from pydub import AudioSegment


def change_suffix(file_name):
    parts = file_name.split(".")
    img_name = parts[len(parts) - 2] + ".wav"
    return img_name


if __name__ == "__main__":
    load_path = r"D:\Folders\_Engineering_ThesisV2\testing_data\dataset\audio"
    save_path = r"D:\Folders\_Engineering_ThesisV2\testing_data\wave"

    # for filename in os.listdir(load_path):
    #     sound = AudioSegment.from_mp3(os.path.join(load_path, filename))
    #     new_filename = change_suffix(filename)
    #     sound.export(os.path.join(save_path, new_filename), format="wav")

    for root, dirs, files in os.walk(load_path):
        for dirname in dirs:
            try:
                os.mkdir(os.path.join(save_path, dirname))
            except OSError:
                print(dirname + " folder already exists.")

    for root, dirs, files in os.walk(load_path):
        for filename in files:
            parts_of_dir = root.split("\\")
            dirname = parts_of_dir[len(parts_of_dir)-1]

            sound = AudioSegment.from_mp3(os.path.join(root, filename))
            new_filename = change_suffix(filename)
            sound.export(os.path.join(os.path.join(save_path, dirname), new_filename), format="wav")
