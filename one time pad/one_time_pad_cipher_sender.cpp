#include<bits/stdc++.h>
using namespace std;

int main(){
    ifstream fin("pad_sequence_sender.txt");
    ofstream fout("cipher_text.txt");

    string pad,msg,cipher="";
    fin>>pad;
    fin.close();
    cout<<"Plain text: "<<endl;
    cin>>msg;

    int n = msg.size();
    for(int i=0;i<n;i++){
        int cur = (msg[i]-97+pad[i]-97)%26+97;
        cipher+=(char)cur;
    }

    pad.erase(0,n);
    ofstream fout1("pad_sequence_sender.txt");
    fout1<<pad;
    fout<<cipher;

    cout<<endl<<"Cipher text: "<<endl<<cipher<<endl;
}
