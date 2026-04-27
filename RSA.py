def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

p = 17
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = mod_inverse(e, phi)

msg = 9

cipher = pow(msg, e, n)
plain = pow(cipher, d, n)

print("Public key:", (e, n))
print("Private key:", (d, n))
print("Encrypted:", cipher)
print("Decrypted:", plain)
