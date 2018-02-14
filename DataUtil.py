import pickle
import os
import numpy as np


class DataUtil:

    def load_data_files(self):
        concatenated_data = None
        for dataSet in os.listdir("Data/"):
            data = self.__load_data(dataSet)
            if concatenated_data is None:
                concatenated_data = data
            else:
                concatenated_data = np.vstack((concatenated_data, data))
        self.data = concatenated_data
        self.save_data_as_file()
        return concatenated_data

    def save_data_as_file(self):
        self.__remove_data_files()
        with open('Data/all_data.pickle', 'wb') as handle:
            pickle.dump(self.data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def update_data(self, colour_name, rgb_value):
        if colour_name == "":
            raise Exception("No colour selected")
        new_entry = [[rgb_value[0], rgb_value[1], rgb_value[2], colour_name]]
        self.data = np.vstack((self.data, new_entry))

    @staticmethod
    def __remove_data_files():
        for data_set in os.listdir("Data/"):
            file_path = os.path.join("Data/", data_set)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

    @staticmethod
    def __load_data(filename):
        with open(os.path.join('Data', filename), 'rb') as f:
            return pickle.load(f)

    def __init__(self):
        self.data = None
