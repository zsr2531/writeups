import hashlib
import sys 
import math

BLOCK_SIZE = 16
CIPHER_TEXT = "15e1c8c4bd2fcb12838d3f48e8fc567adf4fac1c36648eb270ad899a717dfadfccd9b49fc32a726711dd1d7faab7ed81"
PUBLIC_KEY = "537472347762337272795f536d303074686933535f42337374"

def encrypt(plain_text, key):
    result = bytearray()

    padding_size = math.ceil(len(plain_text) / BLOCK_SIZE) * BLOCK_SIZE
    plain_text = plain_text.ljust(padding_size, b'\0')

    for i in range(0, len(plain_text), BLOCK_SIZE):
        result.extend(encrypt_block(plain_text[i:i+BLOCK_SIZE], key))

    return result


def encrypt_block(block, key):
    a = block[0:BLOCK_SIZE // 2]
    b = block[BLOCK_SIZE // 2:BLOCK_SIZE]

    for k in key:
        c = hashlib.sha256(b + bytes([k])).digest()[0:BLOCK_SIZE // 2]
        a, b = b, bytes(x ^ y for x, y in zip(c, a))

    return b + a


if __name__ == "__main__":
    p = bytes.fromhex(CIPHER_TEXT)
    k = bytes.fromhex(PUBLIC_KEY)[::-1]

    encrypted = encrypt(p, k)
    print(''.join([chr(x) for x in encrypted]))
    
