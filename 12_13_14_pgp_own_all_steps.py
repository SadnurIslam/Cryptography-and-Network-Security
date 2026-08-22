import hashlib
import zlib
import math
import random


def isprime(n):
    if n<2:
        return False
    for i in range(2, int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True

def key_generate():
    p = random.randint(23,100)
    while not isprime(p):
        p = random.randint(23,100)

    q = random.randint(23,100)
    while not isprime(q):
            q = random.randint(23,100)

    n = p*q
    phi = (p-1)*(q-1)

    e = 3

    while math.gcd(e,phi)!=1:
         e+=2

    d = pow(e,-1,phi)

    return (e,n),(d,n)

def hashing(msg):
     encode = msg.encode()
     hashed = hashlib.sha256(encode)
     return int(hashed.hexdigest(),16)

def sign(msg, key):
     h = hashing(msg)
     d,n = key
     return pow(h,d,n)

def verify(msg, sign, key):
     h = hashing(msg)
     e,n=key
     recovered = pow(sign, e,n)
     return (h%n)==recovered

def xor_encrypt(msg, key):
     return [b^key for b in msg]

def xor_decrypt(cipher, key):
     return bytes([c^key for c in cipher])

def encrypt_key(session_key, key):
     e,n = key
     return pow(session_key, e, n)

def decrypt_key(encrypted_key, key):
     d,n = key
     return pow(encrypted_key,d,n)



sender_pub, sender_pri = key_generate()
rcv_pub, rcv_pri = key_generate()

print("Sender key: ", sender_pri, sender_pub)
print("\nReceiver key: ", rcv_pri, rcv_pub)

#authentication
def auth():
     #sender
    msg = input("Enter msg: ")
    signature = sign(msg, sender_pri)
    packet = str(signature)+"|"+msg
    compressed = zlib.compress(packet.encode())

    print("\nSend msg: ", msg)
    print("\nSend packet: ", packet)
    print("\nSend compressed: ", compressed)

    #reciver
    decompressed = zlib.decompress(compressed).decode()
    sign_txt, rcv_msg = decompressed.split("|",1)

    if verify(rcv_msg, int(sign_txt), sender_pub):
        print("\nAuthentication successfull")
        print("\nRecieved msg: ", rcv_msg)
    else:
        print("\nAuthentication is not successful")

def confidential_transmission():
    #sender
    msg = input("Enter msg: ")
    compressed = zlib.compress(msg.encode())
    session_key = random.randint(1,255)
    cipher = xor_encrypt(compressed, session_key)
    encrypted_key = encrypt_key(session_key,rcv_pub)

    print("\nSending msg: ",msg)
    print("\nSending cipher: ", cipher)
    print("\nSending encrypted key: ",encrypted_key)

    #receiver
    decrypted_session_key = decrypt_key(encrypted_key, rcv_pri)
    plain = xor_decrypt(cipher, decrypted_session_key)
    decompressed = zlib.decompress(plain).decode()

    print("\nReceived msg: ",decompressed)

def confidential_store():
     #sender
     msg = input("Enter msg: ")
     compressed = zlib.compress(msg.encode())
     session_key = random.randint(1,255)
     cipher = xor_encrypt(compressed, session_key)
     encrypted_session_key = encrypt_key(session_key, rcv_pub)

     with open("zzz.txt", "w") as f:
          f.write(str(encrypted_session_key)+"\n")
          f.write(" ".join(map(str,cipher)))

    #receiver
     with open("zzz.txt") as f:
        recieved_key = int(f.readline())
        recieved_cipher = list(map(int, f.readline().split()))

     decrypted_session_key = decrypt_key(recieved_key, rcv_pri)
     plain = xor_decrypt(recieved_cipher, decrypted_session_key)
     plain = zlib.decompress(plain).decode()

     print("\nsession key: ", decrypted_session_key)
     print("\nplain text: ", plain)


def auth_and_confidential():
    #sender
    msg = input("Enter msg")
    signature = sign(msg, sender_pri)
    packet = str(signature)+"|"+msg
    compressed = zlib.compress(packet.encode())
    session_key = random.randint(1,255)
    cipher = xor_encrypt(compressed, session_key)
    encrypted_session_key = encrypt_key(session_key, rcv_pub)

    print("\nmsg: ",msg)
    print("\nsignature: ",signature)
    print("\nsession key: ",session_key)
    print("\nencrypted_session key: ",encrypted_session_key)
    print("\ncipher: "," ".join(map(str,cipher)))

    #receiver
    decrypted_sesion_key = decrypt_key(encrypted_session_key, rcv_pri)
    plain = xor_decrypt(cipher, decrypted_sesion_key)
    plain = zlib.decompress(plain).decode()
    sign_txt , msg_txt = plain.split("|",1)

    if verify(msg_txt, int(sign_txt), sender_pub):
        print("\nAuthentication successful")
        print("\nDecrypted session key: ", decrypted_sesion_key)
        print("\nmsg: ", msg_txt)
    else:
         print("Authentication failed!")

# auth()
# confidential_transmission()
# confidential_store()
auth_and_confidential()