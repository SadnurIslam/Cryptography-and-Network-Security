/*
Step:
1. take a random number a such that 1 < a < p-1
2. compute r = a^((p-1)/2) mod p
3. if r != 1 and r != p-1, then p is definitely composite
4. repeat the above steps for a certain number of iterations to increase confidence level
5. if all iterations pass, then p is probably prime
*/

#define ll long long
#include <bits/stdc++.h>
using namespace std;

ll power(ll a, ll b, ll mod)
{
    ll result = 1;

    while(b > 0)
    {
        if(b % 2 == 1)
            result = (result * a) % mod;

        a = (a * a) % mod;
        b /= 2;
    }

    return result;
}

bool lehmannTest(ll p, int iterations = 5)
{
    if(p < 2)
        return false;

    if(p % 2 == 0 && p != 2)
        return false;

    for(int i = 0; i < iterations; i++)
    {
        ll a = 2 + rand() % (p - 3);  // 1 < a < p-1

        ll r = power(a, (p - 1) / 2, p);

        if(r != 1 && r != p - 1)
            return false;
    }

    return true;
}

int main()
{
    ll n;

    cout << "Enter number: ";
    cin >> n;

    if(lehmannTest(n))
        cout << "Probably Prime" << endl;
    else
        cout << "Composite" << endl;

    return 0;
}