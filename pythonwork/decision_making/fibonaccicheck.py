num=int(input("enter range="))
prev=0
current=1
is_fibo=False
start=1
sum=0
while(start<=25):
    sum=prev+current
    prev=current
    current=sum
    start+=1
    if num==sum:
        is_fibo=True
        break
print(is_fibo)


