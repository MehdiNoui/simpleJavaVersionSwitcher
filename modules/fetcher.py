import os
# Predefined directories to search for Java installations
java_bases = [
    r"C:\Program Files\Eclipse Adoptium",
    r"C:\Program Files\Java",
    r"C:\Program Files\AdoptOpenJDK",
    r"C:\Program Files\Zulu",
    r"C:\Program Files\Amazon Corretto",
    r"C:\Program Files (x86)\Java"
]

def list_java_versions():
    # Filter out non-existing base directories
    availble_java_bases = []
    for base in java_bases:
        if os.path.isdir(base):
            availble_java_bases.append(base)
    if not availble_java_bases:
        raise FileNotFoundError("No Java installations found in the predefined directories.")
    # List all Java versions found in the available base directories
    versions =[]
    for java_base in availble_java_bases:
        for item in os.listdir(java_base):
            full_path = os.path.join(java_base, item, "bin")
            versions.append(full_path)
    return versions