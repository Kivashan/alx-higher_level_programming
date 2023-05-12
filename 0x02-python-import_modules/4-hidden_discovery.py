#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    temp = dir(hidden_4)

    for i in temp:
        if (i[0] == '_'):
            continue
        print("{}".format(i))
