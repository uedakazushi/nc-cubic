// Direct GF(2) determinant verification of the specified square minor.
// Highest-bit pivots; independent of the low-bit block-table rank search.
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;using U=uint64_t;
int main(int argc,char**argv){
 if(argc!=3)return 2;ifstream in(argv[1],ios::binary),wit(argv[2]);uint32_t n,rows;in.read((char*)&n,4);in.read((char*)&rows,4);
 vector<uint32_t> ids;uint32_t v;while(wit>>v)ids.push_back(v);
 if(ids.size()!=n||!is_sorted(ids.begin(),ids.end())||adjacent_find(ids.begin(),ids.end())!=ids.end()||ids.back()>=rows)return 3;
 int words=(n+63)/64,bytes=(n+7)/8;vector<vector<U>> piv(n);vector<U>a(words);int rank=0;auto start=chrono::steady_clock::now();
 for(uint32_t rr:ids){
  fill(a.begin(),a.end(),0);in.seekg(8+uint64_t(rr)*bytes);in.read((char*)a.data(),bytes);if(!in)return 4;
  int wi=words-1;
  while(wi>=0){
   if(!a[wi]){--wi;continue;}int p=wi*64+63-__builtin_clzll(a[wi]);
   if(piv[p].empty()){piv[p]=a;++rank;break;}
   const U* q=piv[p].data();for(int j=0;j<=wi;++j)a[j]^=q[j];
  }
  if(rank%5000==0)cerr<<"verified="<<rank<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
  if(wi<0){cerr<<"dependent row "<<rr<<"\n";return 5;}
 }
 cout<<"{\"order\":"<<n<<",\"prime\":2,\"determinant\":1,\"verified\":"<<(rank==int(n)?"true":"false")<<"}\n";
 return rank==int(n)?0:6;
}
