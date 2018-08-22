#!/usr/bin/env python3

import string

hex_encoded_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def single_byte_xor_bruteforce(hex_encoded_str: str) -> str:
    hex_bytes = bytes.fromhex(hex_encoded_str)
    for i in string.printable:
        decoded = ''.join([chr(x ^ ord(i)) for x in hex_bytes])
        
        is_valid = ' ' in decoded
        for ch in decoded:
            is_valid &= ch in string.printable
        
        if is_valid:
            yield decoded


if __name__ == "__main__":
    for ans in single_byte_xor_bruteforce(hex_encoded_str):
        print(ans)
