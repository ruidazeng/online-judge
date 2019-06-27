n = int(input())

for x in range(n):
    b, p = input().split()
    b, p = [int(b), float(p)]
    const_hr = 60.0 / p
    min_abpm = 60.0 * b / p - const_hr
    cal_bpm = 60.0 * b / p
    max_abpm = 60.0 * b / p + const_hr
    print(format(min_abpm,'.4f'), format(cal_bpm,'.4f'), format(max_abpm,'.4f'))