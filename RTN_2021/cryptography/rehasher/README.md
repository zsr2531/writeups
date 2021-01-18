# rehasher

> I wrote a new asymmetric encryption algorithm, and it is truly unbreakable!
>
>Don't believe me? What if I told you I repeatedly hashed the input using SHA-256?
>
>See you in fifty million years or so when you finally bruteforced my private key! >:)
>

Apart from the message description above, we get the [Python source code](smoothiecrypt.py) to this very sophisticated encryption algorithm.

```py
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
```

Looks intimidating, right? Well... not so fast.

## A couple of notes

Just by skimming over the source code quickly, we can deduce a few things:

1. It claims to be an asymmetric encryption algorithm, where the blocks are 16 bytes long.

2. The input message is padded with zero bytes (`\0`) if it isn't exactly the right length.

3. The input and the output are exactly the same length.

## What is *actually* going on here?

Well, in order to get an answer to that question, let's break down the `encrypt_block` function!

- At the beginning, it defines two variables; `a` and `b`.
- Afterwards, each of them is initialized with half of the current block (`a` with the first half, `b` with the second).
- And now, for every byte of the input key we
  - ... take the first 8 bytes (half of the block length) of the SHA-256 digest of `b`, plus the current byte of the key as salt, and assign it to `c`.
  - ... XOR `c` with `a` byte by byte and assign it to `b`.
  - ... assign the value of `b` to `a`.
- And finally we concatenate the two half blocks (`b + a`) and we're done.

So, what do we do now? SHA-256 cannot be reversed... right? Well no, but here? ...also no...

## The kicker

Even though SHA-256 *is* a secure hashing algorithm, the way it's used here doesn't make a big difference. Why? Well... let's think about it for a second. The XOR operation there basically gives us a backdoor. Just by reversing the key, we can break this! All we have to do is slap `[::-1]` after `bytes.fromhex(sys.argv[2])` and run it with the input given in the description of the challenge. And just like [that](solution.py), we get a hex string, which is just ASCII for `RTN{3ncrypt_b3c0m3s_D3crypT_1f_K3y_is_R3v3rs3d}`. Wonderful. (note that in my solution I perform the ASCII conversion, so you get the flag directly, rather than a hex string)
