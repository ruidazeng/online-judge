#include <iostream>
#include <map>
#include <vector>
#include <utility>
#include <algorithm>

void solve() {
    int n;
    std::cin >> n;
    std::map<std::string, int> freq;
    std::string name;
    int count;
    for (int i = 0; i < n; ++i) {
        std::cin >> name >> count;
        freq[name] += count;
    }

    std::vector<std::pair<int, std::string>> out;
    for (auto& p : freq) {
        out.emplace_back(-p.second, p.first);
    }
    std::sort(begin(out), end(out));
    std::cout << out.size() << '\n';
    for (auto& p : out) {
        std::cout << p.second << ' ' << (-p.first) << '\n';
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int T;
    std::cin >> T;
    while (T-- > 0) {
        solve();
    }
    
    return 0;
}
