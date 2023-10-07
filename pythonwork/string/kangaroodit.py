source_word="debilish"
target_word="devil" #lived?
wc={}
is_kangaroo=True
for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
for ch in target_word:
    # ch=d
    if ch in wc:
        #extract corrent value from wc
        cur_val=wc[ch]
        if cur_val>0:
            wc[ch]-=1
        else:
            is_kangaroo=False
            break
print(is_kangaroo)    