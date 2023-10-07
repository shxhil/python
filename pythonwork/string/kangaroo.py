text=input("IN= ") #"chicken"
word1=sorted(text)
out=input("OUT= ") #"hen"
word2=sorted(out)

value=True
for w in word2:
    if w in word1:
        value=False
        break
    else:
        value=True
    
print(value)




