import tkinter
def click_button(lbl, enr1, enr2, enr3):
    try:
        a = float(enr1.get())
        b = float(enr2.get())
        c = float(enr3.get())
        d = (b**2-4*a*c)
        if d>0:
            x1 = (-b + d**0.5)/(2*a)
            x2 = (-b - d**0.5)/(2*a)
            x = f"{x1} ; {x2}"
        elif d<0:
            x= "Корней нет"
        else:
            x = -b/2*a
    except ValueError:
            x = "You are wrong, sweetie!"
        
    lbl.configure(text=x)


if __name__ == '__main__':

    app = tkinter.Tk()
    app.title("Change my mind!")
    label = tkinter.Label(master=app, text="", font=("Calibri", 50), bg="#ffa38b", fg="#ffffff")
    entry1 = tkinter.Entry(master=app, justify = tkinter.CENTER, bd =2)
    entry2 = tkinter.Entry(master=app, justify = tkinter.CENTER, bd =2)
    entry3 = tkinter.Entry(master=app, justify = tkinter.CENTER, bd =2)
    button = tkinter.Button(master=app, text="Give me an answer", relief=tkinter.FLAT, bg="#3a4664", fg="#ffffff")
    button.configure(command=lambda: click_button(label, entry1, entry2, entry3))
    label.grid(column=0, row=0, sticky="WESN")
    entry1.grid(column=0,row=1,sticky="WESN")
    entry2.grid(column=0,row=2,sticky="WESN")
    entry3.grid(column=0,row=4,sticky="WESN")
    button.grid(column=0, row=5, sticky="WESN")

    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()


