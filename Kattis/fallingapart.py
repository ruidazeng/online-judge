n = int(input())
intz = [int(x) for x in input().split()]
alice = 0
bob = 0
for i, num in zip(range(n), sorted(intz)[::-1]):
    if i%2 == 0:
        alice += num 
    else:
        bob += num
print(alice, bob)