A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

juice = min(A/I, B/J, C/K)
a_leftov = A - I * juice
b_leftov = B - J * juice
c_leftov = C - K * juice

print(a_leftov, b_leftov, c_leftov)