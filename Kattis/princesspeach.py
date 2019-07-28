N, Y = map(int, input().split())
taboos = [] # Python set
for _ in range(Y):
    taboos.append(int(input()))
taboos = set(taboos)
for i in range(N):
    if i not in taboos:
        print(i)
print("Mario got", len(taboos), "of the dangerous obstacles.")