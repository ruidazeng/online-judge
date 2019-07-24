from string import ascii_lowercase

n = int(input())

for _ in range(n):
    tmp = ascii_lowercase
    string = input().lower()
    for char in tmp:
        if char in string:
            tmp = tmp.replace(char,'')
    print("pangram") if not tmp else print("missing", tmp)