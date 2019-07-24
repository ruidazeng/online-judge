t = int(input())

for _ in range(t):
   _ = int(input())
   stores = list(map(int, input().split()))
   min_dis = (max(stores) - min(stores)) * 2
   print(min_dis)