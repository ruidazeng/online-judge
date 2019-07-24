P, N = map(int, input().split())
parts_replaced = []

for day in range(N):
    part = input()
    if part not in parts_replaced:
        parts_replaced.append(part)
    if len(parts_replaced) == P:
        print(day + 1)
        break
    
if len(parts_replaced) != P:
    print("paradox avoided")