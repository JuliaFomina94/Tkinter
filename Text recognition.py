import tkinter
from tkinter import filedialog as fd
from PIL import Image
import pytesseract

class Application(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("Text recognition")
        self.main_frame = tkinter.Frame(master=self, bg="white", width=100, bd=2)
        self.button = tkinter.Button(master=self.main_frame, text="Open file", bg="pink", relief=tkinter.FLAT,
                                     command=self.open_file)
        self.entry = tkinter.Entry(master=self.main_frame, width=100, justify=tkinter.CENTER)
        self.label = tkinter.Label(master=self.main_frame, bg="white", font=("Calibri", 10))
        self.button1 = tkinter.Button(master=self.main_frame, text="Recognize", bg="pink", relief=tkinter.FLAT,
                                     command=self.get_results)
        self.console = tkinter.Text(self.main_frame, bg="white", fg="black", width=100, height=40, relief=tkinter.FLAT,
                                    font=("Calibri", 10))
        self.label = tkinter.Label(master=self.main_frame, bg="white", font=("Calibri", 10))


    def draw_interface(self):
        self.main_frame.grid(column=0, row=0, sticky="WESN")
        self.button.grid(column=0, row=0, columnspan=6, sticky="WESN")
        self.label.grid(column=0, row=1, columnspan=6, sticky="WESN")
        self.button1.grid(column=0, row=2, columnspan=6, sticky="WESN")
        self.console.grid(column=0, row=3, columnspan=6, sticky="WESN")


    def open_file(self):
        self.file_name = fd.askopenfilename()
        self.label.configure(text=f"{self.file_name}")


    def get_results(self, event=None):
        self.console.delete("0.0", tkinter.END)
        im = Image.open(self.file_name)
        self.text = pytesseract.image_to_string(im, lang="eng")
        im.close()
        message = self.text
        self.console.insert(tkinter.END, f"{message}\n")


    def center(self):
        self.update_idletasks()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        size = tuple(int(i) for i in self.geometry().split('+')[0].split('x'))
        x = width / 2 - size[0] / 2
        y = height / 2 - size[1] / 2
        self.geometry("%dx%d+%d+%d" % (size + (x, y)))


if __name__ == '__main__':
    app = Application()
    app.draw_interface()
    app.center()
    app.resizable(False, False)
    app.mainloop()

