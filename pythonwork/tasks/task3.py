# . Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, disp
# lay the message “You can learn to drive”, if they are 16, display the message“You can buy a lott
# ery ticket”,if they are under 16, display the message “You can go for treat”.





age=int(input("ange ="))
if age>=18:
    print("you can vote")
elif age==17:
    print("you can learn to drive")
elif age ==16:
    print("you can buy a lottery tickeet")
else:
    print("you can go for treat")