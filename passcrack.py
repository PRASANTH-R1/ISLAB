password = "admin123"

wordlist = ["123456", "password", "admin", "admin123"]

for word in wordlist:
    if word == password:
        print("Password Cracked:", word)
        break
