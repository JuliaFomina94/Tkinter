import tkinter


class Application(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("Решение квадратных уравнений")
        self.main_frame = tkinter.Frame(master=self, bg="white", bd=2)
        self.a_entry = tkinter.Entry(master=self.main_frame, width=5, justify=tkinter.CENTER)
        self.a_label = tkinter.Text(master=self.main_frame, width=5, height=1, borderwidth=0, bg="white", font=("Calibri", 10))
        self.a_label.tag_configure("subscript", offset=4, font=("Calibri", 6))
        self.a_label.insert("insert", " ⋅ x", "", "2", "subscript")
        self.a_label.insert("insert", " + ")
        self.a_label.configure(state="disabled")
        self.b_entry = tkinter.Entry(master=self.main_frame, width=5, justify=tkinter.CENTER)
        self.b_label = tkinter.Label(master=self.main_frame, text=" ⋅ x + ", bg="white", font=("Calibri", 10))
        self.c_entry = tkinter.Entry(master=self.main_frame, width=5, justify=tkinter.CENTER)
        self.c_label = tkinter.Label(master=self.main_frame, text=" = 0", bg="white", font=("Calibri", 10))
        self.button = tkinter.Button(master=self.main_frame, text="Решить", relief=tkinter.FLAT, command=self.get_results)
        self.console = tkinter.Text(self.main_frame, bg="black", fg="green", width=20, height=5, relief=tkinter.FLAT, state="disabled", font=("Calibri", 10))

        self.a_entry.bind("<Return>", self.get_results)
        self.b_entry.bind("<Return>", self.get_results)
        self.c_entry.bind("<Return>", self.get_results)
        

    def draw_interface(self):
        self.main_frame.grid(column=0, row=0, sticky="WESN")
        self.a_entry.grid(column=0, row=0, sticky="WESN")
        self.a_label.grid(column=1, row=0, sticky="WESN")
        self.b_entry.grid(column=2, row=0, sticky="WESN")
        self.b_label.grid(column=3, row=0, sticky="WESN")
        self.c_entry.grid(column=4, row=0, sticky="WESN")
        self.c_label.grid(column=5, row=0, sticky="WESN")
        self.button.grid(column=0, row=1, columnspan=6, sticky="WESN")
        self.console.grid(column=0, row=2, columnspan=6, sticky="WESN")


    def check_entries(self):
        entries = [
            ("a", self.a_entry),
            ("b", self.b_entry),
            ("c", self.c_entry)
        ]
        messages = []

        for entry in entries:
            try:
                float(entry[1].get())
                entry[1].configure(bg="white")
            except ValueError:
                entry[1].configure(bg="red")
                messages.append(f"Неверный коэффициент: {entry[0]}")

        return messages


    def get_results(self, event=None):
        self.console.configure(state="normal")
        self.console.delete("0.0", tkinter.END)
        messages = self.check_entries()
        if messages:
            for message in messages:
                self.console.insert(tkinter.END, f"{message}\n")
        else:
            message = self.solve_quadratic_equation()
            self.console.insert(tkinter.END, f"{message}\n")
        self.console.configure(state="disabled")


    def solve_quadratic_equation(self):
        discriminant = float(self.b_entry.get()) ** 2 - 4 * float(self.a_entry.get()) * float(self.c_entry.get())
        if discriminant > 0:
            x1 = round((-float(self.b_entry.get()) + discriminant**0.5)/(2*float(self.a_entry.get())), 3)
            x2 = round((-float(self.b_entry.get()) - discriminant**0.5)/(2*float(self.a_entry.get())), 3)
            message = f"Дискриминант равен {round(discriminant)} - два корня: {x1}, {x2}"
        elif discriminant == 0:
            x = round(-float(self.b_entry.get())/(2*float(self.a_entry.get())), 3)
            message = f"Дискриминант равен 0, корень уравнения: {x}"
        else:
            message = f"Дискриминант меньше 0, корней - нет!"
        return message


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
