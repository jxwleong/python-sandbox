import sys

print(sys.argv)

arg_str = ""
if len(sys.argv) > 0:
    for arg in sys.argv:
        arg_str += str(arg) + " "
print(f"{sys.executable} {arg_str}")