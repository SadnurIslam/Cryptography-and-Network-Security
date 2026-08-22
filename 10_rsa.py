import math

def encrypt(msg, e, n):
    cipher = []
    for i in range(0, len(msg), 3):
        block = msg[i:i+3]
        m = int(block)
        c = pow(m, e, n)
        cipher.append(str(c))
    return cipher

def decrypt(cipher, d, n):
    plain = []
    for c in cipher:
        m = pow(int(c), d, n)
        plain.append(str(m))
    return plain


# Input two prime numbers
p = 47
q = 71

n = p * q
phi = (p - 1) * (q - 1)

# Choose public exponent
e = 79
while math.gcd(e, phi) != 1:
    e += 1

# Built-in modular inverse
d = pow(e, -1, phi)

print("Public Key :", (e, n))
print("Private Key:", (d, n))

msg = "6882326879666683"

cipher = encrypt(msg, e, n)
print("Cipher Text:", " ".join(cipher))

plain = decrypt(cipher, d, n)
print("Decrypted Text:", " ".join(plain))