l = int(input()) # min
d = int(input()) # max
x = int(input())
m = l # max set to min
n = None

def digit_sum(num):
  return sum(int(char) for char in str(num))

for i in range(l, d + 1):
    if digit_sum(i) == x:
        if n is None:
            n = i
        if i > m:
            m = i

print(n)
print(m)