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
}
