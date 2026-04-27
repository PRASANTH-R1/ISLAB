p = 23
g = 7

a = 11
b = 15

A = pow(g, a, p)
B = pow(g, b, p)

key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Shared Key A:", key1)
print("Shared Key B:", key2)
