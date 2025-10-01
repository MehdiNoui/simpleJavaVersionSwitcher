import subprocess
from utils.admin import elevate_if_needed
from modules.java_info import get_user_java_path, get_system_java_path

def clicker_logic(root, selected_version: str, env_type: str):
    # Validate inputs
    if not env_type:
        raise ValueError("Please select an environment type")
    if not selected_version:
        raise ValueError("Please select a version")
    else:
        # Update the User PATH variable
        if env_type == "User Variables":
            if(selected_version == get_user_java_path()):
                raise ValueError("Selected version is already set in User PATH")
            subprocess.run(['setx', 'path', selected_version],
                check=True)
        # Update the System PATH variable
        elif env_type == "System Variables":
            if(selected_version == get_system_java_path()):
                raise ValueError("Selected version is already set in System PATH")
            elevate_if_needed(root)
            subprocess.run(['setx', "/M", 'path', selected_version],
                check=True)
        # Update both User and System PATH variables
        elif env_type == "All":
            if (selected_version == get_user_java_path() and selected_version == get_system_java_path()):
                raise ValueError("Selected version is already set in both User and System PATH")
            elevate_if_needed(root)
            subprocess.run(['setx', 'path', selected_version],
                check=True)
            subprocess.run(['setx', "/M", 'path', selected_version],
                check=True)
        # Unexpected case
        else:
            raise ValueError("Unexpected Error. Please try again.")