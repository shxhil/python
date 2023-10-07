#2. Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is betw
# een 10 and 20, display “Correct”, otherwise display “Too high”.


while(True):#to iterate always
    num=int(input("enter the number= "))
    if num<10:
        print("too low")
    elif num>=10 and num<=20:
        print("correct")
    else:
        print("too high")
        break