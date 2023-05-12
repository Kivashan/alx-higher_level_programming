#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    argv = sys.argv
    no_args = len(argv)
    total = 0
    op = argv[2]

    if (no_args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if (op[0] == '+'):
        total = int(argv[1]) + int(argv[3])
        print("{:d} + {:d} = {:d}".format(int(argv[1]), int(argv[3]), total))
    elif (op[0] == "-"):
        total = int(argv[1]) - int(argv[3])
        print("{:d} - {:d} = {:d}".format(int(argv[1]), int(argv[3]), total))
    elif (op[0] == "*"):
        total = int(argv[1]) * int(argv[3])
        print("{:d} * {:d} = {:d}".format(int(argv[1]), int(argv[3]), total))
    elif (op[0] == "/"):
        total = int(argv[1]) / int(argv[3])
        print("{:f} / {:f} = {:f}".format(int(argv[1]), int(argv[3]), total))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
