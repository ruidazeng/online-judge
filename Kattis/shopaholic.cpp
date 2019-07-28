#include <iostream>
#include <algorithm>
#include <vector>

int main()
{
    int N;
    std::cin >> N;
    std::vector<int> vec;
    while(N--){
        int p;
        std::cin >> p;
        vec.push_back(p);
    }
    std::sort(vec.begin(), vec.end(), std::greater<int>());
    int index = 1;
    long long saved = 0;
    for(auto &x: vec){
        if (index % 3 == 0){
            saved += x;
        }
        ++index;
    }
    std::cout << saved << std::endl;
    return 0;
}