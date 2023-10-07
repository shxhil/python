number=[1,4,10,11,12]

even_list=[]
odd_list=[]
for i in number:
    # print(i)
    if i %2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(odd_list)
print(even_list)