import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","tkinter","ttkthemes"] ,"excludes": ["matplotlib","sqlite3","numpy","pandas"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "vALGO",
        version = "0.1",
        description = "An application build for students to visualise data structure",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main2.py", base=base)]
       )