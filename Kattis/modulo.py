numbers = []
N = 10
MOD = 42

for _ in range(N):
    n = int(input())
    mod = n % MOD
    if mod not in numbers:
        numbers.append(mod)

print(len(numbers))