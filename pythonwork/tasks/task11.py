# Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the n
# ames and after each name display “[name] has been invited”. If they enter a number which is 10 or highe
# r, display the message “Too many people”. 


num=int(input("enter the number of people="))
if num<10:
    for i in range(1,num+1):
        names=input("enter the names=")
        i+=1
    
        print(names,"has been invited")
else:
    print("too high")
