#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv) - 1
    if (nargs == 0):
        print(f"{nargs:d} arguments.")
    elif (nargs == 1):
        print(f"{nargs:d} argument:")
    else:
        print(f"{nargs:d} arguments:")
    for str in range(len(sys.argv)):
        if (str == 0):
            continue
        print(f"{str:d}: {sys.argv[str]:s}")
