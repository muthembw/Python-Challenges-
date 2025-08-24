import time
from tkinter import Tk, Label

root = Tk()
root.title("Digital Clock")
root.configure(bg="black")  # make whole background black

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %Y-%m-%d")  # 🔑 Added weekday

    clock_label.config(text=current_time)
    currentdate_label.config(text=current_date)

    clock_label.after(1000, update_clock)

clock_label = Label(root, font=("calibri", 40, "bold"), background="black", foreground="pink")
clock_label.pack(expand=True, fill="both", anchor="center")

currentdate_label = Label(root, font=("calibri", 20, "bold"), background="black", foreground="white")
currentdate_label.pack(expand=True, fill="both", anchor="s")

update_clock()
root.mainloop()
