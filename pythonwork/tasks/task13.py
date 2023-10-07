# Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the messag
# e “Too low” and ask them to try again. If they enter a value above 20, display the message “Too high” and
# ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then dis
# play the message “Thank you”.



while True:# when while loop full true program will stop
    num=int(input("enter a number btw 10 and 20="))
    start=1
    if num>=10 and num<=20:
        print("thank you")
    elif num<10:
     print("too low, try again")
    elif num>20:
     print("too high,try again")
     