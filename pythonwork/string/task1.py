name="i have one car 2 bikes 3 cycles"
# numbers only
words=name.split(" ")
# print(words)
for w in words:# w=i, have ,one ,car ,2.....
    if w.isdigit():#2,3
        print(w)

