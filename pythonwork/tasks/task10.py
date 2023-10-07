
# 0.Ask the user to enter their name and a number. If the number is less than 10, then display their name t
# hat number of times; otherwise display the message “Too high” 



name=(input("enter the name="))
num=int(input("number="))
start=1
if num<=10:
        while(start<=num+1):
            print(name)
            start+=1
else:
        print("too high")