text="ababbcdcef"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

for k,v in wc.items():
    if v==1:
        print(k)



#adding in box
#a=1
#b=1
#......
