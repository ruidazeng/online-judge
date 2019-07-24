n = int(input())
days = []
sum = 0

for i in range(n):
    s_i, t_i = map(int, input().split())
    days = sorted(list(set(days) | set(range(s_i, t_i + 1))))
    # '|' is union
    # The list containing days does not 
    # have to be sorted in this problem.
for day in days:
    sum += 1
print(sum)