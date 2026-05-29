'''
1. use python when we need big integer like 512 bit number
2. use python bcz it support built in pow(a,b,mod)
'''

import random

def lehmann_test(p, iterations=20):

    if p < 2:
        return False

    if p % 2 == 0 and p != 2:
        return False

    for _ in range(iterations):

        a = random.randint(2, p - 2)  # 1<a<p-1

        r = pow(a, (p - 1) // 2, p)

        if r != 1 and r != p - 1:
            return False

    return True


# Generate random 512-bit odd number
n = random.getrandbits(512) # take a random 512 bit number
n |= 1  # make it odd
# n=13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171

print("Generated Number:\n")
print(n)

if lehmann_test(n):
    print("\nProbably Prime")
else:
    print("\nComposite")