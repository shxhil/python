year=int(input("enter the  year="))
if(year%4==0 and year%100!=0) or (year%400==0):
    #non century year condition
    print(f"{year} is leapyear")
else:
    print(" not leapyear ")
#     #00 end with doublezero centur
# y 400

# if(year%100==0)and (year%400==0): #for century year
#     print("leap year")
# elif(year%400==0)and (year%100!=0):
#     print("leap year")
# else:
#     print("not leap year")
# result="leapyear" if year%400==0 and year%100==0 else "leapyear" if year %100!=0 and year%4==0 else "not leapyear"
# print(result)