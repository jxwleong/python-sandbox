import os
import glob


cwd = os.getcwd()
cfd = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#path = os.path.join(cwd, "**", "*.py")
print(cfd)
print(root_dir)
path = os.path.join(cfd, "**", "*.py")
print(path)
# Explanation on recursive
# https://stackoverflow.com/a/55259781
files = glob.glob(path)
print("W/O recursive: " + str(files))
files = glob.glob(path, recursive=True)
print("With recursive: " + str(files))