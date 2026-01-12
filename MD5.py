

# import hashlib

# def hash_string(input_string):
#         # Create an MD5 hash object
#         md5_hash = hashlib.md5()
        
#         # Update the hash object with the bytes of the input string
#         md5_hash.update(input_string.encode('utf-8'))
        
#         # Return the hexadecimal representation of the hash
#         return md5_hash.hexdigest()

#     # Example usage
# if __name__ == "__main__":
#         test_string = input("Enter a string to hash using MD5: ")
#         print(f"MD5 hash of '{test_string}': {hash_string(test_string)}")

import struct

# Left rotation helper
def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

# MD5 from scratch
def md5(message: bytes) -> str:
    # Step 1: Initialize variables
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Step 2: Pre-processing (padding)
    original_len_bits = (8 * len(message)) & 0xffffffffffffffff
    message += b"\x80"
    while (len(message) % 64) != 56:
        message += b"\x00"
    message += struct.pack("<Q", original_len_bits)

    # Step 3: Define constants
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
    K = [int(abs(__import__('math').sin(i + 1)) * (1 << 32)) & 0xFFFFFFFF for i in range(64)]

    # Step 4: Process each 512-bit block
    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset:chunk_offset + 64]
        M = list(struct.unpack("<16I", chunk))

        a, b, c, d = A, B, C, D

        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | (~d & c)
                g = (5*i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3*i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7*i) % 16

            f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(f, s[i])) & 0xFFFFFFFF

        # Add this chunk's hash to result
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Step 5: Produce the final digest (little-endian)
    return ''.join(format(x, '02x') for x in struct.pack("<4I", A, B, C, D))


# --------------------------
# 🔹 Test the implementation
# --------------------------
print(md5(b"hello"))        # should be 5d41402abc4b2a76b9719d911017c592
print(md5(b"hello world"))  # should be 5eb63bbbe01eeed093cb22bb8f5acdc3

