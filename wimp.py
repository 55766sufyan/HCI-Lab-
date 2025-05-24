import tkinter as tk
from tkinter import simpledialog

tasks = []

def add_task():
    title = simpledialog.askstring("Task Title", "Enter task title:")
    deadline = simpledialog.askstring("Deadline", "Enter deadline:")
    if title and deadline:
        tasks.append((title, deadline))
        update_tasks()

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_tasks()

def update_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, f"{task[0]} - {task[1]}")

root = tk.Tk()
root.title("Task Manager")

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()

root.mainloop()
