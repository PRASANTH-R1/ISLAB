def encrypt(text, k):
    res = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            res += chr((ord(ch)-base+k)%26 + base)
        else:
            res += ch
    return res

def decrypt(text, k):
    return encrypt(text, -k)

msg = input("Enter text: ")
k = int(input("Shift: "))

c = encrypt(msg, k)
print("Encrypted:", c)
print("Decrypted:", decrypt(c, k))
