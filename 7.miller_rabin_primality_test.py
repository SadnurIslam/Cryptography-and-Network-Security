# write in python when need to work with big integer like 512 bit number


import random

def miller_rabin(p, iterations=20):

    # Step 0: handle small cases
    if p < 2:
        return False
    if p in (2, 3):
        return True
    if p % 2 == 0:
        return False

    # Step 1: write p-1 = 2^b * m
    m = p - 1
    b = 0

    while m % 2 == 0:
        m //= 2
        b += 1

    # Step 2: repeat test
    for _ in range(iterations):

        # pick a in [2, p-2]
        a = random.randint(2, p - 2)

        # Step 3: z = a^m mod p
        z = pow(a, m, p)

        # Step 4: check
        if z == 1 or z == p - 1:
            continue

        # Step 5: square up to b-1 times
        passed = False

        for _ in range(b - 1):
            z = pow(z, 2, p)

            if z == p - 1:
                passed = True
                break

            if z == 1:
                return False  # composite

        if not passed:
            return False

    return True



n = random.getrandbits(512) # take a random 512 bit number
n |= 1  # make it odd
# n= 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171

print("Generated Number:\n")
print(n)

if miller_rabin(n, 20):
    print("Probably Prime")
else:
    print("Composite")