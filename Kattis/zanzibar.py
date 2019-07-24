t = int(input())

for _ in range(t):
    lower_bound = 0
    numbers = [int(x) for x in input().split()]
    for i in range(len(numbers) - 2):
        if numbers[i + 1] > 2 * numbers[i]:
            lower_bound += numbers[i+1] - 2 * numbers[i]
    print(lower_bound)