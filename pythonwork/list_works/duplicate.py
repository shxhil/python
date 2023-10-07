num=[2,1,5,3,6,3,5,4,5]
num.sort()
duplicate=[]
for i in range(0,len(num)-1):
    a=num[i]
    b=num[i+1]
    if a==b:
     if a not in duplicate:
        duplicate.append(a)
print(duplicate)  