#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    size = len(arguments) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, arguments[i]))
    elif size == 0:
        print("{} arguments.".format(size))
    else:
        print("{} arguments:".format(size))
        print("{}: {}".format(size, arguments[1]))
