#!/usr/bin/env python3

from challenge_5 import repeating_key_xor
import base64

# lines = []
# with open('6.txt', 'r') as f:
#     for line in f:
#         line = line.strip()
#         line = base64.b64decode(line)
#         lines.append(line.strip())
    
# for line in lines:
#     print(line)

def hamming_distance(a, b):
    length = min(len(a), len(b))
    xor_result = ''.join([f"{ord(a[i]) ^ ord(b[i]):b}" for i in range(length)])
    count_diff = [1 for ch in xor_result if ch == '1']
    return len(count_diff)

print(hamming_distance('this is a test', 'wokka wokka!!!'))
