from string import ascii_lowercase as lowcase

N, M = map(int, input().split())

key = input()
cipher = input()
decipher = "" + key

for ch in cipher[::-1]:
    # Keyword is essentially the lastest letter from
    # plaintext (since we're going backwards)
    keyword = decipher[N - 1]
    decipher = lowcase[(lowcase.index(ch) + 26)%26 -
    lowcase.index(keyword)] + decipher

# Don't print the "secret" n letters prefix
print(decipher[N:])