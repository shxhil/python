from re import*
text="aabbcaabdaaa"
 #    0123456789
# pattern="a+"#one or more occurence of a
pattern="a*"# zero or more occurence of a
matcher=finditer(pattern,text)
for m in matcher:
    print(m.group(),m.start())