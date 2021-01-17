import hashlib
import sys 
import math

BLOCK_SIZE = 16

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
    if len(sys.argv) <= 1:
        print(f"Usage {sys.argv[0]} <plain_text> <public_key>")
        sys.exit(0)

    p = bytes.fromhex(sys.argv[1])
    k = bytes.fromhex(sys.argv[2])

    encrypted = encrypt(p, k)
    print(encrypted.hex())
    
