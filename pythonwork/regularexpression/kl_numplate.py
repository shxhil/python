from re import*
number=input("enter the number=")
rule="(kl)\d{2}[A-Z]{1,2}[\d]{4}"
matcher=fullmatch(rule,number)
print("invalid" if matcher==None else "valid")