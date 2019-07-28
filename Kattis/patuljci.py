DWARVES_NUM = 9
dwarves = [int(input()) for _ in range(DWARVES_NUM)]

sum = sum(dwarves)
two_fake_sum = sum - 100

for i in range(DWARVES_NUM):
    for j in range(DWARVES_NUM):
        if i != j and dwarves[i] + dwarves[j] == two_fake_sum:
            fake1 = i 
            fake2 = j

dwarves.pop(fake1)
dwarves.pop(fake2)

print('\n'.join([str(x) for x in dwarves]))

# Better solution (by CianLR):
#
# from itertools import combinations
#
# dvs = [int(input()) for _ in range(9)]
# for selects in combinations(dvs, 7):
#    if sum(selects) == 100:
#        print('\n'.join([str(x) for x in selects]))
#        break