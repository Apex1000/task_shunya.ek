#include <bits/stdc++.h>
using namespace std;
int main() {
 int n;
    cin>>n;
 int socks[101] = {};
 for(int i = 0; i < n; i++) {
        int z;
        cin >> z;
        socks[z]++;
    }
 int count = 0;
 for(int i = 0; i <= 100; i++){
         count +=socks[i] / 2;
     }
 cout << count << endl;
 return 0;
}
