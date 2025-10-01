import ctypes
import sys
import tkinter as tk
from tkinter import messagebox

class ElevationRequired(Exception):
    pass

def check_admin():
    """Return True if running as admin, False otherwise."""
    return ctypes.windll.shell32.IsUserAnAdmin() != 0

def request_admin_optional():
    if check_admin(): return
    cmdline = " ".join([f'"{arg}"' for arg in sys.argv])
    rc = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, cmdline, None, 1
    )
    if not check_admin():
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning(
            "Admin privileges not detected",
            "You are running without admin privileges.\n"
            "System PATH changes will be disabled."
        )
        root.destroy()

def elevate_if_needed(root=None):
    # If already admin, continue.
    if check_admin():return
    
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