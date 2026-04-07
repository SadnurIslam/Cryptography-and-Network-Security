#include<bits/stdc++.h>
using namespace std;

int main(){
    ofstream fout("polygram_table.txt");
    srand(time(0));
    vector<string>vs,vv;
    for(char i='a';i<='z';i++){
        for(int j='a';j<='z';j++){
            for(int k='a';k<='z';k++){
                string s="";
                s.push_back(i);
                s.push_back(j);
                s.push_back(k);
                vs.push_back(s);
                vv.push_back(s);
            }
        }
    }
    int n = vs.size();
    for(int i=0;i<n;i++){
        int sz = vv.size();
        int r = rand()%sz;
        fout<<vs[i]<<" "<<vv[r]<<endl;
        vv.erase(vv.begin()+r);
    }

    vs.clear();
    vv.clear();

    for(char i='a';i<='z';i++){
        for(int j='a';j<='z';j++){
            string s="";
            s.push_back(i);
            s.push_back(j);
            vs.push_back(s);
            vv.push_back(s);
        }
    }

    n = vs.size();
    for(int i=0;i<n;i++){
        int sz = vv.size();
        int r = rand()%sz;
        fout<<vs[i]<<" "<<vv[r]<<endl;
        vv.erase(vv.begin()+r);
    }

    vs.clear();
    vv.clear();

    for(char i='a';i<='z';i++){
        string s="";
        s.push_back(i);
        vs.push_back(s);
        vv.push_back(s);
    }

    n = vs.size();
    for(int i=0;i<n;i++){
        int sz = vv.size();
        int r = rand()%sz;
        fout<<vs[i]<<" "<<vv[r]<<endl;
        vv.erase(vv.begin()+r);
    }
    
}