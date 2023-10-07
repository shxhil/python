def number(a,b,c):
    if (a>b) and (a>c) :
        print("a is greater")
    elif (b>a) and(b>c):
        print("b is greater")
    elif(c>a)and (c>b):
    #else: 
        print("c is greater")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
number(a,b,c)