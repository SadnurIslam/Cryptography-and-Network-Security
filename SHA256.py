import hashlib

# Input from user
text = input("Enter text: ")

# Generate SHA-256 hash
sha_hash = hashlib.sha256(text.encode())

# Print hexadecimal hash value
print("SHA-256 Hash:", sha_hash.hexdigest())