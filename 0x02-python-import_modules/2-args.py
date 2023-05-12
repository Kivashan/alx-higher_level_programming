#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    no_args = len(argv) - 1
    arg = "arguments"
    delim = ":"

    if (no_args == 1):
        arg = "argument"
    if (no_args == 0):
        delim = "."

    # print no of arguments
    print("{:d} {}{}".format(no_args, arg, delim))

    for i in range(1, no_args + 1):
        print("{:d}: {}".format(i, argv[i]))
