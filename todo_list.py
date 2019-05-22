# To Do List GUI
# Python 3.7.3

import tkinter
import random

# Root window
root = tkinter.Tk()

# Functions


def add_task():
    pass


def delete_all():
    pass


def delete_one():
    pass


def sort_asc():
    pass


def sort_desc():
    pass


def choose_random():
    pass


def number_of_tasks():
    pass


# Window elements
lbl_title = tkinter.Label(root, text="To Do List", bg="white")
lbl_title.pack()

lbl_display = tkinter.Label(root, text="Something", bg="white")
lbl_display.pack()

txt_input = tkinter.Entry(root, width=15)
txt_input.pack()

btn_add_task = tkinter.Button(
    root, text="Add a Task", fg="green", bg="white", command=add_task)
btn_add_task.pack()

btn_delete_all = tkinter.Button(
    root, text="Delete all Tasks", fg="green", bg="white", command=delete_all)
btn_delete_all.pack()

btn_delete_one = tkinter.Button(
    root, text="Delete 1 Task", fg="green", bg="white", command=delete_one)
btn_delete_one.pack()

btn_sort_desc = tkinter.Button(
    root, text="Sort (DESC)", fg="green", bg="white", command=sort_desc)
btn_sort_desc.pack()

btn_sort_asc = tkinter.Button(
    root, text="Sort (ASC)", fg="green", bg="white", command=sort_asc)
btn_sort_asc.pack()

btn_choose_random = tkinter.Button(
    root, text="Choose a Random Task", fg="green", bg="white", command=choose_random)
btn_choose_random.pack()

btn_number_of_tasks = tkinter.Button(
    root, text="Number of Tasks", fg="green", bg="white", command=number_of_tasks)
btn_number_of_tasks.pack()

btn_exit = tkinter.Button(
    root, text="Exit", fg="red", bg="white", command=exit)
btn_exit.pack()

lb_tasks = tkinter.Listbox(root)
lb_tasks.pack()


# Main event loop
root.mainloop()
