import tkinter as tk

tasks = ["Task 1", "Task 2", "Task 3"]

def on_drag_start(event):
    widget = event.widget
    widget._drag_data = widget.get(widget.nearest(event.y)), widget.nearest(event.y)

def on_drag_motion(event):
    widget = event.widget
    i = widget.nearest(event.y)
    if i != widget._drag_data[1]:
        widget.delete(widget._drag_data[1])
        widget.insert(i, widget._drag_data[0])
        widget._drag_data = widget._drag_data[0], i

root = tk.Tk()
root.title("Drag-and-Drop Task List")

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

for task in tasks:
    listbox.insert(tk.END, task)

listbox.bind("<Button-1>", on_drag_start)
listbox.bind("<B1-Motion>", on_drag_motion)

root.mainloop()
