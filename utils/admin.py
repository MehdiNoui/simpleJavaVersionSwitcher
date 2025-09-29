import ctypes
import sys

class ElevationRequired(Exception):
    pass

def elevate_if_needed(root=None):
    # If already admin, continue.
    if ctypes.windll.shell32.IsUserAnAdmin():
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