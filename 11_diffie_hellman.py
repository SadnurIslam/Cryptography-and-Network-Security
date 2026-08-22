# Find primitive root
def is_primitive_root(g, p):
    used = set()
    value = 1

    for _ in range(1, p):
        value = (value * g) % p
        if value in used:
            return False
        used.add(value)

    return len(used) == p - 1


def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return -1


# Input
p = int(input("Enter prime number (p): "))
# g = int(input("Enter primitive root (g): "))
g = find_primitive_root(p)

print("Primitive Root (g):", g)

a = int(input("Enter Alice private key: "))
b = int(input("Enter Bob private key: "))

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice Public Key:", A)
print("Bob Public Key:", B)

# Shared secret
key_alice = pow(B, a, p)
key_bob = pow(A, b, p)

print("Shared Secret Key:", key_alice, key_bob)