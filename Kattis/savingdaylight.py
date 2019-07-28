import sys
for line in sys.stdin:
    m, d, y, start, end = line.split()
    start_hour, start_min = map(int, start.split(':'))
    end_hour, end_min = map(int, end.split(':'))
    duration_hour = end_hour - start_hour
    duration_min = end_min - start_min
    if duration_min < 0:
        duration_hour -= 1
        duration_min += 60
    print(m, d, y, duration_hour, 'hours', duration_min, 'minutes')
