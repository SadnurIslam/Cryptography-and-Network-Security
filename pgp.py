import hashlib
import random
import math
import zlib

# ==========================================================
# RSA KEY GENERATION
# ==========================================================

p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
while math.gcd(e, phi) != 1:
    e += 2

d = pow(e, -1, phi)

# ==========================================================
# COMMON FUNCTIONS
# ==========================================================

def sha256_hash(text):
    return int(hashlib.sha256(text.encode()).hexdigest(), 16)

def sign(message):
    h = sha256_hash(message)
    return pow(h, d, n)

def verify(message, signature):
    h = sha256_hash(message)
    recovered = pow(signature, e, n)
    return (h % n) == recovered

def xor_encrypt(data, key):
    return [b ^ key for b in data]

def xor_decrypt(cipher, key):
    return bytes([c ^ key for c in cipher])

# ==========================================================
# 12(a) / 13(a)
# PGP AUTHENTICATION
# ==========================================================

def authentication():
    print("\n--- PGP AUTHENTICATION ---")

    msg = input("Enter message: ")

    signature = sign(msg)

    packet = str(signature) + "|" + msg
    compressed = zlib.compress(packet.encode())

    print("Compressed Packet:", compressed.hex())

    # Receiver
    recovered = zlib.decompress(compressed).decode()
    sign_text, message = recovered.split("|", 1)

    if verify(message, int(sign_text)):
        print("\nAuthentication Successful")
        print("Message:", message)
    else:
        print("Authentication Failed")

# ==========================================================
# 12(b)
# CONFIDENTIALITY FOR TRANSMITTING DATA
# ==========================================================

def confidentiality_transmit():
    print("\n--- PGP CONFIDENTIALITY (TRANSMIT) ---")

    msg = input("Enter message: ")

    session_key = random.randint(1, 255)

    compressed = zlib.compress(msg.encode())

    cipher = xor_encrypt(compressed, session_key)

    encrypted_key = pow(session_key, e, n)

    print("\nTransmit:")
    print("Encrypted Session Key:", encrypted_key)
    print("Cipher Text:", " ".join(map(str, cipher)))

    # Receiver
    recovered_key = pow(encrypted_key, d, n)
    plain = xor_decrypt(cipher, recovered_key)
    plain = zlib.decompress(plain).decode()

    print("\nReceiver Plain Text:", plain)

# ==========================================================
# 13(b) / 14(a)
# CONFIDENTIALITY FOR STORING DATA
# ==========================================================

def confidentiality_store():
    print("\n--- PGP CONFIDENTIALITY (STORE) ---")

    msg = input("Enter message: ")

    session_key = random.randint(1, 255)

    compressed = zlib.compress(msg.encode())
    cipher = xor_encrypt(compressed, session_key)

    encrypted_key = pow(session_key, e, n)

    with open("encrypted_data.txt", "w") as f:
        f.write(str(encrypted_key) + "\n")
        f.write(" ".join(map(str, cipher)))

    print("Encrypted data stored in encrypted_data.txt")

    # Read back
    with open("encrypted_data.txt") as f:
        encrypted_key = int(f.readline())
        cipher = list(map(int, f.readline().split()))

    recovered_key = pow(encrypted_key, d, n)
    plain = xor_decrypt(cipher, recovered_key)
    plain = zlib.decompress(plain).decode()

    print("Recovered Plain Text:", plain)

# ==========================================================
# 14(b)
# AUTHENTICATION + CONFIDENTIALITY
# ==========================================================

def auth_and_confidentiality():
    print("\n--- PGP AUTHENTICATION + CONFIDENTIALITY ---")

    msg = input("Enter message: ")

    signature = sign(msg)

    data = str(signature) + "|" + msg

    compressed = zlib.compress(data.encode())

    session_key = random.randint(1, 255)

    cipher = xor_encrypt(compressed, session_key)

    encrypted_key = pow(session_key, e, n)

    print("\nTransmit:")
    print("Encrypted Session Key:", encrypted_key)
    print("Cipher:", " ".join(map(str, cipher)))

    # Receiver
    recovered_key = pow(encrypted_key, d, n)

    recovered = xor_decrypt(cipher, recovered_key)
    recovered = zlib.decompress(recovered).decode()

    sign_text, message = recovered.split("|", 1)

    if verify(message, int(sign_text)):
        print("\nVerified Message:", message)
        print("Authentication Successful")
    else:
        print("\nAuthentication Failed")

# ==========================================================
# MAIN
# Uncomment ONLY the required function in exam.
# ==========================================================

authentication()                 # Q12(a), Q13(a)

# confidentiality_transmit()     # Q12(b)

# confidentiality_store()        # Q13(b), Q14(a)

# auth_and_confidentiality()     # Q14(b)