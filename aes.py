from Crypto.Cipher import AES

# -------------------------------
# S-BOX GENERATION (AES)
# -------------------------------
def generate_sbox():
    sbox = [0] * 256

    def gf_mul(a, b):
        p = 0
        for i in range(8):
            if b & 1:
                p ^= a
            hi_bit = a & 0x80
            a <<= 1
            if hi_bit:
                a ^= 0x1B
            b >>= 1
        return p % 256

    def multiplicative_inverse(x):
        if x == 0:
            return 0
        for i in range(1, 256):
            if gf_mul(x, i) == 1:
                return i

    for i in range(256):
        inv = multiplicative_inverse(i)

        # Affine transformation
        s = inv
        for _ in range(4):
            s = (s << 1 | s >> 7) & 0xFF
            inv ^= s

        sbox[i] = inv ^ 0x63

    return sbox


# Generate and display S-Box
sbox = generate_sbox()

print("First 16 S-Box values:")
for i in range(16):
    print(hex(sbox[i]), end=" ")
print("\n")


# -------------------------------
# AES ENCRYPTION
# -------------------------------
key = b'1234567890123456'
cipher = AES.new(key, AES.MODE_ECB)

msg = "CONFIDENTIAL"

# Padding to 16 bytes
padded_msg = msg.ljust(16)

ciphertext = cipher.encrypt(padded_msg.encode())
print("Encrypted:", ciphertext)

plaintext = cipher.decrypt(ciphertext).decode().strip()
print("Decrypted:", plaintext)







from Crypto.Cipher import AES

key = b'1234567890123456'

cipher = AES.new(key, AES.MODE_ECB)

msg = "CONFIDENTIAL"

ciphertext = cipher.encrypt(msg.ljust(16).encode())
print("Encrypted:", ciphertext)

plaintext = cipher.decrypt(ciphertext).decode().strip()
print("Decrypted:", plaintext)
