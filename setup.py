import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\New folder\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\New folder\tcl\tk8.6"

executables = [cx_Freeze.Executable("car.py", base=base, icon="dodge.ico")]


cx_Freeze.setup(
    name = " car game",
    options = {"build_exe": {"packages":["tkinter","os","pygame","random","time"], "include_files":["dodge.ico",'tcl86t.dll','tk86t.dll','.idea',]}},
    version = "0.01",
    description = "car game",
    executables = executables
    )