#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    no_args = len(argv)
    total = 0

    for i in range(1, no_args):
        total += int(argv[i])

    print("{:d}".format(total))
