lst="dehykulifhgfj"
vcount=[]
ccount=[]
vowels="a","e","i","o","u"

for i in lst:
    if i in vowels:
        vcount.append(i)
    else:
        ccount.append(i)

print(vcount)
print(ccount)
