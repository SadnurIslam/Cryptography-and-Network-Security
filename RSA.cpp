#define ll long long

#include<bits/stdc++.h>
using namespace std;

ll binPow(ll a, ll b, ll m){
    a = a%m;
    ll res = 1;
    while(b>0){
        if(b&1)res = (res*a)%m;
        a = (a*a)%m;
        b>>=1;
    }
    return res;
}

vector<string> encrypt(string msg, ll e, ll n){
    vector<string>ciphers;
    for(ll i=0;i<msg.size();i=i+3){
        string block = msg.substr(i, 3);
        ll cur = stoll(block);
        ll cipher = binPow(cur, e, n);
        ciphers.push_back(to_string(cipher));
    }
    return ciphers;
}

vector<string> decrypt(vector<string> ciphers, ll d, ll n){
    vector<string> msgs;
    for(auto c:ciphers){
        ll cipher = stoll(c);
        ll msg = binPow(cipher, d, n);
        msgs.push_back(to_string(msg));
    }
    return msgs;
}

int main(){
    ll p, q;

    // cout<<"Enter two prime numbers: ";
    // cin>>p>>q;

    p = 47;
    q = 71;

    ll n = p*q;
    ll phi = (p-1)*(q-1);

    ll e = 79;  // choose at random
    while(__gcd(e, phi) != 1){
        e++;
    }
    cout << "Public key: (" << e << ", " << n << ")" << endl;

    ll d = 1;
    while((d*e) % phi != 1){
        d++;
    }
    cout << "Private key: (" << d << ", " << n << ")" << endl;

    string msg="6882326879666683";
    // cout<<"Plain text: ";
    // cin>>msg;

    vector<string>cipher = encrypt(msg,e,n);
    cout<<"Cipher text: ";
    for(auto c:cipher)cout<<c<<" ";
    cout<<endl;

    vector<string> decrypted = decrypt(cipher, d, n);
    cout<<"Decrypted text: ";
    for(auto m:decrypted)cout<<m<<" ";
    cout<<endl;
}