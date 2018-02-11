from tkinter import *
from tkinter import filedialog, messagebox
from model import Model
import numpy as np


class Window(Frame):

    def __init__(self, ml_model, master=None):
        Frame.__init__(self, master)
        self.model = ml_model
        self.master = master
        self.initialize()


    def initialize(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        self.cur_rgb = (-1, -1, -1)
        self.main_frame = Frame(self.master).pack()
        self.bottom_frame = Frame(self.master).pack(side=BOTTOM)
        self.main_label = Label(self.main_frame)
        self.prediction = Label(self.bottom_frame)

        Button(self.main_frame, text="upload", fg="red", command=self.upload_image).pack()
        self.main_label.bind("<Button-1>", self.on_click)

        def select_option():
            if self.cur_rgb == (-1, -1, -1):
                return
            try:
                model.update(var.get(), self.cur_rgb)
            except Exception as error:
                messagebox.showerror("Error", str(error))


        var = StringVar(self.bottom_frame)
        choices = ["Red", "Green", "Yellow", "Blue", "Orange", "Purple", "Pink", "White"]
        OptionMenu(self.bottom_frame, var, *choices).pack(side=BOTTOM)
        Button(root, text="Wrong Colour? Click to train!", fg="green", command=select_option).pack(side=BOTTOM)



    def upload_image(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        try:
            img = PhotoImage(file=filename)
            self.main_label.image = img
            self.main_label.config(image=img)
            self.main_label.pack()
        except Exception:
            messagebox.showerror("Error", "Not a valid image file, try with .png")

    def on_click(self, event):
        image = self.main_label.image
        r, g, b = image.get(event.x, event.y)
        self.cur_rgb = (r, g, b)
        prediction = self.model.predict(np.array([[r, g, b]]))
        self.prediction.config(text=prediction[0])
        self.prediction.pack()



if __name__ == "__main__":
    root = Tk()
    model = Model()
    model.fit()
    app = Window(model, root)
    root.mainloop()
