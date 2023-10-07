# Write a program to print table of a number accepted by user. 



num=int(input("enter the number"))
# limit=int(input("limit="))
for i in range(1,num+1):
    if i%2==0:
        print(i)
        i+=1