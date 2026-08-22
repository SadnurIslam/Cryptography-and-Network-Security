# MILLER–RABIN PRIMALITY TEST ALGORITHM

# Step 1:
# Input an odd integer p and number of iterations k.

# Step 2:
# Handle special cases:
#     • If p < 2 → Composite
#     • If p = 2 or 3 → Prime
#     • If p is even → Composite

# Step 3:
# Write p − 1 as:

#     p − 1 = 2^b × m

# where m is odd.

# Step 4:
# Repeat k times:

#     a. Choose a random integer a such that
#        2 ≤ a ≤ p − 2

#     b. Compute
#        z = a^m mod p

#     c. If z = 1 or z = p − 1,
#        go to the next iteration.

#     d. Repeat (b − 1) times:
#          z = z² mod p

#          If z = p − 1:
#              Pass this iteration.

#          If z = 1:
#              Return Composite.

#     e. If p − 1 is never obtained,
#        Return Composite.

# Step 5:
# If all iterations pass,
# Return Probably Prime.


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