/*
workflow:
1. randomly generate substitution table and store it in a file (for length 3 and length 2 and length 1).
2. read the substitution table and the plain text and generate the cipher text and output it.
3. read the substitution table and the cipher text and generate the plain text and output it.
*/


#include<bits/stdc++.h>
using namespace std;

int main(){
    ifstream fin("polygram_table.txt");
    map<string,string>ptc,ctp;
    string s1,s2,plain,cipher="";
    while(fin>>s1>>s2){
        ptc[s1] = s2;
        ctp[s2] = s1;
    }

    cout<<"Plaint text: "<<endl;
    cin>>plain;

    //encryption
    int n = plain.size();
    for(int i=0;i<n-2;i=i+3){
        string str = plain.substr(i,3);
        cipher+=ptc[str];
    }
    if(n%3!=0){
        string str = plain.substr(n/3*3);
        cipher+=ptc[str];
    }
    cout<<endl<<"Cipher text: "<<endl<<cipher<<endl;


    //decryption
    n = cipher.size();
    string msg="";
    for(int i=0;i<n-2;i=i+3){
        string str = cipher.substr(i,3);
        msg+=ctp[str];
    }
    if(n%3!=0){
        string str = cipher.substr(n/3*3);
        msg+=ctp[str];
    }
    cout<<endl<<"Plain text: "<<endl<<msg<<endl;

}
