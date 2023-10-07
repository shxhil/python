#3digit / 2digit R 2digit / min 2 max 3digit alphabet 
from re import*
tyre=input("enter the code=")
rule="[\d]{3}/[\d]{2}[R] [\d]{2}/[\d]{2,3}[A-Z]?"
matcher=fullmatch(rule,tyre)
print("invalid" if matcher==None else "valid")