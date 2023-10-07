num=int(input("enter the number="))
mul=0
for i in range(1,11):
    mul=i*num
    print(mul)
ch=int(input("check="))
if num%ch==0:
    print("true")
else:
    print("false")