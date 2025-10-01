import ctypes
import sys
import tkinter as tk
from tkinter import messagebox

class ElevationRequired(Exception):
    pass

def check_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0

def request_admin_optional(error_label=None):
    if check_admin():
        return

    # Attempt to relaunch with admin privileges
    cmdline = " ".join([f'"{arg}"' for arg in sys.argv])
    rc = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, cmdline, None, 1
    )

    if rc > 32:
        # Relaunch successful, current process should exit.
        sys.exit(0)
    
    # Relaunch failed or was declined
    msg = "You are running without admin privileges.\n System PATH changes neeed admin privileges."
    
    if error_label is not None:
        error_label.config(text=msg, fg="orange")
    else:
        try:
            messagebox.showwarning("Admin privileges not detected", msg)
        except tk.TclError:
            print(f"WARNING: {msg}")

def elevate_if_needed(root=None):
    # If already admin, continue.
    if check_admin():
        return
    
    # Launch a new copy with a marker so we can detect the second run.
    cmdline = " ".join(sys.argv + ["--elevated"])
    rc = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, cmdline, None, 1
    )
    
    # Elevation failed or was refused.
    if rc <= 32:
        raise ElevationRequired("Admin privileges are required to modify system variables.")

    # Close the current process.
    if root is not None:
        try:
            root.destroy()
        except Exception:
            pass
    sys.exit(0)