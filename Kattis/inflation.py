N = int(input())
canisters = sorted([int(x) for x in input().split()])
f = 1 # highest possible percentage

for i in range(1, N + 1):
    if canisters[i-1] == i:
        continue
    elif canisters[i-1] < i:
        percent = canisters[i-1] / i
        if percent < f:
            f = percent
    else:
        f = "impossible"
        break

print(f)