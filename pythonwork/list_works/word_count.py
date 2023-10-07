text="good morning good evening"
words=text.split(" ")
# print(words)
# words.count("good")
wc={}#good=1,mornnig=1,

for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1 #first exicute else case
print(wc)

