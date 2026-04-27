# Elliptic Curve: y^2 = x^3 + ax + b (mod p)

# Curve parameters (small values for demo)
p = 17
a = 2
b = 2

# Base point (generator)
G = (5, 1)


# -------------------------------
# Modular inverse
# -------------------------------
def mod_inv(x, p):
    for i in range(1, p):
        if (x * i) % p == 1:
            return i


# -------------------------------
# Point addition
# -------------------------------
def point_add(P, Q):
    if P == Q:
        # Point doubling
        lam = ((3 * P[0] * P[0] + a) * mod_inv(2 * P[1], p)) % p
    else:
        # Normal addition
        lam = ((Q[1] - P[1]) * mod_inv(Q[0] - P[0], p)) % p

    x3 = (lam * lam - P[0] - Q[0]) % p
    y3 = (lam * (P[0] - x3) - P[1]) % p

    return (x3, y3)


# -------------------------------
# Scalar multiplication
# -------------------------------
def scalar_mult(k, P):
    result = P
    for i in range(k - 1):
        result = point_add(result, P)
    return result


# -------------------------------
# Key Generation
# -------------------------------
private_key = 3   # choose any number < p
public_key = scalar_mult(private_key, G)

print("Private Key:", private_key)
print("Public Key:", public_key)
