import random
import math

def miller_rabin(p, steps):
    if p <2:
        return False
    if p in (2,3):
        return True
    if p%2==0 and p!=2:
        return False
    m = p-1
    b = 0
    while m%2==0:
        b+=1
        m//=2
    for i in range(steps):
        a = random.randint(2,p-2)
        z = pow(a,m,p)
        if z==1 or z==p-1:
            continue
        passed = False
        
        for i in range(b-1):
            z = pow(z,2,p)
            if z ==p-1:
                passed=True
                break
            if z==1:
                return False
        if not passed:
            return False

    return True




n = random.getrandbits(512)
n|=1
print(n)
if miller_rabin(n,20):
    print("\nProbably prime")
else:
    print("\nComposite")