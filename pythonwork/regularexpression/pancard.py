#first three character must be  any random uppercase alphabet
#in 4th place P,FA,C,H,T
#in 5th place uppercase random alphabet
#4 digit
#in last place random alphabet


from re import*
pancard=input("enter pancard=")

rule="[A-Z]{3}[PFACHT]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"
matcher=fullmatch(rule,pancard)
print("invalid" if matcher==None else "valid")