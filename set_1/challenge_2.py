#!/usr/bin/env python3

hex_string = '1c0111001f010100061a024b53535009181c'
hex_bytes = bytes.fromhex(hex_string)
xor_key = bytes.fromhex('686974207468652062756c6c277320657965')
xor_output = bytes([x[0] ^ x[1] for x in zip(hex_bytes, xor_key)])
print(xor_output.hex())
