T = int(input())

for _ in range(T):
    name, date1, date2, courses = input().split()
    year1, _, _ = map(int, date1.split('/'))
    year2, _, _ = map(int, date2.split('/'))
    
    if year1 >= 2010 or year2 >= 1991:
        print(name, "eligible")
    elif int(courses) > 40:
        print(name, "ineligible")
    else:
        print(name, "coach petitions")