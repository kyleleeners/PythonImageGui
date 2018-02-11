import os
import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def load_datasets():
    concatenated_data = None
    for dataSet in os.listdir("Data/"):
        data = load_dataset(dataSet)
        if concatenated_data is None:
            concatenated_data = data
        else:
            concatenated_data = np.vstack((concatenated_data, data))
    remove_datasets(concatenated_data)
    return concatenated_data


def load_dataset(filename):
    with open(os.path.join('Data',filename), 'rb') as f:
        return pickle.load(f)


def create_superset(superset):
    with open('Data/all_data.pickle', 'wb') as handle:
        pickle.dump(superset, handle, protocol=pickle.HIGHEST_PROTOCOL)


def remove_datasets(superset):
    for dataset in os.listdir("Data/"):
        file_path = os.path.join("Data/", dataset)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    create_superset(superset)


class Model:

    def fit(self):
        data = load_datasets()
        X,y = data[:,:3], data[:,3:4].ravel()
        self.model = KNeighborsClassifier(5)
        self.model.fit(X,y)

    def predict(self, item_to_classify):
        return self.model.predict(item_to_classify)

    def update(self, colour_name, rgb_value):
        if colour_name == "":
            raise Exception("No colour selected")
        new_entry = [[rgb_value[0], rgb_value[1], rgb_value[2], colour_name]]
        self.data = np.vstack((self.data, new_entry))
        remove_datasets(self.data)
        self.fit()

    def plot_data(self):
        fig = plt.figure()
        plt.style.use('dark_background')
        ax = Axes3D(fig)
        x, y, z, colours = self.data[:,0].astype(np.float), self.data[:,1].astype(np.float), self.data[:,2].astype(np.float), self.data[:,3]
        ax.scatter(x,y,z, facecolor=colours)
        plt.show()

    def __init__(self):
        self.model = None
        self.data = load_datasets()
        # self.plot_data()


model = Model()
model.fit()
z = model.predict(np.array([[50,100,100]]))
