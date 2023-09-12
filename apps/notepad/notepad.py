import tkinter as tk
from tkinter import Text, Scrollbar, Menu, filedialog, messagebox
import os

def open_file():
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if file:
        text.delete(1.0, tk.END)
        text.insert(tk.END, file.read())
        file.close()

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if file:
        file.write(text.get(1.0, tk.END))
        file.close()
        messagebox.showinfo("Info", "File saved successfully!")

def about():
    messagebox.showinfo("About", "Simple Notepad App")

root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

text = Text(root)
text.pack(fill=tk.BOTH, expand=1)

scrollbar = Scrollbar(text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

root.mainloop()
