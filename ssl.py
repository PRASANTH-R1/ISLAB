#!/bin/bash

echo "=============================="
echo "OPENSSL LAB - ALL IN ONE"
echo "=============================="

# Create sample file
echo "Hello Information Security Lab" > input.txt

echo "\n[1] SYMMETRIC ENCRYPTION (AES)"

# Encrypt
openssl enc -aes-256-cbc -salt -in input.txt -out encrypted.enc -pass pass:1234
echo "Encrypted file created: encrypted.enc"

# Decrypt
openssl enc -d -aes-256-cbc -in encrypted.enc -out decrypted.txt -pass pass:1234
echo "Decrypted file created: decrypted.txt"

echo "\n[2] ASYMMETRIC ENCRYPTION (RSA)"

# Generate keys
openssl genrsa -out private.key 2048
openssl rsa -in private.key -pubout -out public.key

# Encrypt using public key
openssl pkeyutl -encrypt -pubin -inkey public.key -in input.txt -out encrypted_rsa.dat

# Decrypt using private key
openssl pkeyutl -decrypt -inkey private.key -in encrypted_rsa.dat -out decrypted_rsa.txt

echo "RSA Encryption/Decryption Done"

echo "\n[3] MESSAGE DIGEST (SHA-256)"

openssl dgst -sha256 input.txt

echo "\n[4] DIGITAL SIGNATURE"

# Sign
openssl dgst -sha256 -sign private.key -out signature.bin input.txt
echo "Signature created"

# Verify
openssl dgst -sha256 -verify public.key -signature signature.bin input.txt

echo "\n=============================="
echo "ALL OPERATIONS COMPLETED"
echo "=============================="
