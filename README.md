# simpleJavaVersionSwitcher
This is a small, lightweight Python/Tkinter app to help you switch between installed Java versions on Windows.  
It will update your `JAVA_HOME` system variable with admin privileges.

## Features
- Fetch the installed java versions
- Updates `JAVA_HOME` user/system-wide (or both)
- Tkinter GUI—super simple and lightweight.

## Note
This is a small personal project I built for my own use and decided to share.

## Code
There are 4 main files:
- *simple_java_switcher.py* that represents the main and holds the GUI logic.
- *modulesfetcher.py* that fetches the existing java versions from a pre-defined set of paths.
- *modules/clicker.py* that holds the whole button click logic and triggers the variable editing.
- *util/admin.py* that check and relaunch the app when admin previliges are required (for when a system variable edit is triggered)
