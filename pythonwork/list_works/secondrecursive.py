text="abbcdce"                  #19,wed
wc={}                            
duplist=[]#b,c

for ch in text:
    if ch in wc:
        duplist.append(ch)
    else:
        wc[ch]=1 #ch=a
print(duplist[1])#0=b,1=c
