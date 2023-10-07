num=int(input("enter the number="))

if num>=2:
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
else:
    is_prime=False
print(is_prime)