p, q, s = map(int, input().split())

for x in range(1, s + 1):
    if x % p == 0 and x % q == 0:
        print("yes")
        quit()
print("no")