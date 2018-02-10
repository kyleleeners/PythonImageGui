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
        return concatenated_data

    def fit(self):
        data = self.load_datasets()
        X,y = data[:,:3], data[:,3:4].ravel()
        self.model = KNeighborsClassifier(5)
        self.model.fit(X,y)

    def predict(self, item_to_classify):
        return self.model.predict(item_to_classify)

    def __init__(self):
        self.model = None


model = Model()
model.fit()
z = model.predict(np.array([[50,100,100]]))
