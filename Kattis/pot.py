n = int(input())
sum = 0

for x in range(n):
    p_i = input()
    expn = p_i[-1]
    sum += int(p_i[:-1]) ** int(expn)

print(sum)