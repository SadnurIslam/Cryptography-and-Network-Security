/*
1. Write p-1 as 2^b * m where m is odd
2. Pick a random integer a such that 1 < a < p-1
3. Compute z = a^m mod p
4. If z == 1 or z == p-1, then p is probably prime
5. else,  For j = 1 to b-1, compute z = z^2 mod p
   - If z == p-1, then p is probably prime
   - If z == 1, then p is composite
   - if after b-1 iterations, z is not p-1 in any interation, then p is composite
6. Repeat the above steps for a certain number of iterations to increase confidence level


*/

#define ll long long
#include <bits/stdc++.h>
using namespace std;


ll mod_pow(ll a, ll d, ll mod)
{
    ll result = 1;
    while (d > 0)
    {
        if (d % 2 == 1)
            result = (result * a) % mod;

        a = (a * a) % mod;
        d /= 2;
    }
    return result;
}

bool millerRabin(ll p, int iterations = 10)
{
    if (p < 2)
        return false;
    if (p == 2 || p == 3)
        return true;
    if (p % 2 == 0)
        return false;

    // Step 1: p-1 = 2^b * m
    ll m = p - 1;
    int b = 0;

    while (m % 2 == 0)
    {
        m /= 2;
        b++;
    }

    for (int i = 0; i < iterations; i++)
    {
        // Step 2: pick a
        ll a = 2 + rand() % (p - 3);

        // Step 3: z = a^m mod p
        ll z = mod_pow(a, m, p);

        // Step 4: check
        if (z == 1 || z == p - 1)
            continue;

        bool passed = false;

        // Step 5: square up to b-1 times
        for (int j = 1; j < b; j++)
        {
            z = (z * z) % p;

            if (z == p - 1)
            {
                passed = true;
                break;
            }

            if (z == 1)
                return false; // composite
        }

        if (!passed)
            return false;
    }

    return true;
}

int main()
{
    ll p;
    cout << "Enter number: ";
    cin >> p;

    if (millerRabin(p, 20))
        cout << "Probably Prime\n";
    else
        cout << "Composite\n";

    return 0;
}