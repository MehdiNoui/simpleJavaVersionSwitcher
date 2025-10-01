import sys, os
import tkinter as tk
from tkinter import ttk
from modules.fetcher import list_java_versions
from modules.clicker import clicker_logic
from modules.label_refresh import refresh_current_java

# Initialize main window
root = tk.Tk()
root.title("Simple Java switcher")
root.geometry("600x400")
root.resizable(False, False)

# Set application icon
if hasattr(sys, '_MEIPASS'):
    icon_path = os.path.join(sys._MEIPASS, 'assets', 'switch.ico')
else:
    icon_path = os.path.join('assets', 'switch.ico')
root.iconbitmap(icon_path)

# Select Label
label = tk.Label(root, text="Welcome. Select the Java version and environment type to switch.")
label.pack(pady=10)

# Version Label
current_java_label = tk.Label(root, text="", fg="blue")
current_java_label.pack(pady=5)
refresh_current_java(current_java_label)

# Error catcher Label
error_label = tk.Label(root, text="")
error_label.pack(pady=5)
try: 
    versions = list_java_versions()
except FileNotFoundError as e:
    error_label.config(text=str(e), fg="red")
    versions = []

# environment Type Combo Box
env_type_picked = tk.StringVar()
env_type_CB = ttk.Combobox(root,textvariable=env_type_picked)
env_type_CB['values'] = ["User Variables", "System Variables", "All"]
env_type_CB['state'] = 'readonly'
env_type_CB.current(0)
env_type_CB.pack(pady=10)

# Versions Combo Box
vrs_picked = tk.StringVar()
vrs_CB = ttk.Combobox(root,textvariable=vrs_picked)
vrs_CB.config(width=40)
vrs_CB['values'] = versions
vrs_CB['state'] = 'readonly'
vrs_CB.pack(pady=10)

# Select Button
def on_select():
    try:
        clicker_logic(root, vrs_picked.get(), env_type_picked.get())
        error_label.config(text="Success! Java version switched.", fg="green")
        refresh_current_java(current_java_label)
    except Exception as e:
        error_label.config(text=str(e), fg="red")

bt = tk.Button(root,text="Select", command=on_select)
bt.pack(pady=10)

current_value = vrs_CB.get()
root.mainloop()