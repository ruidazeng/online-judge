N = int(input())
displayed_min = 0
actual_second = 0

for _ in range(N):
    m, s = map(int, input().split())
    displayed_min += m 
    actual_second += s

sl_min = (actual_second/60) / displayed_min

if sl_min <= 1:
    print("measurement error")
else:
    print(format(sl_min, '.9f'))