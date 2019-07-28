#include <bits/stdc++.h>
using namespace std;

int num_of_prime_factors(const int to_factor) {
    int count = 0;
    int factor_to_try = 2;
    int shrinking_number = to_factor;
    while (shrinking_number > 1) {
        if (factor_to_try > sqrt(to_factor)) {
            break;
        }
        else if (!(shrinking_number % factor_to_try)) {
            ++count;
            shrinking_number /= factor_to_try;
        }
        else {
            ++factor_to_try;
        }
    }
    if (shrinking_number != 1) ++count;
    return count;
}

int main()
{
    int n;
    cin >> n;
    cout << num_of_prime_factors(n) << endl;
    return 0;
}
