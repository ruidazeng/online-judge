K = int(input())
num_a = 1
num_b = 0

for _ in range(K):
    # swap, num_a is good
    num_a, num_b = num_b, num_a
    # num_b needs to add since B -> BA
    num_b += num_a

print(num_a, num_b)