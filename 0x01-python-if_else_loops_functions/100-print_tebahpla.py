#!/usr/bin/python3

num = 122

for i in range(26):
    print("{}".format(chr(num) if num % 2 == 0 else chr(num - 32)), end='')
    num -= 1
