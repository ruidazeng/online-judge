_ = input()
accounts = [int(x) for x in input().split()]

expense = 0
for money in accounts:
    if money < 0:
        expense += money

print(-expense)