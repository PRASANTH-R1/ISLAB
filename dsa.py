from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key = DSA.generate(2048)
public_key = key.publickey()

message = b"Hello World"
hash_obj = SHA256.new(message)

signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)

print("Signature:", signature)

verifier = DSS.new(public_key, 'fips-186-3')
try:
    verifier.verify(hash_obj, signature)
    print("Signature Verified")
except:
    print("Verification Failed")
