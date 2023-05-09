#!/usr/bin/python3
a = 97
for a in range(a, a + 26):
    if (chr(a) == 'q') or (chr(a) == 'e'):
        continue
    print("{:c}".format(a), end='')
