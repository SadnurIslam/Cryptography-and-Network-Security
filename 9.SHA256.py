import hashlib

# Input from user
text = input("Enter text: ")

encode = text.encode()

# Generate SHA-256 hash
sha_hash = hashlib.sha256(encode)

hashed = sha_hash.hexdigest()

# Print hexadecimal hash value
print("SHA-256 Hash:", hashed)