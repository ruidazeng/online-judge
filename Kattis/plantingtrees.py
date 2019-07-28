n = int(input())
trees = sorted([int(x) for x in input().split()])

for i in range(n):
    trees[i] += n - i + 1

print(max(trees))