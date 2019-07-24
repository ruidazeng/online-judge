N, M = map(int, input().split())

if N - M > 0:
    if N - M == 1:
        print("Dr. Chaz needs 1 more piece of chicken!")
    else:
        print("Dr. Chaz needs", N-M, "more pieces of chicken!")
elif N - M < 0:
    if abs(N - M) == 1:
        print("Dr. Chaz will have 1 piece of chicken left over!")
    else:
        print("Dr. Chaz will have", abs(N-M), "pieces of chicken left over!")