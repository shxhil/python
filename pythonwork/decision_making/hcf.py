num1=24 #date4/7
num2=18

for i in range(1,num2+1):
    if num1%i==0 and num2%i==0:   #i is hcf(eg=18)
        hcf=i
print(hcf)