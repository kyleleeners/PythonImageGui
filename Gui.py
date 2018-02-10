from tkinter import *
from tkinter import filedialog, messagebox
from model import Model
import numpy as np

class Window(Frame):

    def __init__(self, ml_model, master=None):
        Frame.__init__(self, master)

        self.model = ml_model
        self.master = master
        self.init_window()
        self.main_frame = Frame(self.master).pack()
        self.bottom_frame = Frame(self.master).pack(side=BOTTOM)
        self.main_label = Label(self.main_frame)

        Button(self.main_frame, text="upload", fg="red", command=self.upload_image).pack()

        self.prediction = Label(self.bottom_frame)
        self.main_label.bind("<Button-1>", self.on_click)

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

        prediction = self.model.predict(np.array([[r, g, b]]))
        self.prediction.config(text=prediction[0])
        self.prediction.pack()


    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    model = Model()
    model.fit()
    app = Window(model, root)
    root.mainloop()
