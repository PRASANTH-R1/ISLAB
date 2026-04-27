import numpy as np

def mod_inv(a):
    for i in range(26):
        if (a*i) % 26 == 1:
            return i

def matrix_inv(m):
    det = int(np.round(np.linalg.det(m)))
    det_inv = mod_inv(det % 26)
    adj = np.round(det * np.linalg.inv(m)).astype(int)
    return (det_inv * adj) % 26

key = np.array([[3,3],[2,5]])
msg = input("Message: ").upper().replace(" ","")

if len(msg)%2 != 0:
    msg += 'X'

cipher = ""
for i in range(0,len(msg),2):
    pair = [ord(msg[i])-65, ord(msg[i+1])-65]
    res = np.dot(key, pair) % 26
    cipher += chr(res[0]+65)+chr(res[1]+65)

print("Encrypted:", cipher)

# Decryption
inv = matrix_inv(key)
plain = ""

for i in range(0,len(cipher),2):
    pair = [ord(cipher[i])-65, ord(cipher[i+1])-65]
    res = np.dot(inv, pair) % 26
    plain += chr(res[0]+65)+chr(res[1]+65)

print("Decrypted:", plain)
