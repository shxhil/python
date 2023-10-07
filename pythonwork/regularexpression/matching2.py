# from re import*
# text="abcdABCD7e9fk"
# pattern="[a-zA-Z]"
# #       
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(f"location ={m.start()} pattern matched={m.group()}")


#no numbers
from re import*
text="abcdAB#&CD7e9fk"
pattern="[^0-9]"# \d
#       
matcher=finditer(pattern,text)

for m in matcher:
    print(f"location ={m.start()} pattern matched={m.group()}")
