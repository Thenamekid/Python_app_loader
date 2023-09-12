import tkinter as tk
from tkinter import *
import json
import subprocess
import os
from PIL import Image, ImageTk

def launch_app(app_info):
    app_directory_path = app_directory
    if 'directory' in app_info:
        app_directory_path = os.path.join(app_directory, app_info['directory'])
    
    app_path = os.path.join(app_directory_path, app_info['script'])
    try:
        subprocess.run(["python", app_path], check=True, cwd=app_directory_path)
    except subprocess.CalledProcessError:
        print(f"Error launching {app_info['name']} app.")

current_directory = os.path.dirname(os.path.abspath(__file__))
app_directory = os.path.join(current_directory, 'apps')

apps = []

for folder_name in os.listdir(app_directory):
    app_path = os.path.join(app_directory, folder_name)
    if os.path.isdir(app_path):
        json_path = os.path.join(app_path, f"{folder_name}.json")
        if os.path.exists(json_path):
            with open(json_path, 'r') as json_file:
                app_info = json.load(json_file)
                apps.append(app_info)

root = tk.Tk()
root.title("VOS")
root.configure(bg="#A0677B")
root.geometry("500x300")
root.iconbitmap('D:\Virus\Mega_app\OS\VOS_logo.ico')

icons = []

def load_icons():
    for app_info in apps:
        icon_path = os.path.join(app_directory, app_info['directory'], app_info['icon'])
        icon = Image.open(icon_path)
        icon = icon.resize((100, 100), Image.LANCZOS)
        icon = ImageTk.PhotoImage(icon)
        icons.append(icon)

load_icons()    

app_buttons = []

for i, app_info in enumerate(apps):
    button = Button(root, text=app_info['name'], image=icons[i], compound='top', bg="#A0677B", borderwidth=0, highlightthickness=0, activebackground="#A0677B")
    button.grid(row=i // 3, column=i % 3)
    app_buttons.append(button)

    button.config(command=lambda i=i: launch_app(apps[i]))

root.mainloop()
