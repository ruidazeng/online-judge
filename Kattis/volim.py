k = int(input())
n = int(input())
PLAYERS = 8
TIME = 210 

for _ in range(n):
    t, z = input().split()
    t = int(t)
    if TIME - t < 0:
        if k % PLAYERS == 0:
            print(8)
        else:
            print(k % PLAYERS)
        break
    elif z == 'T':
        TIME -= t  
        k += 1
    else:
        TIME -= t