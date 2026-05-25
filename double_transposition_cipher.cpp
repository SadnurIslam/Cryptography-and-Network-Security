// double cipher transposition: use the cipher text from first encryption
// as input again for the second encryption

#include<bits/stdc++.h>
using namespace std;

string encrypt(string msg, int col){
    int n = msg.size();
    int row = ceil(1.0*n/col);
    vector<vector<char>>table(row,vector<char>(col,'?'));
    int k = 0;
    for(int i=0;i<row;i++){
        for(int j=0;j<col && k<n;j++){
            table[i][j] = msg[k];
            k++;
        }
    }
    string cipher = "";
    for(int i=0;i<col;i++){
        for(int j=0;j<row;j++){
            if(table[j][i]=='?')continue;
            cipher+=table[j][i];
        }
    }
    return cipher;
}

string decrypt(string cipher, int col){
    string plain = "";
    int n = cipher.size();
    int row = n/col;
    int rem = n-row*col;
    vector<vector<char>>table(row+1,vector<char>(col,'?'));
    int k = 0;
    for(int i=0;i<col;i++){
        for(int j=0;j<row && k<n;j++){
            table[j][i] = cipher[k];
            k++;
        }
        if(rem>0 && k<n){
            table[row][i] = cipher[k];
            rem--;
            k++;
        }
    }
    for(int i=0;i<=row;i++){
        for(int j=0;j<col;j++){
            if(table[i][j]=='?')break;
            plain+=table[i][j];
        }
    }
    return plain;
}

int main(){
    
    string msg = "DEPARTMENTOFCOMPUTERSCIENCEANDENGINEERING";
    int width;
    cout<<"Width of transposition table: ";
    cin>>width;

    cout<<"Plain text: "<<msg<<endl;
    // string cipher = encrypt(msg,width);
    // cout<<"Cipher text: "<<cipher<<endl;
    string double_cipher = encrypt(encrypt(msg,width),width); //double cipher
    cout<<"Double cipher text: "<<double_cipher<<endl;
    
    string plain = decrypt(decrypt(double_cipher,width),width);
    cout<<"Plain text: "<<plain<<endl;
    cout<<((msg==plain)?"success":"failed")<<endl;
}