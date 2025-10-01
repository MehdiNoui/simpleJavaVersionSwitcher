import subprocess

def get_user_java_path():
    try:
        result = subprocess.run(
            ['reg', 'query', r'HKEY_CURRENT_USER\Environment', '/v', 'Path'],
            capture_output=True, text=True, check=True
        )
        output = result.stdout
        path_value = output.split('    ')[-1].strip()
        return path_value
    except subprocess.CalledProcessError:
        return ValueError("path is not set in User Variables.")

def get_system_java_path():
    try:
        result = subprocess.run(['reg', 'query', r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment', '/v', 'Path'],
                                capture_output=True, text=True, check=True)
        output = result.stdout
        path_value = output.split('    ')[-1].strip()
        return path_value
    except subprocess.CalledProcessError:
        return ValueError("path is not set in System Variables.")