import hashlib

# Input from user
text = input("Enter text: ")

# Convert text to MD5 hash
md5_hash = hashlib.md5(text.encode())

# Print hexadecimal hash value
print("MD5 Hash:", md5_hash.hexdigest())