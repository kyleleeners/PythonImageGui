import os
import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def load_dataset(filename):
    with open(os.path.join('Data',filename), 'rb') as f:
        return pickle.load(f)


class Model:

    def load_datasets(self):
        concatenated_data = None
        for dataSet in os.listdir("Data/"):
            data = load_dataset(dataSet)
            if concatenated_data is None:
                concatenated_data = data
            else:
                concatenated_data = np.vstack((concatenated_data, data))
        self.remove_datasets(concatenated_data)
        return concatenated_data

    def remove_datasets(self, superset):
        for set in os.listdir("Data/"):
            file_path = os.path.join("Data/", set)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
        self.create_superset(superset)

    def create_superset(self, superset):
        with open('Data/all_data.pickle', 'wb') as handle:
            pickle.dump(superset, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def fit(self):
        X,y = self.data[:,:3], self.data[:,3:4].ravel()
        self.model = KNeighborsClassifier(5)
        self.model.fit(X,y)

    def predict(self, item_to_classify):
        return self.model.predict(item_to_classify)

    def update(self, colour_name, rgb_value):
        if colour_name == "":
            raise Exception("No colour selected")
        new_entry = [[rgb_value[0], rgb_value[1], rgb_value[2], colour_name]]
        self.data = np.vstack((self.data, new_entry))
        self.remove_datasets(self.data)
        self.fit()

    def __init__(self):
        self.model = None
        self.data = self.load_datasets()



model = Model()
model.fit()
z = model.predict(np.array([[50,100,100]]))
