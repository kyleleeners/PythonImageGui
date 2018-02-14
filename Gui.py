from tkinter import *
from tkinter import filedialog, messagebox
import numpy as np
import os
import pickle
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
choices = ["Red", "Green", "Yellow", "Blue", "Orange", "Purple", "Pink", "White"]


def load_dataset(filename):
    with open(os.path.join('Data', filename), 'rb') as f:
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


class Window(Frame):
    def __initialize_elements(self):
        Button(self.master, text="upload", fg="red", command=self.__upload_image).pack()
        self.main_label.bind("<B1-Motion>", self.__on_click)

        var = StringVar(self.master)
        OptionMenu(self.master, var, *choices).pack(side=BOTTOM)
        Button(self.master, text="Wrong Colour? Click to train!", fg="green", command=self.__select_option(var))\
            .pack(side=BOTTOM)

    def __upload_image(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        try:
            img = PhotoImage(file=filename)
            self.main_label.image = img
            self.main_label.config(image=img)
            self.main_label.pack(side=BOTTOM)
        except Exception:
            messagebox.showerror("Error", "Not a valid image file, try with .png")

    def __select_option(self, var):
        if self.cur_rgb == (-1, -1, -1):
            return
        try:
            model.update_rgb_data(var.get(), self.cur_rgb)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def __on_click(self, event):
        if event.x < 0 or event.y < 0 or event.x > self.master.winfo_width() or event.y > self.master.winfo_height():
            return
        image = self.main_label.image
        r, g, b = image.get(event.x, event.y)
        self.cur_rgb = (r, g, b)
        prediction = self.model.predict(np.array([[r, g, b]]))
        self.prediction.config(text=prediction[0], font=("arial", 14, "bold"), fg="white", bg="black")
        self.prediction.pack(side=TOP)

    def __init__(self, ml_model, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.configure(bg="black")
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        self.model = ml_model
        self.cur_rgb = (-1, -1, -1)
        self.main_label = Label(self.master, bg="black")
        self.prediction = Label(self.master)
        self.__initialize_elements()


class Model:
    def predict(self, item_to_classify):
        return self.model.predict(item_to_classify)

    def update_rgb_data(self, colour_name, rgb_value):
        if colour_name == "":
            raise Exception("No colour selected")
        new_entry = [[rgb_value[0], rgb_value[1], rgb_value[2], colour_name]]
        self.data = np.vstack((self.data, new_entry))
        remove_datasets(self.data)
        self.__fit()

    def __plot_rgb_data(self):
        figure = plt.figure()
        plt.style.use('dark_background')
        ax = Axes3D(figure)
        r, g, b, colours = self.data[:,0].astype(np.float), self.data[:,1].astype(np.float), self.data[:,2].astype(np.float), self.data[:,3]
        ax.scatter(r, g, b, facecolor=colours)
        plt.show()

    def __fit(self):
        X, y = self.data[:,:3], self.data[:,3:4].ravel()
        self.model = KNeighborsClassifier(9)
        self.model.fit(X, y)

    def __load_datasets(self):
        concatenated_data = None
        for dataSet in os.listdir("Data/"):
            data = load_dataset(dataSet)
            if concatenated_data is None:
                concatenated_data = data
            else:
                concatenated_data = np.vstack((concatenated_data, data))
        remove_datasets(concatenated_data)
        self.data = concatenated_data
        self.__fit()

    def __init__(self):
        self.model = None
        self.__load_datasets()
        # self.__plot_rgb_data() #uncomment this to see 3d plot of colour!


if __name__ == "__main__":
    root = Tk()
    model = Model()
    app = Window(model, root)
    root.mainloop()