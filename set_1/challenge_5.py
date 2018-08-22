#!/usr/bin/env python3

def repeating_key_xor(plaintext, xor_key):
    encoded_bytes = []
    xor_i = 0
    for byte in bytes(plaintext, 'utf-8'):
        if xor_i >= len(xor_key):
            xor_i = 0

        encoded_bytes.append(ord(xor_key[xor_i]) ^ byte)
        xor_i += 1

    return bytes(encoded_bytes).hex()

if __name__ == "__main__":
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    xor_key = "ICE"
    print(repeating_key_xor(plaintext, xor_key))
