
# Ask the user to enter 5 numbers and find the average using for or while loop



sum=0
for i in range(1,6):
    num=int(input("enter the number="))
    sum=num+sum
    avg=sum/5
print("average",avg)
