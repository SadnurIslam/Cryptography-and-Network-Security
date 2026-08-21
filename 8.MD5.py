import hashlib

text = input("Enter text: ")

encode = text.encode()

hashed = hashlib.md5(encode)

print("Hashed value: ", hashed.hexdigest())