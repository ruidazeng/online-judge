from math import sqrt

a, b, c, d = map(int, input().split())

# So, this formula is maximized only when opposite
# angles sum to pi(180).
# Then we can use a simplified form of
# Bretschneider’s formula to get the (maximum) area.
semiperimeter = (a + b + c + d) / 2

k = sqrt((semiperimeter-a)*(semiperimeter-b)*
(semiperimeter-c)*(semiperimeter-d))

# This formula is called as Brahmagupta’s formula .

print(k)