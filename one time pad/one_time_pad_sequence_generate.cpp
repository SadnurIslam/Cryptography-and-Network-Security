#include<bits/stdc++.h>
using namespace std;

int main(){
    ofstream fout("pad_sequence_sender.txt");
    ofstream fout1("pad_sequence_receiver.txt");
    srand(time(0));

    string sequence;

    for(int i=0;i<1000;i++){
        int r = rand()%26+97;
        sequence.push_back(char(r));
    }

    fout<<sequence<<endl;
    fout1<<sequence<<endl;
}
