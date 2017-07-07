from tkinter import *

root = Tk()
def print_name(event):
    print("Hi Himanshu")
btn_print_name_in_shell = Button(root, text = "Print name in shell")
btn_print_name_in_shell.bind("<Button-1>", print_name)
btn_print_name_in_shell.pack()
root.mainloop()
