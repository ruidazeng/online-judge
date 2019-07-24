import sys

codes = {
    'A': '.-',
    'H': '....',
    'O': '---',
    'V': '...-',
    'B': '-...',
    'I': '..',
    'P': '.--.',
    'W': '.--',
    'C': '-.-.',
    'J': '.---',
    'Q': '--.-',
    'X': '-..-',
    'D': '-..',
    'K': '-.-',
    'R': '.-.',
    'Y': '-.--',
    'E': '.',
    'L': '.-..',
    'S': '...',
    'Z': '--..',
    'F': '..-.',
    'M': '--',
    'T': '-',  
    'G': '--.',
    'N': '-.',
    'U': '..-',
    '_': '..--',
    '.': '---.',
    ',': '.-.-',
    '?': '----'
}

rev_codes = {v: k for k, v in codes.items()}

for l in sys.stdin.readlines():
    
    # The strip() removes characters from both left
    # and right based on the argument (a string
    # specifying the set of characters to be removed).
    
    l = l.strip()
    coded = ''.join([codes[c] for c in l])
    code_lens = [len(codes[c]) for c in l][::-1]
    decoded = ''
    
    for length in code_lens:
        code = coded[:length]
        coded = coded[length:]
        decoded += rev_codes[code]
    print(decoded){\rtf1}