lst1=[10,11,4,12]
lst2=[9,10,11,6]

#algorithm for printing common element from array
#without using in (bcz in only in python)


lst1.sort()#sorted for easily incriment or dicrement elements
lst2.sort()
# print(lst2,lst1)

p1,p2=0,0
while (p1<len(lst1) and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print(lst2[p2])#bcz of common both needed to incriment to next line
        p1+=1
        p2+=1
    elif lst1[p1]<lst2[p2]:#smallest needed to increment(p1 is)
        p1+=1
    else:#lst1[p1]>lst2[p2]
        p2+=1
