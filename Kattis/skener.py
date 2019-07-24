r, c, z_r, z_c = map(int, input().split())

grid = [input() for _ in range(r)]

for line in grid:
    for _ in range(z_r):
        for k in line:
            print(k*z_c, end='')
        print()