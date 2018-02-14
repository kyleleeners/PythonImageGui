import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from Graph import Graph
from MlModel import MlModel
from DataUtil import DataUtil
choices = ["Red", "Green", "Yellow", "Blue", "Orange", "Purple", "Pink", "White"]


class Window(tk.Frame):
    def __initialize_elements(self):
        tk.Button(self, text="upload", fg="red", command=self.__upload_image).pack()
        self.master.bind("<B1-Motion>", self.__on_click_or_drag_display_rgb_info)

        choice = tk.StringVar(self.master)
        tk.OptionMenu(self.bottom_frame, choice, *choices).pack(side=tk.BOTTOM)
        tk.Button(self.bottom_frame, text="Wrong Colour? Click to train!", fg="green",
                  command=self.__update_data(choice)).pack(side=tk.BOTTOM)

    def __upload_image(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        try:
            img = tk.PhotoImage(file=filename)
            self.image_label.image = img
            self.image_label.config(image=img)
            self.image_label.pack(side=tk.BOTTOM)
        except Exception:
            messagebox.showerror("Error", "Not a valid image file, try with .png")

    def __on_click_or_drag_display_rgb_info(self, event):
        if event.x < 0 or event.y < 0 or event.x > self.image_label.winfo_width()\
                or event.y > self.image_label.winfo_height():
            return
        image = self.image_label.image
        r, g, b = image.get(event.x, event.y)
        self.cur_rgb = (r, g, b)
        prediction = model.predict(np.array([[r, g, b]]))
        self.prediction.config(text=prediction[0], font=("arial", 14, "bold"), fg="white", bg="black")
        self.prediction.pack(side=tk.TOP)

    def __update_data(self, var):
        if self.cur_rgb == (-1, -1, -1):
            return
        try:
            data_util.update_data(var.get(), self.cur_rgb)
            model.fit(data_util.data)
        except Exception as error:
            messagebox.showerror("Error", str(error))

    @staticmethod
    def __on_exit():
        data_util.save_data_as_file()
        root.destroy()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.protocol('WM_DELETE_WINDOW', self.__on_exit)
        self.configure(bg="black")
        self.pack(fill=tk.BOTH, expand=1)
        self.master = master
        self.master.title("ColourGui")
        self.master.configure(bg="black")
        self.cur_rgb = (-1, -1, -1)
        self.image_label = tk.Label(self.master, bg="black")
        self.prediction = tk.Label(self)
        self.bottom_frame = tk.Frame(self).pack(side=tk.BOTTOM)
        self.__initialize_elements()


if __name__ == "__main__":
    data_util = DataUtil()
    data_util.load_data_files()
    model = MlModel()
    model.fit(data_util.data)
    root = tk.Tk()
    app = Window(root)
    root.mainloop()

