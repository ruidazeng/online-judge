T = int(input())

for _ in range(T):
    k = int(input())
    x = 0 # bus leaves the last stop empty
    for _ in range(k):
        x += 0.5
        x *= 2
    print(int(x))