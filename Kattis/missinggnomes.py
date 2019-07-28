m, n = map(int, input().split())
subseq = list()
target = list()
result = list()

for _ in range(n):
    subseq.append(int(input()))

traversal_index = 0

start = 1
# 1000x faster than list comprehension
target = list(set(range(1, m + 1)) - set(subseq))
# O(N log N)
target = sorted(target)
        
index = 0

# this should be O(N)
while True:
    if index >= n:
        result.extend(target)
        break
    if not target:
        result.extend(subseq[index:])
        break
    if subseq[index] < target[0]:
        result.append(subseq[index])
        index += 1 
    else:
        result.append(target[0])
        target.pop(0)

print(*result)