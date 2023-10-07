# Write a program to print table of a number accepted by user. 



num=int(input("number ="))
k=int(input("limit ="))
for i in range(1,k+1):
    mul=num*i
    print(num,"*",i,"=",mul)
    i+=1