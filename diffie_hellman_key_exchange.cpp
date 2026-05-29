#include <iostream>
using namespace std;



// // if g not given as input 
// bool isPrimitiveRoot(long long g, long long p)
// {
//     bool used[100000] = {false};
    
//     long long value = 1;

//     for (long long i = 1; i < p; i++)
//     {
//         value = (value * g) % p;

//         if (used[value])
//             return false;

//         used[value] = true;
//     }

//     return true;
// }

// long long findPrimitiveRoot(long long p)
// {
//     for (long long g = 2; g < p; g++)
//     {
//         if (isPrimitiveRoot(g, p))
//             return g;
//     }
//     return -1;
// }


// Function for modular exponentiation
long long power(long long base, long long exp, long long mod)
{
    long long result = 1;

    while (exp > 0)
    {
        if (exp % 2 == 1)
        {
            result = (result * base) % mod;
        }

        base = (base * base) % mod;
        exp = exp / 2;
    }

    return result;
}

int main()
{
    long long p, g;
    long long a, b;

    // Input public values
    cout << "Enter prime number (p): ";
    cin >> p;

    cout << "Enter primitive root (g): ";
    cin >> g;

    // // if g not given as input, find it
    //  g = findPrimitiveRoot(p);
    //  cout<<"Primitive root (g): " << g << endl;

    // Input private keys
    cout << "Enter Alice private key (a): ";
    cin >> a;

    cout << "Enter Bob private key (b): ";
    cin >> b;

    // Generate public keys
    long long A = power(g, a, p);
    long long B = power(g, b, p);

    cout << "\nAlice Public Key: " << A << endl;
    cout << "Bob Public Key: " << B << endl;

    // Generate shared secret keys
    long long keyAlice = power(B, a, p);
    long long keyBob = power(A, b, p);

    cout << "\nShared Secret Key for Alice: " << keyAlice << endl;
    cout << "Shared Secret Key for Bob: " << keyBob << endl;

    // Verify keys
    if (keyAlice == keyBob)
    {
        cout << "\nKey Exchange Successful!" << endl;
    }
    else
    {
        cout << "\nKey Exchange Failed!" << endl;
    }

    return 0;
}