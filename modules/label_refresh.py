from modules.java_info import get_user_java_path, get_system_java_path

def refresh_current_java(current_java_label):
    try:
        user_path = get_user_java_path()
    except Exception as e:
        user_path = f"User: {e}"

    try:
        system_path = get_system_java_path()
    except Exception as e:
        system_path = f"System: {e}"

    current_java_label.config(
        text=f"User PATH:\n{user_path}\n\nSystem PATH:\n{system_path}"
    )