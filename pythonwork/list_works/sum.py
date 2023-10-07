#sum of 2 numbers=sum (8) in a list             20,thursday
lst=[2,3,5,7,4]
#    0,1,2,3,4
sum=9 # eg=2+7=9
lst.sort()
lower=0
upper=len(lst)-1#spesific kodkksnoond ahn -1

while(lower<upper):
    cur_sum=lst[lower]+lst[upper]
    if cur_sum==sum:
        print("pairs",lst[lower],lst[upper])
        break
    elif cur_sum<sum:
        lower+=1
    else:#cur_sum>sum
        upper-=1