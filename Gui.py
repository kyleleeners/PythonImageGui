from tkinter import *
from tkinter import filedialog, messagebox


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()
        self.main_frame = self.master
        self.main_label = Label(self.main_frame)

        Button(self.master, text="upload", fg="red", command=self.upload_image).pack(side=BOTTOM)

        self.rgb_value = Label(self.master)
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
        self.rgb_value.config(text="r: %.3f, g: %.3f, b: %.3f" % (r, g, b))
        self.rgb_value.pack()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()
