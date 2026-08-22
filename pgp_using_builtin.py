from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import zlib

# ==========================================================
# RSA KEY GENERATION
# ==========================================================

key = RSA.generate(1024)
private_key = key
public_key = key.publickey()

# ==========================================================
# COMMON FUNCTIONS
# ==========================================================

# ---------- Authentication ----------
def sign_message(message):
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def verify_message(message, signature):
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except:
        return False

# ---------- AES Confidentiality ----------
def aes_encrypt(message):
    session_key = get_random_bytes(16)

    cipher = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())

    rsa_cipher = PKCS1_OAEP.new(public_key)
    enc_session_key = rsa_cipher.encrypt(session_key)

    return enc_session_key, cipher.nonce, tag, ciphertext

def aes_decrypt(enc_session_key, nonce, tag, ciphertext):
    rsa_cipher = PKCS1_OAEP.new(private_key)
    session_key = rsa_cipher.decrypt(enc_session_key)

    cipher = AES.new(session_key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext.decode()

# ==========================================================
# Q12(a) / Q13(a)
# PGP AUTHENTICATION
# ==========================================================

def authentication():
    print("\n===== PGP AUTHENTICATION =====")

    message = input("Enter Message: ")

    signature = sign_message(message)

    packet = signature + message.encode()
    compressed = zlib.compress(packet)

    # ---------- Receiver ----------
    received = zlib.decompress(compressed)

    sig_len = private_key.size_in_bytes()

    recv_signature = received[:sig_len]
    recv_message = received[sig_len:].decode()

    if verify_message(recv_message, recv_signature):
        print("\nAuthentication Successful")
        print("Message:", recv_message)
    else:
        print("Authentication Failed")

# ==========================================================
# Q12(b)
# CONFIDENTIALITY FOR TRANSMITTING DATA
# ==========================================================

def confidentiality_transmit():
    print("\n===== CONFIDENTIALITY (TRANSMIT) =====")

    message = input("Enter Message: ")

    enc_key, nonce, tag, cipher = aes_encrypt(message)

    print("\nData Transmitted Successfully")

    # ---------- Receiver ----------
    plain = aes_decrypt(enc_key, nonce, tag, cipher)

    print("Recovered Message:", plain)

# ==========================================================
# Q13(b) / Q14(a)
# CONFIDENTIALITY FOR STORING DATA
# ==========================================================

def confidentiality_store():
    print("\n===== CONFIDENTIALITY (STORE) =====")

    message = input("Enter Message: ")

    enc_key, nonce, tag, cipher = aes_encrypt(message)

    # Store into file
    with open("encrypted_data.bin", "wb") as f:
        f.write(len(enc_key).to_bytes(2, "big"))
        f.write(enc_key)
        f.write(nonce)
        f.write(tag)
        f.write(cipher)

    print("Encrypted file stored.")

    # ---------- Read Again ----------
    with open("encrypted_data.bin", "rb") as f:

        key_len = int.from_bytes(f.read(2), "big")

        enc_key = f.read(key_len)
        nonce = f.read(16)
        tag = f.read(16)
        cipher = f.read()

    plain = aes_decrypt(enc_key, nonce, tag, cipher)

    print("Recovered Message:", plain)

# ==========================================================
# Q14(b)
# AUTHENTICATION + CONFIDENTIALITY
# ==========================================================

def auth_and_confidentiality():
    print("\n===== AUTHENTICATION + CONFIDENTIALITY =====")

    message = input("Enter Message: ")

    # Step 1: Digital Signature
    signature = sign_message(message)

    # Step 2: Attach Signature
    packet = signature + message.encode()

    # Step 3: Compress
    compressed = zlib.compress(packet)

    # Step 4: AES Encryption
    session_key = get_random_bytes(16)

    aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = aes.encrypt_and_digest(compressed)

    # Step 5: Encrypt Session Key using RSA
    rsa = PKCS1_OAEP.new(public_key)
    enc_session_key = rsa.encrypt(session_key)

    print("\nEncrypted Packet Sent")

    # ==================================================
    # Receiver
    # ==================================================

    rsa = PKCS1_OAEP.new(private_key)
    session_key = rsa.decrypt(enc_session_key)

    aes = AES.new(session_key, AES.MODE_EAX, aes.nonce)
    decompressed = aes.decrypt_and_verify(ciphertext, tag)

    packet = zlib.decompress(decompressed)

    sig_len = private_key.size_in_bytes()

    recv_signature = packet[:sig_len]
    recv_message = packet[sig_len:].decode()

    if verify_message(recv_message, recv_signature):
        print("\nAuthentication Successful")
        print("Recovered Message:", recv_message)
    else:
        print("Authentication Failed")

# ==========================================================
# MAIN
# Uncomment ONLY ONE according to the exam question.
# ==========================================================

# authentication()                 # Q12(a), Q13(a)

# confidentiality_transmit()       # Q12(b)

# confidentiality_store()          # Q13(b), Q14(a)

auth_and_confidentiality()         # Q14(b)