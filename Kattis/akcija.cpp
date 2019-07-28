#include <bits/stdc++.h>
using namespace std;

int main()
{
    int length;
    cin >> length;
    priority_queue<int> pq;
    
    for(int i = 0; i < length; ++i) {
        int x;
        cin >> x;
        pq.push(x);
    }
    int total = 0;
    for(int i = 1; i <= length; ++i) {
        int temp;
        temp = pq.top();
        pq.pop();
        if (i % 3 != 0) {
            total += temp;
        }
    }
    cout << total << endl;

    return 0;
}