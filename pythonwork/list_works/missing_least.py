number=[1,3,4,5,6]
number.sort()
for i in range(0,len(number)-1):
    miss=number[i+1]-number[i]
    if miss!=1:
        num=number[i]+1
        print(num,"is missing")
        
