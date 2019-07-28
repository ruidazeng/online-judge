sentence = input().split()

ae = 0
for word in sentence:
    if 'ae' in word:
        ae += 1

if ae/len(sentence) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")