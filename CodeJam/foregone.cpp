#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
  ll A,B;
void digits(ll Num,vector<int> &Digits){
  ll digit;
  while(Num!=0){
    digit= Num%10;
    Digits.push_back(digit);
    Num = Num/10;
  }
}

void findAB(vector<int> &Digits){
  ll len = Digits.size(),i;
  for(i=0;i<len;i++){
    if(Digits[i] == 4){
      B = B + pow(10,i);
      Digits[i]--;
    }
    A = A + Digits[i]*pow(10,i);
  }

}
int main(){
  std::cin.sync_with_stdio(false);
  ll T,i,N;
  cin>>T;
  for(i=1;i<=T;i++){
    cin>>N;
    A= 0;
    B = 0;
    vector<int> Digits;
    digits(N,Digits);
    findAB(Digits);
    cout<<"Case #"<<i<<": "<<A<<" "<<B<<endl;
  }
}
