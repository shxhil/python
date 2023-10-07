#linear searching

lst=[10,2,13,14,5]
element=13
i=0
limit=len(lst)
is_present=False
while(i<limit):
    cur_value=lst[i]
    i+=1
    if cur_value==element:
        is_present=True
        break
print(is_present)


#to overcome more time consuming in this search=bineary search
# travel fully each and every element in the list