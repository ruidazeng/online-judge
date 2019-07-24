R, C = map(int, input().split())

grid = [None]*R
for r in range(R):
    grid[r] = list(input())

# For each 2x2 see if it contains any buildings
# If not count number of cars and add one to one of the counts

squashed = [0] * 6
for r in range(R - 1):
    for c in range(C - 1):
        car_squash = 0
        # 2x2 "coordinates"
        for r_mod, c_mod in ((0, 0), (0, 1), (1, 0), (1, 1)):
            if grid[r + r_mod][c + c_mod] == '#':
                car_squash = -1
                break
            elif grid[r + r_mod][c + c_mod] == 'X':
                car_squash += 1
        squashed[car_squash] += 1

# Print out total number of parking spaces Mirko can park
# on if he squashes 0 cars (first line), 1 car (second line),
# 2 cars (third line), 3 cars (fourth line), 4 cars (fifth line).

for s in squashed[:-1]:
    print(s)