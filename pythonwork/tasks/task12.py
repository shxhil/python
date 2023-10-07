# Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the n
# ames and after each name display “[name] has been invited”. If they enter a number which is 10 or highe
# r, display the message “Too many people”. 


start=1
while(start<=5):
    
    num=int(input("enter a number="))
    if num>=5:
        print("the last number u entered was a",num)
        break
