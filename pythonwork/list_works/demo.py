text="good morning good evening"
v=text.split()

wc={}
for i in v:
    if i in wc:
        print(wc)
        wc[i]+=1
    else:
        wc[i]=1

# print(wc)
