from tkinter import *
from tkinter import filedialog, messagebox
import PIL.Image
import PIL.ImageTk


class Window(Frame):

    def __init__(self, root = None):
        Frame.__init__(self, root)
        self.root = root
        self.init_window()
        self.main_label = Label(self.root)
        Button(self.root, text="upload", fg="red", command=self.upload_image).pack(side=BOTTOM)

    def init_window(self):
        self.root.title("GUI")
        self.pack(fill=BOTH, expand=1)

    def upload_image(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        try:
            load = PIL.Image.open(filename)
            render = PIL.ImageTk.PhotoImage(load)
            self.main_label.image = render
            self.main_label.config(image=render)
            self.main_label.pack()
        except Exception:
            messagebox.showerror("Error", "Not a valid image file, try with .png")

    def on_click(self, event):
        print("Clicked at: ", event.x, event.y)


if __name__ == "__main__":
    master = Tk()
    app = Window(master)
    master.mainloop()
