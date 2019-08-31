#include <iostream>
#include<string>
#include <bits/stdc++.h> 

using namespace std;

int main()
{
    int i,tcase;
    cin>>tcase;
    for(i=0;i<=tcase;i++)
    {
        string str;
        getline(cin,str);
        reverse(str.begin(),str.end());
        cout<<str<<endl;
    }    
    return 0;
}