n = int(input())
name = []
    
for _ in range(n):
    name.append(input())
if name == sorted(name):
    print("INCREASING")
elif name == sorted(name)[::-1]:
    print("DECREASING")
else:
    print("NEITHER")