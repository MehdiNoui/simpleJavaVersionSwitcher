import subprocess
from utils.admin import elevate_if_needed

def clicker_logic(root, selected_version: str, env_type: str):
    # Validate inputs
    if not env_type:
        raise ValueError("Please select an environment type")
    if not selected_version:
        raise ValueError("Please select a version")
    else:
        # Update the User PATH variable
        if env_type == "User Variables":
            subprocess.run(['setx', 'path', selected_version],
                check=True)
        # Update the System PATH variable
        elif env_type == "System Variables":
            elevate_if_needed(root)
            subprocess.run(['setx', "/M", 'path', selected_version],
                check=True)
        # Update both User and System PATH variables
        else:
            elevate_if_needed(root)
            subprocess.run(['setx', 'path', selected_version],
                check=True)
            subprocess.run(['setx', "/M", 'path', selected_version],
                check=True)