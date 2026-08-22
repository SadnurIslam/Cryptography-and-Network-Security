#include<bits/stdc++.h>
using namespace std;

string encrypt(string msg){
    int n = msg.size();
    string s = "";
    for(int i=0;i<n;i++){
        if(msg[i]>='a' && msg[i]<='z'){
            int cur = (msg[i]-'a'+3)%26+'a';
            s+=char(cur);
        }
        else if(msg[i]>='A' && msg[i]<='Z'){
            int cur = (msg[i]-'A'+3)%26+'A';
            s+=char(cur);
        }
        else{
            s+=msg[i];
        }
    }
    return s;
}

string decrypt(string cipher){
    int n = cipher.size();
    string s = "";
    for(int i=0;i<n;i++){
        if(cipher[i]>='a' && cipher[i]<='z'){
            int cur = (cipher[i]-'a'-3+26)%26+'a';
            s+=char(cur);
        }
        else if(cipher[i]>='A' && cipher[i]<='Z'){
            int cur = (cipher[i]-'A'-3+26)%26+'A';
            s+=char(cur);
        }
        else{
            s+=cipher[i];
        }
    }
    return s;
}

int main(){
    string msg,cipher,plain;
    cin>>msg;
    cipher = encrypt(msg);
    cout<<cipher<<endl;

    plain = decrypt(cipher);
    cout<<plain<<endl;
}
