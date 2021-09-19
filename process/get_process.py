"""
Demonstrate to get psutil Process object given process naem
"""

# https://stackoverflow.com/a/2241047
import psutil

PROCNAME = "python.exe"

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        print(proc)