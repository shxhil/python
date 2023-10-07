#bineary search
lst=[10,2,13,14,5]
element=14
lst.sort()
lower=0
upper=len(lst)-1
is_present=False
while(lower<=upper):
    mid=(upper+lower)//2
    if element==lst[mid]:
        is_present=True
        break
    elif element<lst[mid]:
                #value,not index(lst[mid])
        upper=mid-1
    elif element>lst[mid]:
        lower=mid+1
print(is_present)
