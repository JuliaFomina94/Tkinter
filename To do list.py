import tkinter

class Application(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.tasklist = []
        self.title("To do list")
        self.main_frame = tkinter.Frame(master=self, bg="white", bd=2)
        self.label = tkinter.Label(master=self.main_frame, text="Input", bg="white", font=("Calibri", 10))
        self.entry = tkinter.Entry(master=self.main_frame, width=5, justify=tkinter.CENTER)
        self.button = tkinter.Button(master=self.main_frame, text="Add", bg="pink", relief=tkinter.FLAT,
                                     command=self.get_results)
        self.listbox = tkinter.Listbox(self.main_frame, bg="white", fg="black", width=20, height=5, relief=tkinter.FLAT,
                                    font=("Calibri", 10))
        self.entry.bind("<Return>", self.get_results)
        self.delete_button = tkinter.Button(master=self.main_frame, text="Delete", bg="pink", relief=tkinter.FLAT,
                                     command=self.delete)

    def draw_interface(self):
        self.main_frame.grid(column=0, row=0, sticky="WESN")
        self.entry.grid(column=1, row=0, columnspan=6, sticky="WESN")
        self.label.grid(column=0, row=0, sticky="WESN")
        self.button.grid(column=0, row=1, columnspan=6, sticky="WESN")
        self.listbox.grid(column=0, row=2, columnspan=6, sticky="WESN")
        self.delete_button.grid(column=0, row=5, columnspan=6, sticky="WESN")


    def get_results(self, event=None):
        message = self.entry.get()
        self.entry.delete("0", tkinter.END)
        if message not in self.tasklist:
            self.listbox.insert(tkinter.END, f"{message}\n")
            self.tasklist.append(message)


    def delete(self):
        selection = self.listbox.curselection()
        self.listbox.delete(selection[0])


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

