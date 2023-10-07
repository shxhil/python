text="abcda"                            #1st recursive character
wc={}
for ch in text:
    if ch in wc:
        print("first recursive character",ch)
        break
    else:
        wc[ch]=1
