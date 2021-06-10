import sys
from cx_Freeze import setup,Executable

build_exe_options = {"packages":["os","tkinter","ttkthemes","pyttsx3"],"excludes":["matplotlib","numpy","sqlite3","pandas"]}

base = None

if sys.platform == "win32":
    base = "Win32GUI"


setup(  name = "vALGO",
        version = "0.1",
        description = "An application build for students to visualise data structure",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main2.py", base=base)]
       )