#!/usr/bin/env python3

from challenge_3 import single_byte_xor_bruteforce
import string

lines = []
with open('4.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    for ans in single_byte_xor_bruteforce(line):
        print(ans)
