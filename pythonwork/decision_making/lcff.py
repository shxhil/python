num1=int(input("enter the first number= "))
num2=int(input("enter the second number= "))
if num1>num2:
    num=num1
else:
    num=num2
for i in range(num,1,-1):
    if num1%i==0 and num2%i==0:   #i is hcf(eg=18)
        hcf=i
        print(hcf)