from math import sqrt, ceil
from array import *

T = int(input())
for _ in range(T):
    # readin
    plain_text = input()
    text_len = len(plain_text)
    
    k = ceil(sqrt(text_len))
    # k x k matrix
    m = k * k
    
    asteriks = m - text_len
    
    text_matrix = [[None for _ in range(k)] for _ in range(k)]
    traversal = 0
    # make plain text
    for i in range(k):
        for j in range(k):
            if traversal >= text_len:
                text_matrix[i][j] = '*'
            else:
                text_matrix[i][j] = plain_text[traversal]
            traversal += 1
    
    cipher_matrix = [[None for _ in range(k)] for _ in range(k)]
    # decipher 
    for i in range(k):
        for j in range(k):
            cipher_matrix[i][j] = text_matrix[k - 1 - j][i]
    
    # print the matrix without '*'
    for i in range(k):
        for j in range(k):
            if cipher_matrix[i][j] != '*':
                print(cipher_matrix[i][j], end = '')
    # next line 
    print()