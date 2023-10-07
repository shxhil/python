#starting with an alphabet k,l,m
#second place that must be a digit and that divisible n/3
#followed by any number of characters

from re import*
variable=input("enter variable=")

rule="[k-mK-m][369][\w]*"
matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")