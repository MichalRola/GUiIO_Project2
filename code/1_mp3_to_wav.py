"""
Each species was saved in separate folder.
We can carry it over to music genres.
"""
import os
from pydub import AudioSegment


def change_suffix(file_name):
    parts = file_name.split(".")
    new_file_name = parts[len(parts) - 2] + ".wav"
    return new_file_name


if __name__ == "__main__":
    load_path = r"audio"
    save_path = r"audio\wave"

    # Creating folders, if necessary.
    # for root, dirs, files in os.walk(load_path):
    #     for dirname in dirs:
    #         try:
    #             os.mkdir(os.path.join(save_path, dirname))
    #         except OSError:
    #             print(dirname + " folder already exists.")

    # Converting from wav to mp3 format.
    for root, dirs, files in os.walk(load_path):
        for filename in files:
            parts_of_dir = root.split("\\")
            dirname = parts_of_dir[len(parts_of_dir)-1]

            sound = AudioSegment.from_mp3(os.path.join(root, filename))
            new_filename = change_suffix(filename)
            sound.export(os.path.join(save_path, new_filename), format="wav")
