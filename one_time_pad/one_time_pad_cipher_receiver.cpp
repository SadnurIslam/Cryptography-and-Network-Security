#include<bits/stdc++.h>
using namespace std;

int main(){
    ifstream fin("pad_sequence_receiver.txt");
    ifstream fin1("cipher_text.txt");

    string pad,msg="",cipher="";
    fin>>pad;
    fin.close();

    fin1>>cipher;
    fin1.close();

    cout<<"Cipher text: "<<endl;
    cout<<cipher<<endl;

    int n = cipher.size();
    for(int i=0;i<n;i++){
        int cur = (cipher[i]-97-(pad[i]-97)+26)%26+97;
        msg+=(char)cur;
    }

    pad.erase(0,n);
    ofstream fout1("pad_sequence_receiver.txt");
    fout1<<pad;
    
    cout<<endl<<"Plain text: "<<endl<<msg<<endl;
}
