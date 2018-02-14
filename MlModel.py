from sklearn.neighbors import KNeighborsClassifier


class MlModel:

    def fit(self, data):
        x, y = data[:, :3], data[:, 3:4].ravel()
        self.model.fit(x, y)

    def predict(self, item_to_classify):
        return self.model.predict(item_to_classify)

    def __init__(self):
        self.model = KNeighborsClassifier(9)
