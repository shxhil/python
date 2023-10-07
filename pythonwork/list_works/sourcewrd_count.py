source_word="decreased"
wc={}
for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(wc)