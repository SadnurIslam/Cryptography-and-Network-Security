/*
workflow:
1. Randomly generate a pad sequence and store it in two file one for sender and one for receiver.
2. Sender will read the pad sequence and the message to be sent and generate the cipher text and store it in a file.
3. Sender will also update the pad sequence by erasing the used part and store it back in the file.
4. Receiver will read the pad sequence and the cipher text and generate the plain text and output it.
5. Receiver will also update the pad sequence by erasing the used part and store it back in the file.
*/



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
