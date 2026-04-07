#include<bits/stdc++.h>
using namespace std;

int main(){
    cout<<"Plain text: "<<endl;
    string msg;
    cin>>msg;

    //encryption
    int n = msg.size();
    string cipher="";
    for(int i=0;i<n;i++){
        int cur = (msg[i]-97+3)%26+97;  //shift by 3
        cipher+=(char)cur;
    }
    cout<<endl<<"Cipher text: "<<endl<<cipher<<endl<<endl;

    //decryption
    string plain="";
    for(int i=0;i<n;i++){
        int cur = (cipher[i]-97-3+26)%26+97;  //shift by -3
        plain+=(char)cur;
    }
    cout<<"Plain text: "<<endl<<plain<<endl;

}